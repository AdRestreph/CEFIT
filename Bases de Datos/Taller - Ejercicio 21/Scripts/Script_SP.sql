DELIMITER //

-- CrearCotizacionEvento
-- Crea una cotización y los detalles de costo iniciales para un evento
CREATE PROCEDURE CrearCotizacionEvento (
    IN p_id_cliente INT,
    IN p_id_tipo_evento INT,
    IN p_titulo_evento VARCHAR(200),
    IN p_presupuesto_aprobado DECIMAL(10,2),
    OUT p_id_cotizacion INT
)
BEGIN
    -- 1. Insertar el evento base (estado inicial)
    INSERT INTO EVENTO (ID_TIPO_EVENTO, ID_CLIENTE, TITULO_EVENTO, PRESUPUESTO_APROBADO, ESTADO_ACTUAL)
    VALUES (p_id_tipo_evento, p_id_cliente, p_titulo_evento, p_presupuesto_aprobado, 'Cotizado');

    SET @id_evento_nuevo = LAST_INSERT_ID();

    -- 2. Insertar la cotización
    INSERT INTO COTIZACION (FECHA_EMISION, VALIDEZ, ID_CLIENTE, ID_TIPO_EVENTO, CONDICION_PAGO, REQUISITO_CONFIRMACION)
    VALUES (NOW(), 'VALIDO', p_id_cliente, p_id_tipo_evento, '50% anticipo', 'Firma digital');

    SET p_id_cotizacion = LAST_INSERT_ID();

    -- Nota: Los detalles de costos y servicios deben ser añadidos en pasos posteriores.

END //

-- ReservarRecinto
-- Reserva un recinto después de verificar su disponibilidad
CREATE PROCEDURE ReservarRecinto (
    IN p_id_evento INT,
    IN p_id_recinto INT,
    IN p_id_configuracion INT,
    IN p_fecha_inicio DATETIME,
    IN p_fecha_fin DATETIME,
    IN p_precio_hora DECIMAL(10,2)
)
BEGIN
    DECLARE horas DECIMAL(5,2);

    -- 1. Verificar disponibilidad usando la función
    IF FN_VerificarDisponibilidadPeriodo(p_id_recinto, p_fecha_inicio, p_fecha_fin) THEN

        SET horas = TIMESTAMPDIFF(HOUR, p_fecha_inicio, p_fecha_fin);

        -- 2. Insertar en DETALLE_RECINTOS
        INSERT INTO DETALLE_RECINTOS (ID_EVENTO, ID_RECINTO, ID_CONFIGURACION, FECHA_HORA_INICIO, FECHA_HORA_FIN, PRECIO_HORA, HORAS_RESERVADAS)
        VALUES (p_id_evento, p_id_recinto, p_id_configuracion, p_fecha_inicio, p_fecha_fin, p_precio_hora, horas);

        SELECT 'Reserva de recinto exitosa.' AS Mensaje;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: El recinto no está disponible en el período solicitado.';
    END IF;
END //

-- AsignarEquipamientoEvento
-- Asigna equipamiento si hay suficiente stock disponible
CREATE PROCEDURE AsignarEquipamientoEvento (
    IN p_id_evento INT,
    IN p_id_equipamento INT,
    IN p_cantidad_solicitada INT,
    IN p_precio_unitario DECIMAL(12,2),
    IN p_unidad_medida ENUM('HORA','DIA','UNIDAD','PERSONA','EVENTO')
)
BEGIN
    DECLARE stock_disponible INT;

    -- 1. Verificar stock
    SELECT CANTIDAD_DISPONIBLE INTO stock_disponible
    FROM EQUIPAMENTO
    WHERE ID_EQUIPAMENTO = p_id_equipamento;

    IF stock_disponible >= p_cantidad_solicitada THEN
        -- 2. Insertar en DETALLE_COSTO (asumiendo que es donde se registra el uso de equipamiento)
        INSERT INTO DETALLE_COSTO (ID_EVENTO, TIPO_COSTO, ID_EQUIPAMENTO, CONCEPTO, CANTIDAD, UNIDAD_MEDIDA, PRECIO_UNITARIO)
        VALUES (p_id_evento, 'EQUIPAMIENTO', p_id_equipamento, 'Alquiler de equipo', p_cantidad_solicitada, p_unidad_medida, p_precio_unitario);

        -- El TR_ActualizarInventarioEquipamiento se encargará de reducir el stock.
        SELECT 'Equipamiento asignado exitosamente.' AS Mensaje;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Stock insuficiente para el equipamiento solicitado.';
    END IF;
