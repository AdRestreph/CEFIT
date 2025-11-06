INSERT INTO CONFIGURACION (TIPO_CONFIGURACION, CAPACIDAD, FRANJA_HORARIA) VALUES
    ('Teatro', 250, '08:00:00'),
    ('Escuela', 120, '08:00:00'),
    ('Banquete', 180, '18:00:00');

INSERT INTO TIPO_RECINTO (TIPO) VALUES
    ('Salón'),
    ('Auditorio'),
    ('Sala de Reuniones');

INSERT INTO RECINTO (NOMBRE, ID_TIPO_RECINTO, UBICACION, DIMENSIONES, ID_CONFIGURACION, CARACTERISTICAS, TARIFA) VALUES
    ('Salón Estelar', 1, 'Planta Alta, Ala Oeste', '20x15m', 1, 'Proyector 4K, Sonido Envolvente', 'HORA'),
    ('Auditorio Central', 2, 'Planta Baja', '30x25m', 2, 'Escenario Fijo, Cabina de Control', 'DIA'),
    ('Sala Ejecutiva 1', 3, 'Primer Piso', '8x6m', 2, 'Videoconferencia, Pizarra Digital', 'HORA');

INSERT INTO DISPONIBILIDAD_RECINTO (ID_RECINTO, ESTADO, FECHA_INICIO, FECHA_FIN) VALUES
    (1, 'OCUPADO', '2025-12-10 10:00:00', '2025-12-10 14:00:00'),
    (2, 'MANTENIMIENTO', '2025-11-01 08:00:00', '2025-11-03 18:00:00');

INSERT INTO TIPO_EQUIPAMENTO (TIPO, DESCRIPCION, VALOR_REPOSICION, VIDA_UTIL) VALUES
    ('Audiovisual', 'Proyectores, pantallas, micrófonos', 5500.00, '5 años'),
    ('Mobiliario', 'Sillas, mesas, atriles', 1200.00, '10 años'),
    ('Decoración', 'Telas, centros de mesa, iluminación', 800.00, '2 años');

INSERT INTO ALMACENAMIENTO (UBICACION, ESPECIFICACION) VALUES
    ('Depósito Principal A', 'Climatizado para electrónica'),
    ('Sala de Utilería 1', 'Estanterías resistentes');

INSERT INTO EQUIPAMENTO (ID_TIPO_EQUIPAMENTO, CANTIDAD_DISPONIBLE, ESTADO, ID_ALMACENAMIENTO, MANTENIMIENTO_REQUERIDO) VALUES
    (1, 5, 'DISPONIBLE', 1, 'NO'),
    (2, 150, 'EN USO', 2, 'NO'),
    (1, 2, 'MANTENIMIENTO', 1, 'SI');

INSERT INTO CATEGORIA_SERVICIO (CATEGORIA, DESCRIPCION, PRECIO_BASE) VALUES
    ('Catering', 'Alimentos y bebidas, menús especiales', 25.00),
    ('Técnico', 'Soporte de audio, video e iluminación', 50.00),
    ('Seguridad', 'Vigilancia y control de acceso', 35.00);

INSERT INTO PROVEEDOR (NOMBRE, TIPO) VALUES
    ('Cocina Central', 'INTERNO'),
    ('Tech Solutions S.A.', 'EXTERNO'),
    ('Vigilancia Total', 'EXTERNO');

INSERT INTO SERVICIO (NOMBRE, ID_CATEGORIA, ID_PROVEEDOR, CONDICIONES_CONTRATACION, UNIDAD_FACTURACION, PLAZO_MIN_SOLICITUD) VALUES
    ('Coffee Break Estándar', 1, 1, 'Mínimo 20 personas', 'PERSONA', 3),
    ('Asistencia Técnica AV', 2, 2, 'Horario 8am a 6pm', 'HORA', 7),
    ('Servicio de Vigilancia', 3, 3, 'Mínimo 4 horas por evento', 'HORA', 10);

INSERT INTO CLIENTE (TIPO_CLIENTE, NOMBRE, TIPO_DOCUMENTO, NUM_DOCUMENTO, DIRECCION, TELEFONO, CORREO, CLASIFICACION_VOLUMEN, CONDICIONES_ESPECIALES) VALUES
    ('CORPORATIVO', 'Empresa Global Corp', 'NIT', '900123456-7', 'Av. Principal 123', '573001112233', 'globalcorp@mail.com', 'ALTA', 'Descuento 10% en recintos'),
    ('AGENCIA', 'Eventos Elite S.A.S.', 'NIT', '800987654-2', 'Calle Falsa 456', '573004445566', 'eventoselite@mail.com', 'MEDIA', 'Pago a 60 días'),
    ('PARTICULAR', 'Sofía Pérez', 'CEDULA DE CIUDADANIA', '1020304050', 'Carrera 789', '573007778899', 'sofia.perez@personal.com', 'BAJA', 'Ninguna');

