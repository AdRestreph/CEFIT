-- ============================================================
-- CLIENTES
-- (adapta sp_InsertCustomer, sp_UpdateCustomer, sp_DeleteCustomer,
--  sp_GetCustomer, sp_GetAllCustomers, sp_SearchCustomers)
-- ============================================================
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