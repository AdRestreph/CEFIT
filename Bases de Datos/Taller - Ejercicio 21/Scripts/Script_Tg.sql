DELIMITER //

-- TR_ActualizarDisponibilidadRecinto
-- Se dispara al reservar un recinto, actualizando la tabla DISPONIBILIDAD_RECINTO
CREATE TRIGGER TR_ActualizarDisponibilidadRecinto
AFTER INSERT ON DETALLE_RECINTOS
FOR EACH ROW
BEGIN
    INSERT INTO DISPONIBILIDAD_RECINTO (ID_RECINTO, ESTADO, FECHA_INICIO, FECHA_FIN)
    VALUES (NEW.ID_RECINTO, 'OCUPADO', NEW.FECHA_HORA_INICIO, NEW.FECHA_HORA_FIN);
END //

-- TR_VerificarConflictosHorarios
-- Se dispara ANTES de insertar un nuevo recinto para asegurar que no haya conflicto
CREATE TRIGGER TR_VerificarConflictosHorarios
BEFORE INSERT ON DETALLE_RECINTOS
FOR EACH ROW
BEGIN
    DECLARE conflicto INT DEFAULT 0;

    -- Verificar conflictos en la tabla de DETALLE_RECINTOS (reservas existentes)
    SELECT COUNT(*) INTO conflicto
    FROM DETALLE_RECINTOS DR
    WHERE DR.ID_RECINTO = NEW.ID_RECINTO
      AND NEW.FECHA_HORA_FIN > DR.FECHA_HORA_INICIO
      AND NEW.FECHA_HORA_INICIO < DR.FECHA_HORA_FIN;

    IF conflicto > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: Conflicto de horario. El recinto ya está reservado.';
    END IF;

    -- Verificar conflictos en la tabla de DISPONIBILIDAD_RECINTO (mantenimiento)
    SELECT COUNT(*) INTO conflicto
    FROM DISPONIBILIDAD_RECINTO DR
    WHERE DR.ID_RECINTO = NEW.ID_RECINTO
      AND DR.ESTADO = 'MANTENIMIENTO'
      AND NEW.FECHA_HORA_FIN > DR.FECHA_INICIO
      AND NEW.FECHA_HORA_INICIO < DR.FECHA_FIN;

    IF conflicto > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: Conflicto de horario. El recinto está en mantenimiento.';
    END IF;
END //

-- TR_ActualizarInventarioEquipamiento
-- Se dispara al asignar equipamiento al evento, reduciendo el stock
CREATE TRIGGER TR_ActualizarInventarioEquipamiento
AFTER INSERT ON DETALLE_COSTO
FOR EACH ROW
BEGIN
    -- Solo si el costo es de tipo EQUIPAMIENTO
    IF NEW.TIPO_COSTO = 'EQUIPAMIENTO' AND NEW.ID_EQUIPAMENTO IS NOT NULL THEN
        UPDATE EQUIPAMENTO
        SET CANTIDAD_DISPONIBLE = CANTIDAD_DISPONIBLE - NEW.CANTIDAD
        WHERE ID_EQUIPAMENTO = NEW.ID_EQUIPAMENTO;
    END IF;
END //

-- TR_CalcularCostosEvento
-- Se dispara al insertar un costo y actualiza el presupuesto total del evento
CREATE TRIGGER TR_CalcularCostosEvento
AFTER INSERT ON DETALLE_COSTO
FOR EACH ROW
BEGIN
    DECLARE nuevo_presupuesto DECIMAL(10,2);

    -- Recalcular el presupuesto total usando la función
    SET nuevo_presupuesto = FN_CalcularPresupuestoEvento(NEW.ID_EVENTO);

    -- Actualizar el evento
    UPDATE EVENTO
    SET PRESUPUESTO_APROBADO = nuevo_presupuesto
    WHERE ID_EVENTO = NEW.ID_EVENTO;
END //

-- TR_GenerarCronogramaActividades (Lógica Simplificada)
-- Se dispara al confirmar el evento para iniciar la planificación
CREATE TRIGGER TR_GenerarCronogramaActividades
AFTER UPDATE ON EVENTO
FOR EACH ROW
BEGIN
    -- Asumimos que "Confirmado" es el estado que dispara la planificación.
    IF NEW.ESTADO_ACTUAL LIKE '%Confirmado%' AND OLD.ESTADO_ACTUAL NOT LIKE '%Confirmado%' THEN
        -- Aquí se insertaría la lógica compleja, pero por simplicidad se registra la acción:
        INSERT INTO ACTIVIDADES (NOMBRE, DESCRIPCION)
        VALUES (CONCAT('Planificación Inicial Evento ', NEW.ID_EVENTO), 'Generación automática de cronograma base.');

        -- NOTA: La lógica completa implicaría iterar sobre plantillas de actividades por TIPO_EVENTO
        -- e insertarlas en CRONOGRAMA_ACTIVIDADES y PLANIFICACION.
    END IF;
END //

DELIMITER ;