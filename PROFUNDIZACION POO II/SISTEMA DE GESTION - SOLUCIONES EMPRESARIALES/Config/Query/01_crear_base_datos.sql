-- ============================================================
-- 01_crear_base_datos.sql
-- Creacion de la base de datos y todas las tablas
-- Sistema de Gestion - Soluciones Empresariales
-- ============================================================

CREATE DATABASE IF NOT EXISTS SITEMA_DE_GESTION_SOLUCIONES_EMPRESARIALES;
USE SITEMA_DE_GESTION_SOLUCIONES_EMPRESARIALES;

-- ────────────────────────────────────────────────────────────
-- 1. CLIENTES
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS clientes (
    codigo                  VARCHAR(20)  PRIMARY KEY,
    tipo                    VARCHAR(20)  NOT NULL CHECK (tipo IN ('PYME', 'corporativo', 'gobierno')),
    razon_social            VARCHAR(150) NOT NULL,
    sector_actividad        VARCHAR(100),
    ruc                     VARCHAR(20)  UNIQUE,
    direccion               VARCHAR(200),
    telefono                VARCHAR(30),
    sitio_web               VARCHAR(100),
    contacto_principal      VARCHAR(100),
    cargo_contacto          VARCHAR(100),
    correo_electronico      VARCHAR(100),
    telefono_directo        VARCHAR(30),
    fecha_primera_relacion  DATE,
    origen_contacto         VARCHAR(80),
    clasificacion_potencial VARCHAR(20)
);

-- ────────────────────────────────────────────────────────────
-- 2. CONSULTORES
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS consultores (
    codigo_empleado         VARCHAR(20)  PRIMARY KEY,
    nombres                 VARCHAR(100) NOT NULL,
    apellidos               VARCHAR(100) NOT NULL,
    documento_identidad     VARCHAR(20)  UNIQUE,
    formacion_academica     VARCHAR(200),
    certificaciones         TEXT,
    especialidades          TEXT,
    anios_experiencia       SMALLINT,
    nivel                   VARCHAR(20)  CHECK (nivel IN ('junior', 'senior', 'gerente', 'socio')),
    tarifa_horaria          NUMERIC(10,2),
    idiomas                 VARCHAR(150),
    disponibilidad          VARCHAR(80)
);

-- ────────────────────────────────────────────────────────────
-- 3. SERVICIOS
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS servicios (
    codigo                  VARCHAR(20)  PRIMARY KEY,
    nombre_comercial        VARCHAR(150) NOT NULL,
    categoria               VARCHAR(80),
    descripcion             TEXT,
    entregables_tipicos     TEXT,
    duracion_estimada       VARCHAR(60),
    metodologia             VARCHAR(150),
    beneficios_cliente      TEXT,
    equipo_minimo           VARCHAR(100),
    tarifario_referencial   NUMERIC(12,2),
    casos_exito             TEXT
);

-- ────────────────────────────────────────────────────────────
-- 4. PROYECTOS
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS proyectos (
    numero                  VARCHAR(20)  PRIMARY KEY,
    titulo                  VARCHAR(200) NOT NULL,
    cliente_codigo          VARCHAR(20)  REFERENCES clientes(codigo),
    servicio_codigo         VARCHAR(20)  REFERENCES servicios(codigo),
    alcance                 TEXT,
    objetivos               TEXT,
    fecha_inicio            DATE,
    duracion_prevista_dias  INTEGER,
    presupuesto_aprobado    NUMERIC(14,2),
    fases_principales       TEXT,
    estado                  VARCHAR(20)  CHECK (estado IN ('planificación', 'en curso', 'pausado', 'cerrado', 'cancelado')),
    nivel_confidencialidad  VARCHAR(20)  CHECK (nivel_confidencialidad IN ('público', 'interno', 'confidencial', 'restringido'))
);

-- ────────────────────────────────────────────────────────────
-- 5. PROYECTO_CONSULTORES (relación N:M)
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS proyecto_consultores (
    id                      INT AUTO_INCREMENT PRIMARY KEY,
    proyecto_numero         VARCHAR(20)  REFERENCES proyectos(numero),
    consultor_codigo        VARCHAR(20)  REFERENCES consultores(codigo_empleado),
    rol                     VARCHAR(80),
    dedicacion_porcentaje   SMALLINT     CHECK (dedicacion_porcentaje BETWEEN 1 AND 100)
);

-- ────────────────────────────────────────────────────────────
-- 6. PROPUESTAS COMERCIALES
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS propuestas (
    numero                  VARCHAR(20)  PRIMARY KEY,
    fecha_presentacion      DATE,
    cliente_codigo          VARCHAR(20)  REFERENCES clientes(codigo),
    titulo                  VARCHAR(200),
    servicios_incluidos     TEXT,
    enfoque_metodologico    TEXT,
    equipo_propuesto        TEXT,
    cronograma_tentativo    TEXT,
    inversion_requerida     NUMERIC(14,2),
    condiciones_comerciales TEXT,
    validez_dias            SMALLINT,
    estado                  VARCHAR(20)  CHECK (estado IN ('enviada', 'en evaluación', 'aceptada', 'rechazada'))
);