INSERT INTO PERSONA_CONTACTO (NOMBRE_COMPLETO, TELEFONO, DIRECCION, CORREO) VALUES
    ('Ana López', '573012223344', 'Oficina 123', 'ana.lopez@globalcorp.com'),
    ('Carlos Gómez', '573015556677', 'Oficina Eventos', 'carlos.gomez@elite.com'),
    ('Juan Rodríguez', '573018889900', 'Casa Sofía', 'juan.rodriguez@personal.com');

INSERT INTO CLIENTE_CONTACTO (ID_CLIENTE, ID_PERSONA_CONTACTO) VALUES
    (1, 1),
    (2, 2),
    (3, 3);

INSERT INTO TIPO_PERSONAL (TIPO, RESPONSABILIDADES_ESPECIFICAS, TARIFA_APLICABLE) VALUES
    ('Coordinador de Eventos', 'Supervisión general, gestión de proveedores', 85.00),
    ('Técnico AV', 'Montaje y operación de equipos audiovisuales', 60.00),
    ('Camarero', 'Servicio de alimentos y bebidas', 35.00),
    ('Seguridad', 'Vigilancia y control de acceso', 40.00);

INSERT INTO PERSONAL (NOMBRE, APELLIDO, ID_TIPO_PERSONAL) VALUES
    ('Daniela', 'Vargas', 1),
    ('Ricardo', 'Soto', 2),
    ('Elena', 'Morales', 3),
    ('Pedro', 'Jiménez', 4);

INSERT INTO TIPO_EVENTO (TIPO, DESCRIPCION) VALUES
    ('Congreso', 'Evento académico o profesional con ponencias'),
    ('Boda', 'Ceremonia y recepción social'),
    ('Feria', 'Exposición comercial o sectorial');

INSERT INTO EVENTO (TITULO_EVENTO, ID_TIPO_EVENTO, ID_CLIENTE, FECHA_HORA_INICIO, FECHA_HORA_FIN, MONTAJE_SOLICITADO, NUMERO_ESTIMADO_ASISTENTES, PRESUPUESTO_APROBADO, ESTADO_ACTUAL, ID_EMPLEADO_RESPONSABLE) VALUES
    ('Congreso de Tecnología 2026', 1, 1, '2026-03-15 09:00:00', '2026-03-17 18:00:00', 'Escuela y Teatro', 200, 25000.00, 'En planificación', 1),
    ('Boda Sofía y Juan', 2, 3, '2026-05-20 19:00:00', '2026-05-21 03:00:00', 'Banquete y Pista', 150, 18000.00, 'Pendiente confirmación', 1);

INSERT INTO DETALLE_RECINTOS (ID_EVENTO, ID_RECINTO, ID_CONFIGURACION, FECHA_HORA_INICIO, FECHA_HORA_FIN, PRECIO_HORA, HORAS_RESERVADAS, MONTAJE_ESPECIFICO, OBSERVACIONES) VALUES
    (1, 1, 2, '2026-03-15 09:00:00', '2026-03-15 13:00:00', 150.00, 4.00, 'Configuración Escuela con mesas individuales', 'Requerido acceso 1 hora antes'),
    (1, 1, 1, '2026-03-15 14:00:00', '2026-03-15 18:00:00', 150.00, 4.00, 'Configuración Teatro con atril', 'Probar proyección antes de iniciar');

INSERT INTO DETALLE_SERVICIOS (ID_EVENTO, ID_SERVICIO, CANTIDAD, PRECIO_UNITARIO, OBSERVACIONES) VALUES
    (1, 1, 200, 25.00, '2 Coffee breaks por día, para 200 personas'),
    (1, 2, 16, 60.00, '8 horas por día de asistencia técnica');

INSERT INTO DISPONIBILIDAD_PERSONAL (ID_PERSONAL, ESTADO, EVENTO_ASIGNADO, FECHA_INICIO, FECHA_FIN) VALUES
    (1, 'ASIGNADO', 1, '2026-03-14 08:00:00', '2026-03-18 20:00:00'),
    (2, 'DISPONIBLE', NULL, '2025-10-31 08:00:00', '2026-10-31 18:00:00'),
    (3, 'VACACIONES', NULL, '2025-12-01 00:00:00', '2025-12-15 23:59:59');

INSERT INTO CLIENTE_EVENTOS_ANTERIORES (ID_CLIENTE, ID_EVENTO) VALUES
    (1, 1);

INSERT INTO DESCUENTO (NOMBRE, VALOR, TIPO) VALUES
    ('Fidelidad Corporativa', 10.00, 'PORCENTAJE'),
    ('Promoción Boda', 500.00, 'MONTO');