END //

-- ProgramarPersonalEvento
-- Asigna el personal disponible para un evento y marca su disponibilidad
CREATE PROCEDURE ProgramarPersonalEvento (
    IN p_id_evento INT,
    IN p_id_tipo_personal INT,
    IN p_rol VARCHAR(100),
    IN p_horas_trabajadas DECIMAL(6,2),
    IN p_fecha_inicio DATETIME,
    IN p_fecha_fin DATETIME
)
BEGIN
    DECLARE id_personal_encontrado INT;
    DECLARE tarifa DECIMAL(10,2);

    -- 1. Encontrar personal disponible
    SET id_personal_encontrado = FN_ObtenerPersonalDisponible(p_id_tipo_personal, p_fecha_inicio);

    -- 2. Obtener la tarifa
    SELECT TARIFA_APLICABLE INTO tarifa FROM TIPO_PERSONAL WHERE ID_TIPO_PERSONAL = p_id_tipo_personal;

    IF id_personal_encontrado IS NOT NULL THEN
        -- 3. Insertar en DETALLE_PERSONAL
        INSERT INTO DETALLE_PERSONAL (ID_EVENTO, ID_PERSONAL, ROL, HORAS_TRABAJADAS, TARIFA_HORA)
        VALUES (p_id_evento, id_personal_encontrado, p_rol, p_horas_trabajadas, tarifa);

        -- 4. Marcar la disponibilidad del personal como asignado
        INSERT INTO DISPONIBILIDAD_PERSONAL (ID_PERSONAL, ESTADO, EVENTO_ASIGNADO, FECHA_INICIO, FECHA_FIN)
        VALUES (id_personal_encontrado, 'ASIGNADO', p_id_evento, p_fecha_inicio, p_fecha_fin);

        SELECT 'Personal asignado exitosamente.' AS Mensaje;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: No hay personal disponible del tipo solicitado para la fecha.';
    END IF;
END //

-- RegistrarEvaluacionPostEvento
-- Registra el feedback y la puntuación tras la finalización de un evento
CREATE PROCEDURE RegistrarEvaluacionPostEvento (
    IN p_id_evento INT,
    IN p_aspectos_valorados TEXT,
    IN p_puntuacion DECIMAL(5,2),
    IN p_comentarios_cliente TEXT,
    IN p_incidencias_reportadas TEXT,
    IN p_lecciones_aprendidas TEXT,
    IN p_recomendaciones_futuras TEXT
)
BEGIN
    -- 1. Insertar la evaluación
    INSERT INTO EVALUACIONES_POSTEVENTO (
        ID_EVENTO, FECHA_EVALUACION, ASPECTOS_VALORADOS, PUNTUACION_TOTAL,
        COMENTARIOS_CLIENTE, INCIDENCIAS_REPORTADAS, LECCIONES_APRENDIDAS, RECOMENDACIONES_FUTURAS
    )
    VALUES (
        p_id_evento, NOW(), p_aspectos_valorados, p_puntuacion,
        p_comentarios_cliente, p_incidencias_reportadas, p_lecciones_aprendidas, p_recomendaciones_futuras
    );

    -- 2. Actualizar el estado del evento (opcional, si se tiene un estado "Evaluado")
    UPDATE EVENTO SET ESTADO_ACTUAL = CONCAT(ESTADO_ACTUAL, ' - Evaluado') WHERE ID_EVENTO = p_id_evento;

    SELECT 'Evaluación post-evento registrada.' AS Mensaje;
END //

DELIMITER ;