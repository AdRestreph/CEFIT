DELIMITER //

-- FN_VerificarDisponibilidadPeriodo
-- Verifica si un recinto está libre para un periodo dado (NULL = disponible)
CREATE FUNCTION FN_VerificarDisponibilidadPeriodo (
    p_id_recinto INT,
    p_fecha_inicio DATETIME,
    p_fecha_fin DATETIME
)
    RETURNS BOOLEAN
    READS SQL DATA
BEGIN
    DECLARE conflicto INT DEFAULT 0;

    -- Buscar conflictos en DETALLE_RECINTOS (reservas confirmadas)
    SELECT COUNT(*) INTO conflicto
    FROM DETALLE_RECINTOS DR
    WHERE DR.ID_RECINTO = p_id_recinto
      AND p_fecha_fin > DR.FECHA_HORA_INICIO
      AND p_fecha_inicio < DR.FECHA_HORA_FIN;

    -- Buscar conflictos en DISPONIBILIDAD_RECINTO (mantenimiento o eventos antiguos)
    IF conflicto = 0 THEN
        SELECT COUNT(*) INTO conflicto
        FROM DISPONIBILIDAD_RECINTO DR
        WHERE DR.ID_RECINTO = p_id_recinto
          AND DR.ESTADO IN ('OCUPADO', 'MANTENIMIENTO')
          AND p_fecha_fin > DR.FECHA_INICIO
          AND p_fecha_inicio < DR.FECHA_FIN;
    END IF;

    RETURN conflicto = 0;
END //

-- FN_ObtenerPersonalDisponible
-- Verifica si el personal de un tipo específico está disponible en una fecha
CREATE FUNCTION FN_ObtenerPersonalDisponible (
    p_id_tipo_personal INT,
    p_fecha DATETIME
)
    RETURNS INT
    READS SQL DATA
BEGIN
    DECLARE personal_disponible INT;

    SELECT ID_PERSONAL INTO personal_disponible
    FROM PERSONAL P
    WHERE P.ID_TIPO_PERSONAL = p_id_tipo_personal
      AND P.ID_PERSONAL NOT IN (
        SELECT ID_PERSONAL FROM DISPONIBILIDAD_PERSONAL DP
        WHERE DP.ESTADO = 'ASIGNADO'
          AND p_fecha BETWEEN DP.FECHA_INICIO AND DP.FECHA_FIN
    )
    LIMIT 1; -- Devuelve el ID del primer personal disponible encontrado

    RETURN personal_disponible;
END //

-- FN_CalcularPresupuestoEvento
-- Calcula el presupuesto total sumando todos los costos asociados
CREATE FUNCTION FN_CalcularPresupuestoEvento (
    p_id_evento INT
)
    RETURNS DECIMAL(14,2)
    READS SQL DATA
BEGIN
    DECLARE total_presupuesto DECIMAL(14,2);

    SELECT COALESCE(SUM(SUBTOTAL), 0) INTO total_presupuesto
    FROM DETALLE_COSTO
    WHERE ID_EVENTO = p_id_evento;

    RETURN total_presupuesto;
END //

-- FN_CalcularCapacidadConfiguracion
-- Obtiene la capacidad específica de un recinto según la configuración
CREATE FUNCTION FN_CalcularCapacidadConfiguracion (
    p_id_configuracion INT
)
    RETURNS INT
    READS SQL DATA
BEGIN
    DECLARE capacidad INT;

    SELECT CAPACIDAD INTO capacidad
    FROM CONFIGURACION
    WHERE ID_CONFIGURACION = p_id_configuracion;

    RETURN capacidad;
END //

-- FN_EstimarOcupacionAnual (Simplificada)
-- Estima el porcentaje de ocupación anual de un recinto
CREATE FUNCTION FN_EstimarOcupacionAnual (
    p_id_recinto INT,
    p_anio INT
)
    RETURNS DECIMAL(5,2)
    READS SQL DATA
BEGIN
    DECLARE horas_ocupadas DECIMAL(10,2);
    DECLARE total_horas_anio DECIMAL(10,2) DEFAULT 8760.00; -- Horas en un año no bisiesto

    SELECT COALESCE(SUM(TIMESTAMPDIFF(HOUR, FECHA_HORA_INICIO, FECHA_HORA_FIN)), 0) INTO horas_ocupadas
    FROM DETALLE_RECINTOS
    WHERE ID_RECINTO = p_id_recinto
      AND YEAR(FECHA_HORA_INICIO) = p_anio;

    RETURN (horas_ocupadas / total_horas_anio) * 100.00;
END //

DELIMITER ;

