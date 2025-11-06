-- 1. ¿Cuáles son todos los servicios contratados para un evento específico?
SELECT
    E.TITULO_EVENTO,
    S.NOMBRE AS Nombre_Servicio,
    CS.CATEGORIA AS Categoria,
    DS.CANTIDAD,
    DS.PRECIO_UNITARIO,
    DS.SUBTOTAL,
    DS.OBSERVACIONES
FROM
    EVENTO E
        JOIN
    DETALLE_SERVICIOS DS ON E.ID_EVENTO = DS.ID_EVENTO
        JOIN
    SERVICIO S ON DS.ID_SERVICIO = S.ID_SERVICIO
        JOIN
    CATEGORIA_SERVICIO CS ON S.ID_CATEGORIA = CS.ID_CATEGORIA_SERVICIOS
WHERE
    E.ID_EVENTO = 1;

-- 2. ¿Qué eventos tienen más de 200 asistentes?

SELECT
    TITULO_EVENTO,
    FECHA_HORA_INICIO,
    NUMERO_ESTIMADO_ASISTENTES
FROM
    EVENTO
WHERE
    NUMERO_ESTIMADO_ASISTENTES >= 200
ORDER BY
    NUMERO_ESTIMADO_ASISTENTES DESC;

-- 3. ¿Cuáles son los recintos disponibles el 10 de mayo de 2024 con capacidad mínima de 100 personas?

SELECT
    R.ID_RECINTO,
    R.NOMBRE,
    C.CAPACIDAD,
    R.UBICACION
FROM
    RECINTO R
        JOIN
    CONFIGURACION C ON R.ID_CONFIGURACION = C.ID_CONFIGURACION
WHERE
    C.CAPACIDAD >= 100;

SELECT
    R.NOMBRE,
    C.TIPO_CONFIGURACION,
    C.CAPACIDAD
FROM
    RECINTO R
        JOIN
    CONFIGURACION C ON R.ID_CONFIGURACION = C.ID_CONFIGURACION
WHERE
    C.CAPACIDAD >= 100
  -- Excluir recintos que ya tienen una reserva o mantenimiento que se superpone con la fecha y hora de interés.
  AND R.ID_RECINTO NOT IN (
    SELECT
        ID_RECINTO
    FROM
        DETALLE_RECINTOS
    WHERE
      -- Verifica si la reserva existente se superpone con el 10/05/2026 09:00:00 - 17:00:00
        '2026-05-10 17:00:00' > FECHA_HORA_INICIO
      AND '2026-05-10 09:00:00' < FECHA_HORA_FIN
)
  AND R.ID_RECINTO NOT IN (
    SELECT
        ID_RECINTO
    FROM
        DISPONIBILIDAD_RECINTO
    WHERE
        ESTADO IN ('OCUPADO', 'MANTENIMIENTO')
      AND '2026-05-10 17:00:00' > FECHA_INICIO
      AND '2026-05-10 09:00:00' < FECHA_FIN
);

-- 4. ¿Qué eventos son conferencias o reuniones corporativas?

SELECT
    E.TITULO_EVENTO,
    TE.TIPO AS Tipo_Evento,
    C.NOMBRE AS Cliente_Nombre,
    C.TIPO_CLIENTE
FROM
    EVENTO E
        JOIN
    TIPO_EVENTO TE ON E.ID_TIPO_EVENTO = TE.ID_TIPO_EVENTO
        JOIN
    CLIENTE C ON E.ID_CLIENTE = C.ID_CLIENTE
WHERE
    TE.TIPO = 'Congreso'
   OR C.TIPO_CLIENTE = 'CORPORATIVO';

-- 5. ¿Cuáles son las cotizaciones emitidas en febrero de 2024?

SELECT
    ID_COTIZACION,
    FECHA_EMISION,
    VALIDEZ,
    C.NOMBRE AS Nombre_Cliente,
    TE.TIPO AS Tipo_Evento
