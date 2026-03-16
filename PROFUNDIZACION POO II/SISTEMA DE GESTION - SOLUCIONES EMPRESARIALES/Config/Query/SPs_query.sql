USE SITEMA_DE_GESTION_SOLUCIONES_EMPRESARIALES;
-- 1. INSERTAR CLIENTE
CREATE PROCEDURE sp_InsertCliente(
    IN p_codigo                 VARCHAR(20),
    IN p_tipo                   VARCHAR(20),
    IN p_razon_social           VARCHAR(150),
    IN p_sector_actividad       VARCHAR(100),
    IN p_ruc                    VARCHAR(20),
    IN p_direccion              VARCHAR(200),
    IN p_telefono               VARCHAR(30),
    IN p_sitio_web              VARCHAR(100),
    IN p_contacto_principal     VARCHAR(100),
    IN p_cargo_contacto         VARCHAR(100),
    IN p_correo_electronico     VARCHAR(100),
    IN p_telefono_directo       VARCHAR(30),
    IN p_fecha_primera_relacion DATE,
    IN p_origen_contacto        VARCHAR(80),
    IN p_clasificacion_potencial VARCHAR(20)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;

    START TRANSACTION;

    INSERT INTO clientes (
        codigo, tipo, razon_social, sector_actividad, ruc,
        direccion, telefono, sitio_web, contacto_principal,
        cargo_contacto, correo_electronico, telefono_directo,
        fecha_primera_relacion, origen_contacto, clasificacion_potencial
    ) VALUES (
                 p_codigo, p_tipo, p_razon_social, p_sector_actividad, p_ruc,
                 p_direccion, p_telefono, p_sitio_web, p_contacto_principal,
                 p_cargo_contacto, p_correo_electronico, p_telefono_directo,
                 p_fecha_primera_relacion, p_origen_contacto, p_clasificacion_potencial
             );

    COMMIT;

    SELECT p_codigo AS codigo, 'Cliente insertado correctamente' AS mensaje;
END //


-- 2. ACTUALIZAR CLIENTE
CREATE PROCEDURE sp_UpdateCliente(
    IN p_codigo                 VARCHAR(20),
    IN p_tipo                   VARCHAR(20),
    IN p_razon_social           VARCHAR(150),
    IN p_sector_actividad       VARCHAR(100),
    IN p_ruc                    VARCHAR(20),
    IN p_direccion              VARCHAR(200),
    IN p_telefono               VARCHAR(30),
    IN p_sitio_web              VARCHAR(100),
    IN p_contacto_principal     VARCHAR(100),
    IN p_cargo_contacto         VARCHAR(100),
    IN p_correo_electronico     VARCHAR(100),
    IN p_telefono_directo       VARCHAR(30),
    IN p_clasificacion_potencial VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM clientes WHERE codigo = p_codigo;

    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El cliente no existe';
    END IF;

    UPDATE clientes
    SET tipo                    = p_tipo,
        razon_social            = p_razon_social,
        sector_actividad        = p_sector_actividad,
        ruc                     = p_ruc,
        direccion               = p_direccion,
        telefono                = p_telefono,
        sitio_web               = p_sitio_web,
        contacto_principal      = p_contacto_principal,
        cargo_contacto          = p_cargo_contacto,
        correo_electronico      = p_correo_electronico,
        telefono_directo        = p_telefono_directo,
        clasificacion_potencial = p_clasificacion_potencial
    WHERE codigo = p_codigo;

    COMMIT;

    SELECT 'Cliente actualizado correctamente' AS mensaje;
END //


-- 3. ELIMINAR CLIENTE
CREATE PROCEDURE sp_DeleteCliente(
    IN p_codigo VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM clientes WHERE codigo = p_codigo;

    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El cliente no existe';
    END IF;

    -- Verificar si el cliente tiene proyectos asociados
    SELECT COUNT(*) INTO v_count FROM proyectos WHERE cliente_codigo = p_codigo;

    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No se puede eliminar: el cliente tiene proyectos asociados';
    END IF;

    -- Verificar si el cliente tiene facturas asociadas
    SELECT COUNT(*) INTO v_count FROM facturas WHERE cliente_codigo = p_codigo;

    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No se puede eliminar: el cliente tiene facturas asociadas';
    END IF;

    DELETE FROM clientes WHERE codigo = p_codigo;

    COMMIT;

    SELECT 'Cliente eliminado correctamente' AS mensaje;
END //


-- 4. OBTENER CLIENTE POR CÓDIGO
CREATE PROCEDURE sp_GetCliente(
    IN p_codigo VARCHAR(20)
)
BEGIN
    SELECT * FROM clientes WHERE codigo = p_codigo;
END //


-- 5. OBTENER TODOS LOS CLIENTES
CREATE PROCEDURE sp_GetAllClientes()
BEGIN
    SELECT codigo, tipo, razon_social, sector_actividad,
           contacto_principal, correo_electronico, clasificacion_potencial
    FROM clientes
    ORDER BY razon_social;
END //


-- 6. BUSCAR CLIENTES POR NOMBRE O CONTACTO
CREATE PROCEDURE sp_SearchClientes(
    IN p_termino VARCHAR(100)
)
BEGIN
    SELECT codigo, tipo, razon_social, sector_actividad,
           contacto_principal, correo_electronico, clasificacion_potencial
    FROM clientes
    WHERE razon_social       LIKE CONCAT('%', p_termino, '%')
       OR contacto_principal LIKE CONCAT('%', p_termino, '%')
       OR ruc                LIKE CONCAT('%', p_termino, '%')
    ORDER BY razon_social;
END //


-- ============================================================
-- CONSULTORES
-- (adapta sp_InsertEmployee, sp_UpdateEmployee, sp_DeleteEmployee,
--  sp_GetEmployee, sp_GetAllEmployees, sp_SearchEmployees)
-- ============================================================

-- 1. INSERTAR CONSULTOR
CREATE PROCEDURE sp_InsertConsultor(
    IN p_codigo_empleado     VARCHAR(20),
    IN p_nombres             VARCHAR(100),
    IN p_apellidos           VARCHAR(100),
    IN p_documento_identidad VARCHAR(20),
    IN p_formacion_academica VARCHAR(200),
    IN p_certificaciones     TEXT,
    IN p_especialidades      TEXT,
    IN p_anios_experiencia   SMALLINT,
    IN p_nivel               VARCHAR(20),
    IN p_tarifa_horaria      NUMERIC(10,2),
    IN p_idiomas             VARCHAR(150),
    IN p_disponibilidad      VARCHAR(80)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;

    START TRANSACTION;

    INSERT INTO consultores (
        codigo_empleado, nombres, apellidos, documento_identidad,
        formacion_academica, certificaciones, especialidades,
        anios_experiencia, nivel, tarifa_horaria, idiomas, disponibilidad
    ) VALUES (
                 p_codigo_empleado, p_nombres, p_apellidos, p_documento_identidad,
                 p_formacion_academica, p_certificaciones, p_especialidades,
                 p_anios_experiencia, p_nivel, p_tarifa_horaria, p_idiomas, p_disponibilidad
             );

    COMMIT;

    SELECT p_codigo_empleado AS codigo_empleado, 'Consultor insertado correctamente' AS mensaje;
END //


-- 2. ACTUALIZAR CONSULTOR
CREATE PROCEDURE sp_UpdateConsultor(
    IN p_codigo_empleado     VARCHAR(20),
    IN p_nombres             VARCHAR(100),
    IN p_apellidos           VARCHAR(100),
    IN p_formacion_academica VARCHAR(200),
    IN p_certificaciones     TEXT,
    IN p_especialidades      TEXT,
    IN p_anios_experiencia   SMALLINT,
    IN p_nivel               VARCHAR(20),
    IN p_tarifa_horaria      NUMERIC(10,2),
    IN p_idiomas             VARCHAR(150),
    IN p_disponibilidad      VARCHAR(80)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM consultores WHERE codigo_empleado = p_codigo_empleado;

    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El consultor no existe';
    END IF;

    UPDATE consultores
    SET nombres             = p_nombres,
        apellidos           = p_apellidos,
        formacion_academica = p_formacion_academica,
        certificaciones     = p_certificaciones,
        especialidades      = p_especialidades,
        anios_experiencia   = p_anios_experiencia,
        nivel               = p_nivel,
        tarifa_horaria      = p_tarifa_horaria,
        idiomas             = p_idiomas,
        disponibilidad      = p_disponibilidad
    WHERE codigo_empleado = p_codigo_empleado;

    COMMIT;

    SELECT 'Consultor actualizado correctamente' AS mensaje;
END //


-- 3. ELIMINAR CONSULTOR
CREATE PROCEDURE sp_DeleteConsultor(
    IN p_codigo_empleado VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM consultores WHERE codigo_empleado = p_codigo_empleado;

    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El consultor no existe';
    END IF;

    -- Verificar si el consultor tiene proyectos asignados
    SELECT COUNT(*) INTO v_count FROM proyecto_consultores WHERE consultor_codigo = p_codigo_empleado;

    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No se puede eliminar: el consultor tiene proyectos asignados';
    END IF;

    -- Verificar si el consultor tiene horas registradas
    SELECT COUNT(*) INTO v_count FROM horas_trabajadas WHERE consultor_codigo = p_codigo_empleado;

    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No se puede eliminar: el consultor tiene horas registradas';
    END IF;

    DELETE FROM consultores WHERE codigo_empleado = p_codigo_empleado;

    COMMIT;

    SELECT 'Consultor eliminado correctamente' AS mensaje;
END //


-- 4. OBTENER CONSULTOR POR CÓDIGO
CREATE PROCEDURE sp_GetConsultor(
    IN p_codigo_empleado VARCHAR(20)
)
BEGIN
    SELECT * FROM consultores WHERE codigo_empleado = p_codigo_empleado;
END //


-- 5. OBTENER TODOS LOS CONSULTORES
CREATE PROCEDURE sp_GetAllConsultores()
BEGIN
    SELECT codigo_empleado, nombres, apellidos, nivel,
           especialidades, tarifa_horaria, disponibilidad
    FROM consultores
    ORDER BY apellidos, nombres;
END //


-- 6. BUSCAR CONSULTORES POR NOMBRE O ESPECIALIDAD
CREATE PROCEDURE sp_SearchConsultores(
    IN p_termino VARCHAR(100)
)
BEGIN
    SELECT codigo_empleado, nombres, apellidos, nivel,
           especialidades, tarifa_horaria, disponibilidad
    FROM consultores
    WHERE nombres        LIKE CONCAT('%', p_termino, '%')
       OR apellidos      LIKE CONCAT('%', p_termino, '%')
       OR especialidades LIKE CONCAT('%', p_termino, '%')
    ORDER BY apellidos, nombres;
END //


-- ============================================================
-- SERVICIOS
-- (adapta sp_InsertProduct, sp_UpdateProduct, sp_DeleteProduct,
--  sp_GetProduct, sp_GetAllProducts, sp_SearchProducts)
-- ============================================================

-- 1. INSERTAR SERVICIO
CREATE PROCEDURE sp_InsertServicio(
    IN p_codigo                VARCHAR(20),
    IN p_nombre_comercial      VARCHAR(150),
    IN p_categoria             VARCHAR(80),
    IN p_descripcion           TEXT,
    IN p_entregables_tipicos   TEXT,
    IN p_duracion_estimada     VARCHAR(60),
    IN p_metodologia           VARCHAR(150),
    IN p_beneficios_cliente    TEXT,
    IN p_equipo_minimo         VARCHAR(100),
    IN p_tarifario_referencial NUMERIC(12,2),
    IN p_casos_exito           TEXT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;

    START TRANSACTION;

    INSERT INTO servicios (
        codigo, nombre_comercial, categoria, descripcion,
        entregables_tipicos, duracion_estimada, metodologia,
        beneficios_cliente, equipo_minimo, tarifario_referencial, casos_exito
    ) VALUES (
                 p_codigo, p_nombre_comercial, p_categoria, p_descripcion,
                 p_entregables_tipicos, p_duracion_estimada, p_metodologia,
                 p_beneficios_cliente, p_equipo_minimo, p_tarifario_referencial, p_casos_exito
             );

    COMMIT;

    SELECT p_codigo AS codigo, 'Servicio insertado correctamente' AS mensaje;
END //


-- 2. ACTUALIZAR SERVICIO
CREATE PROCEDURE sp_UpdateServicio(
    IN p_codigo                VARCHAR(20),
    IN p_nombre_comercial      VARCHAR(150),
    IN p_categoria             VARCHAR(80),
    IN p_descripcion           TEXT,
    IN p_duracion_estimada     VARCHAR(60),
    IN p_metodologia           VARCHAR(150),
    IN p_tarifario_referencial NUMERIC(12,2)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM servicios WHERE codigo = p_codigo;

    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El servicio no existe';
    END IF;

    UPDATE servicios
    SET nombre_comercial      = p_nombre_comercial,
        categoria             = p_categoria,
        descripcion           = p_descripcion,
        duracion_estimada     = p_duracion_estimada,
        metodologia           = p_metodologia,
        tarifario_referencial = p_tarifario_referencial
    WHERE codigo = p_codigo;

    COMMIT;

    SELECT 'Servicio actualizado correctamente' AS mensaje;
END //


-- 3. ELIMINAR SERVICIO
CREATE PROCEDURE sp_DeleteServicio(
    IN p_codigo VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
            ROLLBACK;
            RESIGNAL;
        END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM servicios WHERE codigo = p_codigo;

    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El servicio no existe';
    END IF;

    -- Verificar si el servicio está asociado a algún proyecto
    SELECT COUNT(*) INTO v_count FROM proyectos WHERE servicio_codigo = p_codigo;

    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'No se puede eliminar: el servicio tiene proyectos asociados';
    END IF;

    DELETE FROM servicios WHERE codigo = p_codigo;

    COMMIT;

    SELECT 'Servicio eliminado correctamente' AS mensaje;
END //


-- 4. OBTENER SERVICIO POR CÓDIGO
CREATE PROCEDURE sp_GetServicio(
    IN p_codigo VARCHAR(20)
)
BEGIN
    SELECT * FROM servicios WHERE codigo = p_codigo;
END //


-- 5. OBTENER TODOS LOS SERVICIOS
CREATE PROCEDURE sp_GetAllServicios()
BEGIN
    SELECT codigo, nombre_comercial, categoria,
           duracion_estimada, tarifario_referencial
    FROM servicios
    ORDER BY nombre_comercial;
END //


-- 6. BUSCAR SERVICIOS POR NOMBRE O CATEGORÍA
CREATE PROCEDURE sp_SearchServicios(
    IN p_termino VARCHAR(100)
)
BEGIN
    SELECT codigo, nombre_comercial, categoria,
           duracion_estimada, tarifario_referencial
    FROM servicios
    WHERE nombre_comercial LIKE CONCAT('%', p_termino, '%')
       OR categoria        LIKE CONCAT('%', p_termino, '%')
       OR metodologia      LIKE CONCAT('%', p_termino, '%')
    ORDER BY nombre_comercial;
END //


-- ============================================================
-- PROCEDIMIENTOS AUXILIARES
-- (adapta sp_GetAllCategories, sp_GetAllSuppliers)
-- ============================================================

-- Obtener consultores disponibles (para asignar a proyectos)
CREATE PROCEDURE sp_GetConsultoresDisponibles()
BEGIN
    SELECT codigo_empleado,
           CONCAT(nombres, ' ', apellidos) AS nombre_completo,
           nivel, especialidades, tarifa_horaria
    FROM consultores
    WHERE disponibilidad != 'no disponible'
    ORDER BY nivel, apellidos;
END //


-- Obtener clientes activos (con proyectos en curso)
CREATE PROCEDURE sp_GetClientesActivos()
BEGIN
    SELECT DISTINCT c.codigo, c.razon_social, c.tipo,
                    c.contacto_principal, c.correo_electronico
    FROM clientes c
             INNER JOIN proyectos p ON c.codigo = p.cliente_codigo
    WHERE p.estado = 'en curso'
    ORDER BY c.razon_social;
END //


DELIMITER ;

CREATE PROCEDURE sp_InsertProyecto(
    IN p_numero                 VARCHAR(20),
    IN p_titulo                 VARCHAR(200),
    IN p_cliente_codigo         VARCHAR(20),
    IN p_servicio_codigo        VARCHAR(20),
    IN p_alcance                TEXT,
    IN p_objetivos              TEXT,
    IN p_fecha_inicio           DATE,
    IN p_duracion_prevista_dias INTEGER,
    IN p_presupuesto_aprobado   NUMERIC(14,2),
    IN p_fases_principales      TEXT,
    IN p_estado                 VARCHAR(20),
    IN p_nivel_confidencialidad VARCHAR(20)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    INSERT INTO proyectos (
        numero, titulo, cliente_codigo, servicio_codigo, alcance, objetivos,
        fecha_inicio, duracion_prevista_dias, presupuesto_aprobado,
        fases_principales, estado, nivel_confidencialidad
    ) VALUES (
        p_numero, p_titulo, p_cliente_codigo, p_servicio_codigo, p_alcance, p_objetivos,
        p_fecha_inicio, p_duracion_prevista_dias, p_presupuesto_aprobado,
        p_fases_principales, p_estado, p_nivel_confidencialidad
    );

    COMMIT;
    SELECT p_numero AS numero, 'Proyecto insertado correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_UpdateProyecto(
    IN p_numero                 VARCHAR(20),
    IN p_titulo                 VARCHAR(200),
    IN p_cliente_codigo         VARCHAR(20),
    IN p_servicio_codigo        VARCHAR(20),
    IN p_alcance                TEXT,
    IN p_objetivos              TEXT,
    IN p_fecha_inicio           DATE,
    IN p_duracion_prevista_dias INTEGER,
    IN p_presupuesto_aprobado   NUMERIC(14,2),
    IN p_fases_principales      TEXT,
    IN p_estado                 VARCHAR(20),
    IN p_nivel_confidencialidad VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM proyectos WHERE numero = p_numero;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El proyecto no existe';
    END IF;

    UPDATE proyectos SET
        titulo                 = p_titulo,
        cliente_codigo         = p_cliente_codigo,
        servicio_codigo        = p_servicio_codigo,
        alcance                = p_alcance,
        objetivos              = p_objetivos,
        fecha_inicio           = p_fecha_inicio,
        duracion_prevista_dias = p_duracion_prevista_dias,
        presupuesto_aprobado   = p_presupuesto_aprobado,
        fases_principales      = p_fases_principales,
        estado                 = p_estado,
        nivel_confidencialidad = p_nivel_confidencialidad
    WHERE numero = p_numero;

    COMMIT;
    SELECT 'Proyecto actualizado correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_DeleteProyecto(
    IN p_numero VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM proyectos WHERE numero = p_numero;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El proyecto no existe';
    END IF;

    SELECT COUNT(*) INTO v_count FROM fases WHERE proyecto_numero = p_numero;
    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede eliminar: el proyecto tiene fases asociadas';
    END IF;

    SELECT COUNT(*) INTO v_count FROM facturas WHERE proyecto_numero = p_numero;
    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede eliminar: el proyecto tiene facturas asociadas';
    END IF;

    SELECT COUNT(*) INTO v_count FROM proyecto_consultores WHERE proyecto_numero = p_numero;
    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede eliminar: el proyecto tiene consultores asignados';
    END IF;

    DELETE FROM proyectos WHERE numero = p_numero;

    COMMIT;
    SELECT 'Proyecto eliminado correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_GetProyecto(
    IN p_numero VARCHAR(20)
)
BEGIN
    SELECT * FROM proyectos WHERE numero = p_numero;
END //


CREATE PROCEDURE sp_GetAllProyectos()
BEGIN
    SELECT numero, titulo, cliente_codigo, servicio_codigo,
           fecha_inicio, presupuesto_aprobado, estado, nivel_confidencialidad
    FROM proyectos
    ORDER BY fecha_inicio DESC;
END //


CREATE PROCEDURE sp_SearchProyectos(
    IN p_termino VARCHAR(100)
)
BEGIN
    SELECT numero, titulo, cliente_codigo, servicio_codigo,
           fecha_inicio, presupuesto_aprobado, estado, nivel_confidencialidad
    FROM proyectos
    WHERE titulo          LIKE CONCAT('%', p_termino, '%')
       OR cliente_codigo  LIKE CONCAT('%', p_termino, '%')
       OR estado          LIKE CONCAT('%', p_termino, '%')
    ORDER BY fecha_inicio DESC;
END //


CREATE PROCEDURE sp_GetProyectosByCliente(
    IN p_cliente_codigo VARCHAR(20)
)
BEGIN
    SELECT numero, titulo, cliente_codigo, servicio_codigo,
           fecha_inicio, presupuesto_aprobado, estado, nivel_confidencialidad
    FROM proyectos
    WHERE cliente_codigo = p_cliente_codigo
    ORDER BY fecha_inicio DESC;
END //


-- ============================================================
-- PROPUESTAS
-- ============================================================

CREATE PROCEDURE sp_InsertPropuesta(
    IN p_numero                 VARCHAR(20),
    IN p_fecha_presentacion     DATE,
    IN p_cliente_codigo         VARCHAR(20),
    IN p_titulo                 VARCHAR(200),
    IN p_servicios_incluidos    TEXT,
    IN p_enfoque_metodologico   TEXT,
    IN p_equipo_propuesto       TEXT,
    IN p_cronograma_tentativo   TEXT,
    IN p_inversion_requerida    NUMERIC(14,2),
    IN p_condiciones_comerciales TEXT,
    IN p_validez_dias           SMALLINT,
    IN p_estado                 VARCHAR(20)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    INSERT INTO propuestas (
        numero, fecha_presentacion, cliente_codigo, titulo, servicios_incluidos,
        enfoque_metodologico, equipo_propuesto, cronograma_tentativo,
        inversion_requerida, condiciones_comerciales, validez_dias, estado
    ) VALUES (
        p_numero, p_fecha_presentacion, p_cliente_codigo, p_titulo, p_servicios_incluidos,
        p_enfoque_metodologico, p_equipo_propuesto, p_cronograma_tentativo,
        p_inversion_requerida, p_condiciones_comerciales, p_validez_dias, p_estado
    );

    COMMIT;
    SELECT p_numero AS numero, 'Propuesta insertada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_UpdatePropuesta(
    IN p_numero                 VARCHAR(20),
    IN p_fecha_presentacion     DATE,
    IN p_cliente_codigo         VARCHAR(20),
    IN p_titulo                 VARCHAR(200),
    IN p_servicios_incluidos    TEXT,
    IN p_enfoque_metodologico   TEXT,
    IN p_equipo_propuesto       TEXT,
    IN p_cronograma_tentativo   TEXT,
    IN p_inversion_requerida    NUMERIC(14,2),
    IN p_condiciones_comerciales TEXT,
    IN p_validez_dias           SMALLINT,
    IN p_estado                 VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM propuestas WHERE numero = p_numero;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La propuesta no existe';
    END IF;

    UPDATE propuestas SET
        fecha_presentacion    = p_fecha_presentacion,
        cliente_codigo        = p_cliente_codigo,
        titulo                = p_titulo,
        servicios_incluidos   = p_servicios_incluidos,
        enfoque_metodologico  = p_enfoque_metodologico,
        equipo_propuesto      = p_equipo_propuesto,
        cronograma_tentativo  = p_cronograma_tentativo,
        inversion_requerida   = p_inversion_requerida,
        condiciones_comerciales = p_condiciones_comerciales,
        validez_dias          = p_validez_dias,
        estado                = p_estado
    WHERE numero = p_numero;

    COMMIT;
    SELECT 'Propuesta actualizada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_DeletePropuesta(
    IN p_numero VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM propuestas WHERE numero = p_numero;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La propuesta no existe';
    END IF;

    DELETE FROM propuestas WHERE numero = p_numero;

    COMMIT;
    SELECT 'Propuesta eliminada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_GetPropuesta(
    IN p_numero VARCHAR(20)
)
BEGIN
    SELECT * FROM propuestas WHERE numero = p_numero;
END //


CREATE PROCEDURE sp_GetAllPropuestas()
BEGIN
    SELECT numero, fecha_presentacion, cliente_codigo, titulo,
           inversion_requerida, validez_dias, estado
    FROM propuestas
    ORDER BY fecha_presentacion DESC;
END //


CREATE PROCEDURE sp_SearchPropuestas(
    IN p_termino VARCHAR(100)
)
BEGIN
    SELECT numero, fecha_presentacion, cliente_codigo, titulo,
           inversion_requerida, validez_dias, estado
    FROM propuestas
    WHERE titulo         LIKE CONCAT('%', p_termino, '%')
       OR cliente_codigo LIKE CONCAT('%', p_termino, '%')
       OR estado         LIKE CONCAT('%', p_termino, '%')
    ORDER BY fecha_presentacion DESC;
END //


-- ============================================================
-- FASES
-- ============================================================

CREATE PROCEDURE sp_InsertFase(
    IN p_codigo                   VARCHAR(20),
    IN p_proyecto_numero          VARCHAR(20),
    IN p_nombre                   VARCHAR(150),
    IN p_descripcion              TEXT,
    IN p_fecha_inicio_planificada DATE,
    IN p_fecha_inicio_real        DATE,
    IN p_fecha_fin_planificada    DATE,
    IN p_fecha_fin_real           DATE,
    IN p_responsable_codigo       VARCHAR(20),
    IN p_entregables_asociados    TEXT,
    IN p_esfuerzo_estimado_horas  NUMERIC(8,2),
    IN p_recursos_necesarios      TEXT,
    IN p_dependencias             TEXT,
    IN p_porcentaje_avance        NUMERIC(5,2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    INSERT INTO fases (
        codigo, proyecto_numero, nombre, descripcion,
        fecha_inicio_planificada, fecha_inicio_real,
        fecha_fin_planificada, fecha_fin_real,
        responsable_codigo, entregables_asociados,
        esfuerzo_estimado_horas, recursos_necesarios,
        dependencias, porcentaje_avance
    ) VALUES (
        p_codigo, p_proyecto_numero, p_nombre, p_descripcion,
        p_fecha_inicio_planificada, p_fecha_inicio_real,
        p_fecha_fin_planificada, p_fecha_fin_real,
        p_responsable_codigo, p_entregables_asociados,
        p_esfuerzo_estimado_horas, p_recursos_necesarios,
        p_dependencias, p_porcentaje_avance
    );

    COMMIT;
    SELECT p_codigo AS codigo, 'Fase insertada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_UpdateFase(
    IN p_codigo                   VARCHAR(20),
    IN p_proyecto_numero          VARCHAR(20),
    IN p_nombre                   VARCHAR(150),
    IN p_descripcion              TEXT,
    IN p_fecha_inicio_planificada DATE,
    IN p_fecha_inicio_real        DATE,
    IN p_fecha_fin_planificada    DATE,
    IN p_fecha_fin_real           DATE,
    IN p_responsable_codigo       VARCHAR(20),
    IN p_entregables_asociados    TEXT,
    IN p_esfuerzo_estimado_horas  NUMERIC(8,2),
    IN p_recursos_necesarios      TEXT,
    IN p_dependencias             TEXT,
    IN p_porcentaje_avance        NUMERIC(5,2)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM fases WHERE codigo = p_codigo;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La fase no existe';
    END IF;

    UPDATE fases SET
        proyecto_numero          = p_proyecto_numero,
        nombre                   = p_nombre,
        descripcion              = p_descripcion,
        fecha_inicio_planificada = p_fecha_inicio_planificada,
        fecha_inicio_real        = p_fecha_inicio_real,
        fecha_fin_planificada    = p_fecha_fin_planificada,
        fecha_fin_real           = p_fecha_fin_real,
        responsable_codigo       = p_responsable_codigo,
        entregables_asociados    = p_entregables_asociados,
        esfuerzo_estimado_horas  = p_esfuerzo_estimado_horas,
        recursos_necesarios      = p_recursos_necesarios,
        dependencias             = p_dependencias,
        porcentaje_avance        = p_porcentaje_avance
    WHERE codigo = p_codigo;

    COMMIT;
    SELECT 'Fase actualizada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_DeleteFase(
    IN p_codigo VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM fases WHERE codigo = p_codigo;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La fase no existe';
    END IF;

    SELECT COUNT(*) INTO v_count FROM entregables WHERE fase_codigo = p_codigo;
    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede eliminar: la fase tiene entregables asociados';
    END IF;

    DELETE FROM fases WHERE codigo = p_codigo;

    COMMIT;
    SELECT 'Fase eliminada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_GetFase(
    IN p_codigo VARCHAR(20)
)
BEGIN
    SELECT * FROM fases WHERE codigo = p_codigo;
END //


CREATE PROCEDURE sp_GetAllFases()
BEGIN
    SELECT codigo, proyecto_numero, nombre, responsable_codigo,
           fecha_inicio_planificada, fecha_fin_planificada, porcentaje_avance
    FROM fases
    ORDER BY proyecto_numero, fecha_inicio_planificada;
END //


CREATE PROCEDURE sp_GetFasesByProyecto(
    IN p_proyecto_numero VARCHAR(20)
)
BEGIN
    SELECT codigo, proyecto_numero, nombre, responsable_codigo,
           fecha_inicio_planificada, fecha_fin_planificada, porcentaje_avance
    FROM fases
    WHERE proyecto_numero = p_proyecto_numero
    ORDER BY fecha_inicio_planificada;
END //


-- ============================================================
-- ENTREGABLES
-- ============================================================

CREATE PROCEDURE sp_InsertEntregable(
    IN p_codigo                    VARCHAR(20),
    IN p_proyecto_numero           VARCHAR(20),
    IN p_fase_codigo               VARCHAR(20),
    IN p_titulo                    VARCHAR(200),
    IN p_tipo                      VARCHAR(30),
    IN p_descripcion               TEXT,
    IN p_autor_principal_codigo    VARCHAR(20),
    IN p_colaboradores             TEXT,
    IN p_fecha_entrega_planificada DATE,
    IN p_fecha_entrega_real        DATE,
    IN p_estado_revision           VARCHAR(50),
    IN p_version_actual            VARCHAR(10),
    IN p_aprobacion_cliente        BOOLEAN
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    INSERT INTO entregables (
        codigo, proyecto_numero, fase_codigo, titulo, tipo, descripcion,
        autor_principal_codigo, colaboradores, fecha_entrega_planificada,
        fecha_entrega_real, estado_revision, version_actual, aprobacion_cliente
    ) VALUES (
        p_codigo, p_proyecto_numero, p_fase_codigo, p_titulo, p_tipo, p_descripcion,
        p_autor_principal_codigo, p_colaboradores, p_fecha_entrega_planificada,
        p_fecha_entrega_real, p_estado_revision, p_version_actual, p_aprobacion_cliente
    );

    COMMIT;
    SELECT p_codigo AS codigo, 'Entregable insertado correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_UpdateEntregable(
    IN p_codigo                    VARCHAR(20),
    IN p_proyecto_numero           VARCHAR(20),
    IN p_fase_codigo               VARCHAR(20),
    IN p_titulo                    VARCHAR(200),
    IN p_tipo                      VARCHAR(30),
    IN p_descripcion               TEXT,
    IN p_autor_principal_codigo    VARCHAR(20),
    IN p_colaboradores             TEXT,
    IN p_fecha_entrega_planificada DATE,
    IN p_fecha_entrega_real        DATE,
    IN p_estado_revision           VARCHAR(50),
    IN p_version_actual            VARCHAR(10),
    IN p_aprobacion_cliente        BOOLEAN
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM entregables WHERE codigo = p_codigo;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El entregable no existe';
    END IF;

    UPDATE entregables SET
        proyecto_numero           = p_proyecto_numero,
        fase_codigo               = p_fase_codigo,
        titulo                    = p_titulo,
        tipo                      = p_tipo,
        descripcion               = p_descripcion,
        autor_principal_codigo    = p_autor_principal_codigo,
        colaboradores             = p_colaboradores,
        fecha_entrega_planificada = p_fecha_entrega_planificada,
        fecha_entrega_real        = p_fecha_entrega_real,
        estado_revision           = p_estado_revision,
        version_actual            = p_version_actual,
        aprobacion_cliente        = p_aprobacion_cliente
    WHERE codigo = p_codigo;

    COMMIT;
    SELECT 'Entregable actualizado correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_DeleteEntregable(
    IN p_codigo VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM entregables WHERE codigo = p_codigo;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El entregable no existe';
    END IF;

    DELETE FROM entregables WHERE codigo = p_codigo;

    COMMIT;
    SELECT 'Entregable eliminado correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_GetEntregable(
    IN p_codigo VARCHAR(20)
)
BEGIN
    SELECT * FROM entregables WHERE codigo = p_codigo;
END //


CREATE PROCEDURE sp_GetAllEntregables()
BEGIN
    SELECT codigo, proyecto_numero, fase_codigo, titulo, tipo,
           autor_principal_codigo, fecha_entrega_planificada,
           fecha_entrega_real, estado_revision, version_actual, aprobacion_cliente
    FROM entregables
    ORDER BY proyecto_numero, fecha_entrega_planificada;
END //


CREATE PROCEDURE sp_GetEntregablesByProyecto(
    IN p_proyecto_numero VARCHAR(20)
)
BEGIN
    SELECT codigo, proyecto_numero, fase_codigo, titulo, tipo,
           autor_principal_codigo, fecha_entrega_planificada,
           fecha_entrega_real, estado_revision, version_actual, aprobacion_cliente
    FROM entregables
    WHERE proyecto_numero = p_proyecto_numero
    ORDER BY fecha_entrega_planificada;
END //


-- ============================================================
-- HORAS TRABAJADAS
-- ============================================================

CREATE PROCEDURE sp_InsertHoraTrabajada(
    IN p_consultor_codigo      VARCHAR(20),
    IN p_proyecto_numero       VARCHAR(20),
    IN p_fecha                 DATE,
    IN p_actividad_realizada   VARCHAR(200),
    IN p_horas_dedicadas       NUMERIC(6,2),
    IN p_lugar                 VARCHAR(20),
    IN p_descripcion_detallada TEXT,
    IN p_resultados_obtenidos  TEXT,
    IN p_dificultades          TEXT,
    IN p_horas_facturables     NUMERIC(6,2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    INSERT INTO horas_trabajadas (
        consultor_codigo, proyecto_numero, fecha, actividad_realizada,
        horas_dedicadas, lugar, descripcion_detallada,
        resultados_obtenidos, dificultades, horas_facturables
    ) VALUES (
        p_consultor_codigo, p_proyecto_numero, p_fecha, p_actividad_realizada,
        p_horas_dedicadas, p_lugar, p_descripcion_detallada,
        p_resultados_obtenidos, p_dificultades, p_horas_facturables
    );

    COMMIT;
    SELECT LAST_INSERT_ID() AS id, 'Hora registrada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_UpdateHoraTrabajada(
    IN p_id                    INT,
    IN p_consultor_codigo      VARCHAR(20),
    IN p_proyecto_numero       VARCHAR(20),
    IN p_fecha                 DATE,
    IN p_actividad_realizada   VARCHAR(200),
    IN p_horas_dedicadas       NUMERIC(6,2),
    IN p_lugar                 VARCHAR(20),
    IN p_descripcion_detallada TEXT,
    IN p_resultados_obtenidos  TEXT,
    IN p_dificultades          TEXT,
    IN p_horas_facturables     NUMERIC(6,2)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM horas_trabajadas WHERE id = p_id;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El registro de horas no existe';
    END IF;

    UPDATE horas_trabajadas SET
        consultor_codigo      = p_consultor_codigo,
        proyecto_numero       = p_proyecto_numero,
        fecha                 = p_fecha,
        actividad_realizada   = p_actividad_realizada,
        horas_dedicadas       = p_horas_dedicadas,
        lugar                 = p_lugar,
        descripcion_detallada = p_descripcion_detallada,
        resultados_obtenidos  = p_resultados_obtenidos,
        dificultades          = p_dificultades,
        horas_facturables     = p_horas_facturables
    WHERE id = p_id;

    COMMIT;
    SELECT 'Hora actualizada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_DeleteHoraTrabajada(
    IN p_id INT
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM horas_trabajadas WHERE id = p_id;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El registro de horas no existe';
    END IF;

    DELETE FROM horas_trabajadas WHERE id = p_id;

    COMMIT;
    SELECT 'Hora eliminada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_GetHoraTrabajada(
    IN p_id INT
)
BEGIN
    SELECT * FROM horas_trabajadas WHERE id = p_id;
END //


CREATE PROCEDURE sp_GetAllHorasTrabajadas()
BEGIN
    SELECT id, consultor_codigo, proyecto_numero, fecha,
           actividad_realizada, horas_dedicadas, lugar, horas_facturables
    FROM horas_trabajadas
    ORDER BY fecha DESC;
END //


CREATE PROCEDURE sp_GetHorasByConsultor(
    IN p_consultor_codigo VARCHAR(20)
)
BEGIN
    SELECT id, consultor_codigo, proyecto_numero, fecha,
           actividad_realizada, horas_dedicadas, lugar, horas_facturables
    FROM horas_trabajadas
    WHERE consultor_codigo = p_consultor_codigo
    ORDER BY fecha DESC;
END //


CREATE PROCEDURE sp_GetHorasByProyecto(
    IN p_proyecto_numero VARCHAR(20)
)
BEGIN
    SELECT id, consultor_codigo, proyecto_numero, fecha,
           actividad_realizada, horas_dedicadas, lugar, horas_facturables
    FROM horas_trabajadas
    WHERE proyecto_numero = p_proyecto_numero
    ORDER BY fecha DESC;
END //


-- ============================================================
-- FACTURAS
-- ============================================================

CREATE PROCEDURE sp_InsertFactura(
    IN p_numero_factura       VARCHAR(20),
    IN p_fecha                DATE,
    IN p_cliente_codigo       VARCHAR(20),
    IN p_proyecto_numero      VARCHAR(20),
    IN p_periodo_inicio       DATE,
    IN p_periodo_fin          DATE,
    IN p_servicios_prestados  TEXT,
    IN p_honorarios           NUMERIC(14,2),
    IN p_gastos_reembolsables NUMERIC(14,2),
    IN p_descuentos           NUMERIC(14,2),
    IN p_impuestos            NUMERIC(14,2),
    IN p_condiciones_pago     VARCHAR(100),
    IN p_estado               VARCHAR(20)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    INSERT INTO facturas (
        numero_factura, fecha, cliente_codigo, proyecto_numero,
        periodo_inicio, periodo_fin, servicios_prestados,
        honorarios, gastos_reembolsables, descuentos, impuestos,
        condiciones_pago, estado
    ) VALUES (
        p_numero_factura, p_fecha, p_cliente_codigo, p_proyecto_numero,
        p_periodo_inicio, p_periodo_fin, p_servicios_prestados,
        p_honorarios, p_gastos_reembolsables, p_descuentos, p_impuestos,
        p_condiciones_pago, p_estado
    );

    COMMIT;
    SELECT p_numero_factura AS numero_factura, 'Factura insertada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_UpdateFactura(
    IN p_numero_factura       VARCHAR(20),
    IN p_fecha                DATE,
    IN p_cliente_codigo       VARCHAR(20),
    IN p_proyecto_numero      VARCHAR(20),
    IN p_periodo_inicio       DATE,
    IN p_periodo_fin          DATE,
    IN p_servicios_prestados  TEXT,
    IN p_honorarios           NUMERIC(14,2),
    IN p_gastos_reembolsables NUMERIC(14,2),
    IN p_descuentos           NUMERIC(14,2),
    IN p_impuestos            NUMERIC(14,2),
    IN p_condiciones_pago     VARCHAR(100),
    IN p_estado               VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM facturas WHERE numero_factura = p_numero_factura;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La factura no existe';
    END IF;

    UPDATE facturas SET
        fecha                = p_fecha,
        cliente_codigo       = p_cliente_codigo,
        proyecto_numero      = p_proyecto_numero,
        periodo_inicio       = p_periodo_inicio,
        periodo_fin          = p_periodo_fin,
        servicios_prestados  = p_servicios_prestados,
        honorarios           = p_honorarios,
        gastos_reembolsables = p_gastos_reembolsables,
        descuentos           = p_descuentos,
        impuestos            = p_impuestos,
        condiciones_pago     = p_condiciones_pago,
        estado               = p_estado
    WHERE numero_factura = p_numero_factura;

    COMMIT;
    SELECT 'Factura actualizada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_DeleteFactura(
    IN p_numero_factura VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM facturas WHERE numero_factura = p_numero_factura;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La factura no existe';
    END IF;

    DELETE FROM facturas WHERE numero_factura = p_numero_factura;

    COMMIT;
    SELECT 'Factura eliminada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_GetFactura(
    IN p_numero_factura VARCHAR(20)
)
BEGIN
    SELECT * FROM facturas WHERE numero_factura = p_numero_factura;
END //


CREATE PROCEDURE sp_GetAllFacturas()
BEGIN
    SELECT numero_factura, fecha, cliente_codigo, proyecto_numero,
           honorarios, gastos_reembolsables, descuentos, impuestos,
           condiciones_pago, estado
    FROM facturas
    ORDER BY fecha DESC;
END //


CREATE PROCEDURE sp_GetFacturasByCliente(
    IN p_cliente_codigo VARCHAR(20)
)
BEGIN
    SELECT numero_factura, fecha, cliente_codigo, proyecto_numero,
           honorarios, gastos_reembolsables, descuentos, impuestos,
           condiciones_pago, estado
    FROM facturas
    WHERE cliente_codigo = p_cliente_codigo
    ORDER BY fecha DESC;
END //


-- ============================================================
-- CONOCIMIENTO
-- ============================================================

CREATE PROCEDURE sp_InsertConocimiento(
    IN p_codigo                  VARCHAR(20),
    IN p_titulo                  VARCHAR(200),
    IN p_tipo                    VARCHAR(30),
    IN p_industria               VARCHAR(100),
    IN p_autor_codigo            VARCHAR(20),
    IN p_fecha_creacion          DATE,
    IN p_descripcion             TEXT,
    IN p_palabras_clave          TEXT,
    IN p_archivo_adjunto         VARCHAR(250),
    IN p_nivel_acceso            VARCHAR(20),
    IN p_potencial_reutilizacion VARCHAR(20)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    INSERT INTO conocimiento (
        codigo, titulo, tipo, industria, autor_codigo, fecha_creacion,
        descripcion, palabras_clave, archivo_adjunto,
        nivel_acceso, potencial_reutilizacion
    ) VALUES (
        p_codigo, p_titulo, p_tipo, p_industria, p_autor_codigo, p_fecha_creacion,
        p_descripcion, p_palabras_clave, p_archivo_adjunto,
        p_nivel_acceso, p_potencial_reutilizacion
    );

    COMMIT;
    SELECT p_codigo AS codigo, 'Conocimiento insertado correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_UpdateConocimiento(
    IN p_codigo                  VARCHAR(20),
    IN p_titulo                  VARCHAR(200),
    IN p_tipo                    VARCHAR(30),
    IN p_industria               VARCHAR(100),
    IN p_autor_codigo            VARCHAR(20),
    IN p_fecha_creacion          DATE,
    IN p_descripcion             TEXT,
    IN p_palabras_clave          TEXT,
    IN p_archivo_adjunto         VARCHAR(250),
    IN p_nivel_acceso            VARCHAR(20),
    IN p_potencial_reutilizacion VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM conocimiento WHERE codigo = p_codigo;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El registro de conocimiento no existe';
    END IF;

    UPDATE conocimiento SET
        titulo                 = p_titulo,
        tipo                   = p_tipo,
        industria              = p_industria,
        autor_codigo           = p_autor_codigo,
        fecha_creacion         = p_fecha_creacion,
        descripcion            = p_descripcion,
        palabras_clave         = p_palabras_clave,
        archivo_adjunto        = p_archivo_adjunto,
        nivel_acceso           = p_nivel_acceso,
        potencial_reutilizacion = p_potencial_reutilizacion
    WHERE codigo = p_codigo;

    COMMIT;
    SELECT 'Conocimiento actualizado correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_DeleteConocimiento(
    IN p_codigo VARCHAR(20)
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM conocimiento WHERE codigo = p_codigo;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El registro de conocimiento no existe';
    END IF;

    DELETE FROM conocimiento WHERE codigo = p_codigo;

    COMMIT;
    SELECT 'Conocimiento eliminado correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_GetConocimiento(
    IN p_codigo VARCHAR(20)
)
BEGIN
    SELECT * FROM conocimiento WHERE codigo = p_codigo;
END //


CREATE PROCEDURE sp_GetAllConocimiento()
BEGIN
    SELECT codigo, titulo, tipo, industria, autor_codigo,
           fecha_creacion, nivel_acceso, potencial_reutilizacion
    FROM conocimiento
    ORDER BY fecha_creacion DESC;
END //


CREATE PROCEDURE sp_SearchConocimiento(
    IN p_termino VARCHAR(100)
)
BEGIN
    SELECT codigo, titulo, tipo, industria, autor_codigo,
           fecha_creacion, nivel_acceso, potencial_reutilizacion
    FROM conocimiento
    WHERE titulo         LIKE CONCAT('%', p_termino, '%')
       OR palabras_clave LIKE CONCAT('%', p_termino, '%')
       OR industria      LIKE CONCAT('%', p_termino, '%')
    ORDER BY fecha_creacion DESC;
END //


-- ============================================================
-- PROYECTO_CONSULTORES
-- ============================================================

CREATE PROCEDURE sp_InsertProyectoConsultor(
    IN p_proyecto_numero       VARCHAR(20),
    IN p_consultor_codigo      VARCHAR(20),
    IN p_rol                   VARCHAR(80),
    IN p_dedicacion_porcentaje SMALLINT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    INSERT INTO proyecto_consultores (
        proyecto_numero, consultor_codigo, rol, dedicacion_porcentaje
    ) VALUES (
        p_proyecto_numero, p_consultor_codigo, p_rol, p_dedicacion_porcentaje
    );

    COMMIT;
    SELECT LAST_INSERT_ID() AS id, 'Consultor asignado correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_UpdateProyectoConsultor(
    IN p_id                    INT,
    IN p_rol                   VARCHAR(80),
    IN p_dedicacion_porcentaje SMALLINT
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM proyecto_consultores WHERE id = p_id;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La asignacion no existe';
    END IF;

    UPDATE proyecto_consultores SET
        rol                   = p_rol,
        dedicacion_porcentaje = p_dedicacion_porcentaje
    WHERE id = p_id;

    COMMIT;
    SELECT 'Asignacion actualizada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_DeleteProyectoConsultor(
    IN p_id INT
)
BEGIN
    DECLARE v_count INT DEFAULT 0;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN ROLLBACK; RESIGNAL; END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count FROM proyecto_consultores WHERE id = p_id;
    IF v_count = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La asignacion no existe';
    END IF;

    DELETE FROM proyecto_consultores WHERE id = p_id;

    COMMIT;
    SELECT 'Asignacion eliminada correctamente' AS mensaje;
END //


CREATE PROCEDURE sp_GetAllProyectoConsultores()
BEGIN
    SELECT id, proyecto_numero, consultor_codigo, rol, dedicacion_porcentaje
    FROM proyecto_consultores
    ORDER BY proyecto_numero;
END //


CREATE PROCEDURE sp_GetConsultoresByProyecto(
    IN p_proyecto_numero VARCHAR(20)
)
BEGIN
    SELECT id, proyecto_numero, consultor_codigo, rol, dedicacion_porcentaje
    FROM proyecto_consultores
    WHERE proyecto_numero = p_proyecto_numero;
END //


CREATE PROCEDURE sp_GetProyectosByConsultor(
    IN p_consultor_codigo VARCHAR(20)
)
BEGIN
    SELECT id, proyecto_numero, consultor_codigo, rol, dedicacion_porcentaje
    FROM proyecto_consultores
    WHERE consultor_codigo = p_consultor_codigo;
END //


DELIMITER ;