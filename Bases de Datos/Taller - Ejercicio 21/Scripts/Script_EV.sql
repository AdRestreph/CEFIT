DELIMITER //

-- EVT_VerificarPreparativosEventos
-- Se ejecuta diariamente a la medianoche. Verifica eventos en los próximos 7 días para enviar alertas.
CREATE EVENT EVT_VerificarPreparativosEventos
ON SCHEDULE EVERY 1 DAY
STARTS TIMESTAMP(CURDATE() + INTERVAL 1 DAY)
DO
BEGIN
    INSERT INTO ACTIVIDADES (NOMBRE, DESCRIPCION, FECHA_CREACION)
    SELECT
        CONCAT('Revisar Preparativos para ', TITULO_EVENTO),
        CONCAT('El evento ID ', ID_EVENTO, ' está a menos de 7 días. Verificar check-list.'),
        NOW()
    FROM
        EVENTO
    WHERE
        FECHA_HORA_INICIO BETWEEN NOW() AND DATE_ADD(NOW(), INTERVAL 7 DAY)
        AND ESTADO_ACTUAL IN ('Confirmado', 'En Planificación'); -- Solo eventos relevantes

END //

-- EVT_GenerarReportesPostEvento
-- Se ejecuta el primer día de cada mes para generar reportes del mes anterior.
CREATE EVENT EVT_GenerarReportesPostEvento
ON SCHEDULE EVERY 1 MONTH
STARTS DATE_ADD(LAST_DAY(CURDATE() - INTERVAL 1 MONTH), INTERVAL 1 DAY)
DO
BEGIN
    DECLARE ultimo_mes DATE;
    SET ultimo_mes = DATE_SUB(CURDATE(), INTERVAL 1 MONTH);

    -- Simulación de la generación de un reporte sumario del mes
    INSERT INTO REPORTES_AUDITORIA (NOMBRE_REPORTE, FECHA_GENERACION, CONTENIDO_RESUMEN)
    SELECT
        CONCAT('Reporte Post-Evento ', DATE_FORMAT(ultimo_mes, '%Y-%m')),
        NOW(),
        CONCAT('Eventos evaluados: ', COUNT(EPE.ID_EVALUACION))
    FROM
        EVALUACIONES_POSTEVENTO EPE
    WHERE
        MONTH(EPE.FECHA_EVALUACION) = MONTH(ultimo_mes)
        AND YEAR(EPE.FECHA_EVALUACION) = YEAR(ultimo_mes);
END //

-- EVT_ActualizarDisponibilidadTemporal
-- Se ejecuta cada 4 horas. Libera recintos cuya reserva ya expiró.
CREATE EVENT EVT_ActualizarDisponibilidadTemporal
ON SCHEDULE EVERY 4 HOUR
DO
BEGIN
    -- Eliminar los registros de DISPONIBILIDAD_RECINTO que estaban marcados como 'OCUPADO'
    -- y cuya fecha de finalización ya pasó.
    DELETE FROM DISPONIBILIDAD_RECINTO
    WHERE ESTADO = 'OCUPADO'
      AND FECHA_FIN < NOW();
END //

-- EVT_ControlarMantenimientoEquipos
-- Se ejecuta el primer día de cada mes. Programa mantenimiento preventivo.
CREATE EVENT EVT_ControlarMantenimientoEquipos
ON SCHEDULE EVERY 1 MONTH
STARTS DATE_ADD(LAST_DAY(CURDATE()), INTERVAL 1 DAY)
DO
BEGIN

    UPDATE EQUIPAMENTO
    SET ESTADO = 'MANTENIMIENTO'
    WHERE VIDA_UTIL_REMANENTE < 100 -- Ejemplo: menos de 100 horas/ciclos restantes
      AND ESTADO = 'DISPONIBLE'; -- Solo si están disponibles para entrar a mantenimiento
END //

-- EVT_AnalizarRendimientoServicios
-- Se ejecuta trimestralmente (cada 3 meses).
CREATE EVENT EVT_AnalizarRendimientoServicios
ON SCHEDULE EVERY 3 MONTH
STARTS DATE_ADD(CURDATE(), INTERVAL 3 MONTH) -- Comienza en 3 meses, luego repite
DO
BEGIN
    INSERT INTO REPORTES_AUDITORIA (NOMBRE_REPORTE, FECHA_GENERACION, CONTENIDO_RESUMEN)
    VALUES (
        'Análisis Trimestral Rendimiento Servicios',
        NOW(),
        'Servicios con Puntuación media menor a 3.0 en las últimas 10 evaluaciones.'
    );
END //

DELIMITER ;