-- ────────────────────────────────────────────────────────────
-- 7. FASES Y ACTIVIDADES
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS fases (
    codigo                   VARCHAR(20)  PRIMARY KEY,
    proyecto_numero          VARCHAR(20)  REFERENCES proyectos(numero),
    nombre                   VARCHAR(150) NOT NULL,
    descripcion              TEXT,
    fecha_inicio_planificada DATE,
    fecha_inicio_real        DATE,
    fecha_fin_planificada    DATE,
    fecha_fin_real           DATE,
    responsable_codigo       VARCHAR(20)  REFERENCES consultores(codigo_empleado),
    entregables_asociados    TEXT,
    esfuerzo_estimado_horas  NUMERIC(8,2),
    recursos_necesarios      TEXT,
    dependencias             TEXT,
    porcentaje_avance        NUMERIC(5,2) DEFAULT 0 CHECK (porcentaje_avance BETWEEN 0 AND 100)
);

-- ────────────────────────────────────────────────────────────
-- 8. ENTREGABLES
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS entregables (
    codigo                    VARCHAR(20)  PRIMARY KEY,
    proyecto_numero           VARCHAR(20)  REFERENCES proyectos(numero),
    fase_codigo               VARCHAR(20)  REFERENCES fases(codigo),
    titulo                    VARCHAR(200) NOT NULL,
    tipo                      VARCHAR(30)  CHECK (tipo IN ('informe', 'presentación', 'modelo', 'implementación')),
    descripcion               TEXT,
    autor_principal_codigo    VARCHAR(20)  REFERENCES consultores(codigo_empleado),
    colaboradores             TEXT,
    fecha_entrega_planificada DATE,
    fecha_entrega_real        DATE,
    estado_revision           VARCHAR(50),
    version_actual            VARCHAR(10)  DEFAULT '1.0',
    aprobacion_cliente        BOOLEAN      DEFAULT FALSE
);

-- ────────────────────────────────────────────────────────────
-- 9. HORAS TRABAJADAS
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS horas_trabajadas (
    id                    INT AUTO_INCREMENT PRIMARY KEY,
    consultor_codigo      VARCHAR(20)  REFERENCES consultores(codigo_empleado),
    proyecto_numero       VARCHAR(20)  REFERENCES proyectos(numero),
    fecha                 DATE         NOT NULL,
    actividad_realizada   VARCHAR(200),
    horas_dedicadas       NUMERIC(6,2) NOT NULL,
    lugar                 VARCHAR(20)  CHECK (lugar IN ('oficina', 'cliente', 'remoto')),
    descripcion_detallada TEXT,
    resultados_obtenidos  TEXT,
    dificultades          TEXT,
    horas_facturables     NUMERIC(6,2)
);

-- ────────────────────────────────────────────────────────────
-- 10. FACTURACION
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS facturas (
    numero_factura          VARCHAR(20)  PRIMARY KEY,
    fecha                   DATE         NOT NULL,
    cliente_codigo          VARCHAR(20)  REFERENCES clientes(codigo),
    proyecto_numero         VARCHAR(20)  REFERENCES proyectos(numero),
    periodo_inicio          DATE,
    periodo_fin             DATE,
    servicios_prestados     TEXT,
    honorarios              NUMERIC(14,2) DEFAULT 0,
    gastos_reembolsables    NUMERIC(14,2) DEFAULT 0,
    descuentos              NUMERIC(14,2) DEFAULT 0,
    impuestos               NUMERIC(14,2) DEFAULT 0,
    condiciones_pago        VARCHAR(100),
    estado                  VARCHAR(20)  CHECK (estado IN ('emitida', 'enviada', 'pagada', 'vencida', 'anulada'))
);

-- ────────────────────────────────────────────────────────────
-- 11. GESTION DEL CONOCIMIENTO
-- ────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS conocimiento (
    codigo                  VARCHAR(20)  PRIMARY KEY,
    titulo                  VARCHAR(200) NOT NULL,
    tipo                    VARCHAR(30)  CHECK (tipo IN ('metodología', 'herramienta', 'caso de estudio')),
    industria               VARCHAR(100),
    autor_codigo            VARCHAR(20)  REFERENCES consultores(codigo_empleado),
    fecha_creacion          DATE,
    descripcion             TEXT,
    palabras_clave          TEXT,
    archivo_adjunto         VARCHAR(250),
    nivel_acceso            VARCHAR(20)  CHECK (nivel_acceso IN ('público', 'interno', 'restringido')),
    potencial_reutilizacion VARCHAR(20)  CHECK (potencial_reutilizacion IN ('alto', 'medio', 'bajo'))
);