INSERT INTO DETALLE_COSTO (ID_EVENTO, TIPO_COSTO, ID_RECINTO, ID_SERVICIO, ID_EQUIPAMENTO, ID_PERSONAL, CONCEPTO, CANTIDAD, UNIDAD_MEDIDA, PRECIO_UNITARIO) VALUES
    (1, 'RECINTO', 1, NULL, NULL, NULL, 'Alquiler Salón Estelar Día 1', 8.00, 'HORA', 150.00),
    (1, 'SERVICIO', NULL, 1, NULL, NULL, 'Catering Coffee Break (200 pax)', 200.00, 'PERSONA', 25.00),
    (1, 'EQUIPAMIENTO', NULL, NULL, 1, NULL, 'Alquiler de Proyector 4K', 3.00, 'DIA', 100.00),
    (1, 'PERSONAL', NULL, NULL, NULL, 1, 'Coordinador de Eventos (Día 1)', 8.00, 'HORA', 85.00),
    (1, 'OTROS', NULL, NULL, NULL, NULL, 'Impresión de Materiales', 1.00, 'EVENTO', 450.00);

INSERT INTO DETALLE_PERSONAL (ID_EVENTO, ID_PERSONAL, ROL, HORAS_TRABAJADAS, TARIFA_HORA) VALUES
    (1, 1, 'Coordinador General', 24.00, 85.00),
    (1, 2, 'Asistencia Técnica', 16.00, 60.00);

INSERT INTO COTIZACION (ID_COTIZACION, FECHA_EMISION, VALIDEZ, ID_CLIENTE, ID_TIPO_EVENTO, ID_RECINTO, ID_DETALLE_RECINTOS, ID_DETALLE_SERVICIOS, ID_DETALLE_COSTO, CONDICION_PAGO, REQUISITO_CONFIRMACION, ID_DESCUENTO, OBSERVACIONES) VALUES
    (1000, '2025-10-31 15:00:00', 'VALIDO', 1, 1, 1, 1, 1, 1, '50% anticipo, 50% post-evento', 'Firma de contrato en 7 días', 1, 'Incluye setup completo.');

INSERT INTO ACTIVIDADES (NOMBRE, DESCRIPCION) VALUES
    ('Registro de Asistentes', 'Proceso de check-in y entrega de material'),
    ('Sesión de Apertura', 'Palabras de bienvenida y keynote speaker'),
    ('Almuerzo Buffet', 'Servicio de catering en área designada');

INSERT INTO CRONOGRAMA_ACTIVIDADES (FECHA_INICIO, FECHA_FIN, ID_ACTIVIDADES) VALUES
    ('2026-03-15 08:00:00', '2026-03-15 09:00:00', 1),
    ('2026-03-15 09:00:00', '2026-03-15 10:00:00', 2),
    ('2026-03-15 13:00:00', '2026-03-15 14:00:00', 3);

INSERT INTO MENU (HORARIO, CATEGORIA, DESCRIPCION, COSTO_BASE) VALUES
    ('Mañana', 'DESAYUNO', 'Café, jugos, bollería y fruta', 8.00),
    ('Mediodía', 'ALMUERZO', 'Buffet ejecutivo: 3 platos, bebida', 20.00),
    ('Noche', 'CENA', 'Menú de gala: 4 tiempos', 45.00);

INSERT INTO CATERING (ID_PERSONAL_ENCARGADO, ID_EVENTO) VALUES
    (3, 1);

INSERT INTO CATERING_MENU (ID_CATERING, ID_MENU) VALUES
    (1, 1),
    (1, 2);

INSERT INTO EVALUACIONES_POSTEVENTO (ID_EVENTO, FECHA_EVALUACION, ASPECTOS_VALORADOS, PUNTUACION_TOTAL, COMENTARIOS_CLIENTE, INCIDENCIAS_REPORTADAS, LECCIONES_APRENDIDAS, RECOMENDACIONES_FUTURAS) VALUES
    (1, '2026-03-20 10:00:00', 'Recinto, Servicios AV, Coordinación', 9.20, 'Excelente atención y logística.', 'Un micrófono falló brevemente.', 'Revisar equipos AV antes de cada sesión.', 'Más opciones de menú vegetariano.');

INSERT INTO FIRMAS_AUTORIZADAS (NOMBRE, APELLIDO, FIRMA_DIGITAL) VALUES
    ('Gerente', 'General', 0x476572656E74654669726D61);

INSERT INTO CRONOGRAMA_PAGO (FECHA_VENCIMIENTO, ID_DETALLE_COSTO) VALUES
    ('2026-02-15', 1),
    ('2026-03-25', 2);

INSERT INTO CONTRATO (FECHA_FIRMA, ID_CLIENTE, ID_EVENTO, CONDICIONES_GENERALES, ID_DETALLE_SERVICIOS, ID_CRONOGRAMA_PAGO, POLITICA_CANCELACION, PENALIZACION, CLAUSULAS_ESPECIALES, ANEXOS, ID_FIRMAS_AUTORIZADAS) VALUES
    ('2025-11-15 11:00:00', 1, 1, 'Términos estándar de servicio', 1, 1, 'Penalización 50% si cancela 30 días antes', '10% del total si hay cambios de última hora', 'Acceso de carga por puerta trasera', 0x436F6E747261746F416E65786F, 1);