FROM
    COTIZACION CT
        JOIN
    CLIENTE C ON CT.ID_CLIENTE = C.ID_CLIENTE
        JOIN
    TIPO_EVENTO TE ON CT.ID_TIPO_EVENTO = TE.ID_TIPO_EVENTO
WHERE
    CT.FECHA_EMISION BETWEEN '2024-02-01 00:00:00' AND '2024-02-29 23:59:59'
ORDER BY
    FECHA_EMISION ASC;

-- 6. ¿Qué equipamientos son de tipo Audiovisual, Mobiliario o Iluminación?

SELECT
    E.ID_EQUIPAMENTO,
    T.TIPO AS Tipo_de_Equipamento,
    T.DESCRIPCION AS Descripcion_Tipo,
    E.CANTIDAD_DISPONIBLE,
    E.ESTADO,
    A.UBICACION AS Ubicacion_Almacenamiento
FROM
    EQUIPAMENTO E
        JOIN
    TIPO_EQUIPAMENTO T ON E.ID_TIPO_EQUIPAMENTO = T.ID_TIPO_EQUIPAMENTO
        LEFT JOIN
    ALMACENAMIENTO A ON E.ID_ALMACENAMIENTO = A.ID_ALMACENAMIENTO
WHERE
    T.TIPO IN ('Audiovisual', 'Mobiliario', 'Iluminación')
ORDER BY
    T.TIPO, E.ID_EQUIPAMENTO;

-- 7. ¿Cuáles son los servicios con descripciones que contienen las palabras "premium" o "exclusivo"?

SELECT
    CS.CATEGORIA,
    CS.DESCRIPCION AS Descripcion_Categoria,
    S.NOMBRE AS Nombre_Servicio,
    S.UNIDAD_FACTURACION
FROM
    CATEGORIA_SERVICIO CS
        JOIN
    SERVICIO S ON CS.ID_CATEGORIA_SERVICIOS = S.ID_CATEGORIA
WHERE
   -- Búsqueda por la palabra "premium" o "exclusivo" en la descripción
    CS.DESCRIPCION LIKE '%premium%'
   OR CS.DESCRIPCION LIKE '%exclusivo%';

-- 8. ¿Qué eventos pasados no tienen evaluación post-evento?

SELECT
    ID_EVENTO,
    TITULO_EVENTO,
    FECHA_HORA_FIN,
    ESTADO_ACTUAL
FROM
    EVENTO
WHERE
    FECHA_HORA_FIN < NOW()
  AND ID_EVENTO NOT IN (
    SELECT
        ID_EVENTO
    FROM
        EVALUACIONES_POSTEVENTO
)
ORDER BY
    FECHA_HORA_FIN DESC;

-- 9. ¿Cuáles son los recintos ordenados por capacidad descendente y tarifa ascendente?

SELECT
    R.NOMBRE,
    C.CAPACIDAD,
    R.UBICACION,
    C.TIPO_CONFIGURACION
FROM
    RECINTO R
        JOIN
    CONFIGURACION C ON R.ID_CONFIGURACION = C.ID_CONFIGURACION
ORDER BY
    C.CAPACIDAD DESC;

-- 10. ¿Cuáles son los ingresos totales por tipo de evento y mes?

SELECT
    TE.TIPO AS Tipo_Evento,
    YEAR(E.FECHA_HORA_INICIO) AS Año,
    MONTHNAME(E.FECHA_HORA_INICIO) AS Mes,
    SUM(DC.SUBTOTAL) AS Ingresos_Totales
FROM
    DETALLE_COSTO DC
        JOIN
    EVENTO E ON DC.ID_EVENTO = E.ID_EVENTO
        JOIN
    TIPO_EVENTO TE ON E.ID_TIPO_EVENTO = TE.ID_TIPO_EVENTO
GROUP BY
    TE.TIPO, Año, Mes
ORDER BY
    Año ASC,Ingresos_Totales DESC;