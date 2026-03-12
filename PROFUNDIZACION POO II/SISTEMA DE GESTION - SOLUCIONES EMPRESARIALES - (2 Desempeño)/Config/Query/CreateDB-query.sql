CREATE DATABASE SITEMA_DE_GESTION_SOLUCIONES_EMPRESARIALES;

USE SITEMA_DE_GESTION_SOLUCIONES_EMPRESARIALES;
-- 1. CLIENTES
-- ────────────────────────────────────────────────────────────
CREATE TABLE clientes (
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
CREATE TABLE consultores (
    codigo_empleado         VARCHAR(20)  PRIMARY KEY,
    nombres                 VARCHAR(100) NOT NULL,
    apellidos               VARCHAR(100) NOT NULL,
    documento_identidad     VARCHAR(20)  UNIQUE,
    formacion_academica     VARCHAR(200),
    certificaciones         TEXT,
    especialidades          TEXT,        -- valores separados por coma: estrategia, finanzas, operaciones, marketing, recursos_humanos
    anios_experiencia       SMALLINT,
    nivel                   VARCHAR(20)  CHECK (nivel IN ('junior', 'senior', 'gerente', 'socio')),
    tarifa_horaria          NUMERIC(10,2),
    idiomas                 VARCHAR(150),
    disponibilidad          VARCHAR(80)
);

-- ────────────────────────────────────────────────────────────
-- 3. SERVICIOS
-- ────────────────────────────────────────────────────────────
CREATE TABLE servicios (
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
CREATE TABLE proyectos (
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

-- Consultores asignados a proyectos (relación N:M)
CREATE TABLE proyecto_consultores (
    id                      SERIAL       PRIMARY KEY,  -- usar INTEGER AUTOINCREMENT en SQLite
    proyecto_numero         VARCHAR(20)  REFERENCES proyectos(numero),
    consultor_codigo        VARCHAR(20)  REFERENCES consultores(codigo_empleado),
    rol                     VARCHAR(80),
    dedicacion_porcentaje   SMALLINT     CHECK (dedicacion_porcentaje BETWEEN 1 AND 100)
);

-- ────────────────────────────────────────────────────────────
-- 5. PROPUESTAS COMERCIALES
-- ────────────────────────────────────────────────────────────
CREATE TABLE propuestas (
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
-- 6. FASES Y ACTIVIDADES
-- ────────────────────────────────────────────────────────────
CREATE TABLE fases (
    codigo                  VARCHAR(20)  PRIMARY KEY,
    proyecto_numero         VARCHAR(20)  REFERENCES proyectos(numero),
    nombre                  VARCHAR(150) NOT NULL,
    descripcion             TEXT,
    fecha_inicio_planificada DATE,
    fecha_inicio_real        DATE,
    fecha_fin_planificada    DATE,
    fecha_fin_real           DATE,
    responsable_codigo      VARCHAR(20)  REFERENCES consultores(codigo_empleado),
    entregables_asociados   TEXT,
    esfuerzo_estimado_horas NUMERIC(8,2),
    recursos_necesarios     TEXT,
    dependencias            TEXT,
    porcentaje_avance       NUMERIC(5,2) DEFAULT 0 CHECK (porcentaje_avance BETWEEN 0 AND 100)
);

-- ────────────────────────────────────────────────────────────
-- 7. ENTREGABLES
-- ────────────────────────────────────────────────────────────
CREATE TABLE entregables (
    codigo                  VARCHAR(20)  PRIMARY KEY,
    proyecto_numero         VARCHAR(20)  REFERENCES proyectos(numero),
    fase_codigo             VARCHAR(20)  REFERENCES fases(codigo),
    titulo                  VARCHAR(200) NOT NULL,
    tipo                    VARCHAR(30)  CHECK (tipo IN ('informe', 'presentación', 'modelo', 'implementación')),
    descripcion             TEXT,
    autor_principal_codigo  VARCHAR(20)  REFERENCES consultores(codigo_empleado),
    colaboradores           TEXT,
    fecha_entrega_planificada DATE,
    fecha_entrega_real        DATE,
    estado_revision         VARCHAR(50),
    version_actual          VARCHAR(10)  DEFAULT '1.0',
    aprobacion_cliente      BOOLEAN      DEFAULT FALSE
);

-- ────────────────────────────────────────────────────────────
-- 8. HORAS TRABAJADAS
-- ────────────────────────────────────────────────────────────
CREATE TABLE horas_trabajadas (
    id                      SERIAL       PRIMARY KEY,  -- usar INTEGER AUTOINCREMENT en SQLite
    consultor_codigo        VARCHAR(20)  REFERENCES consultores(codigo_empleado),
    proyecto_numero         VARCHAR(20)  REFERENCES proyectos(numero),
    fecha                   DATE         NOT NULL,
    actividad_realizada     VARCHAR(200),
    horas_dedicadas         NUMERIC(6,2) NOT NULL,
    lugar                   VARCHAR(20)  CHECK (lugar IN ('oficina', 'cliente', 'remoto')),
    descripcion_detallada   TEXT,
    resultados_obtenidos    TEXT,
    dificultades            TEXT,
    horas_facturables       NUMERIC(6,2)
);

-- ────────────────────────────────────────────────────────────
-- 9. FACTURACIÓN
-- ────────────────────────────────────────────────────────────
CREATE TABLE facturas (
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
    -- total calculado en consulta: honorarios + gastos_reembolsables - descuentos + impuestos
    condiciones_pago        VARCHAR(100),
    estado                  VARCHAR(20)  CHECK (estado IN ('emitida', 'enviada', 'pagada', 'vencida', 'anulada'))
);

-- ────────────────────────────────────────────────────────────
-- 10. GESTIÓN DEL CONOCIMIENTO
-- ────────────────────────────────────────────────────────────
CREATE TABLE conocimiento (
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


-- ============================================================
-- DATOS DE EJEMPLO
-- ============================================================

INSERT INTO clientes VALUES (
    'CLI-001', 'corporativo', 'TechCorp Ecuador S.A.', 'Tecnología',
    '1791234567001', 'Av. Amazonas N39-234, Quito', '02-2345678',
    'www.techcorp.ec', 'María Fernanda López', 'Gerente General',
    'mlopez@techcorp.ec', '099-1234567', '2023-03-15', 'referido', 'alto'
);

INSERT INTO clientes VALUES (
    'CLI-002', 'PYME', 'Distribuidora El Sol Cía. Ltda.', 'Comercio',
    '0992345678001', 'Calle 9 de Octubre 456, Guayaquil', '04-3456789',
    NULL, 'Carlos Rivas', 'Propietario',
    'crivas@elsol.com.ec', '098-7654321', '2024-01-10', 'evento', 'medio'
);

INSERT INTO consultores VALUES (
    'CON-001', 'Andrés', 'Mejía Torres', '1723456789',
    'MBA - USFQ', 'PMP, Six Sigma Black Belt',
    'estrategia, operaciones', 10, 'senior',
    120.00, 'Español, Inglés', 'tiempo completo'
);

INSERT INTO consultores VALUES (
    'CON-002', 'Valeria', 'Sánchez Ruiz', '1745678901',
    'Ing. Financiera - PUCE', 'CFA Level II',
    'finanzas, estrategia', 6, 'senior',
    95.00, 'Español, Inglés, Francés', 'tiempo completo'
);

INSERT INTO consultores VALUES (
    'CON-003', 'Diego', 'Paredes Mora', '1756789012',
    'Psicología Organizacional - UCE', 'SHRM-CP',
    'recursos_humanos, marketing', 3, 'junior',
    55.00, 'Español', 'medio tiempo'
);

INSERT INTO servicios VALUES (
    'SRV-001', 'Transformación Digital', 'Estrategia',
    'Diagnóstico y hoja de ruta para digitalización empresarial',
    'Diagnóstico AS-IS, Roadmap Digital, Plan de implementación',
    '3 meses', 'Design Thinking + Agile',
    'Reducción de costos operativos, mejora de eficiencia',
    '2 consultores senior', 45000.00,
    'Banco Nacional 2022, RetailMega 2023'
);

INSERT INTO servicios VALUES (
    'SRV-002', 'Reestructuración Financiera', 'Finanzas',
    'Análisis y rediseño de estructura de capital y rentabilidad',
    'Modelo financiero, Plan de reestructuración, Dashboard KPIs',
    '6 semanas', 'Análisis DCF + Benchmarking',
    'Mejora de liquidez y reducción de costos financieros',
    '1 consultor finanzas', 22000.00,
    'GrupoAlfa 2023'
);

INSERT INTO proyectos VALUES (
    'PRY-2024-001', 'Transformación Digital TechCorp',
    'CLI-001', 'SRV-001',
    'Digitalización de procesos core del negocio',
    'Reducir tiempos de proceso en 40% y costos en 25%',
    '2024-01-15', 90, 48000.00,
    'Diagnóstico, Diseño, Implementación, Cierre',
    'en curso', 'confidencial'
);

INSERT INTO proyectos VALUES (
    'PRY-2024-002', 'Reestructuración Financiera El Sol',
    'CLI-002', 'SRV-002',
    'Revisión integral de estructura de costos y deuda',
    'Reducir carga financiera en 30% en 12 meses',
    '2024-03-01', 45, 22000.00,
    'Diagnóstico, Modelado, Recomendaciones',
    'planificación', 'interno'
);

INSERT INTO proyecto_consultores (proyecto_numero, consultor_codigo, rol, dedicacion_porcentaje) VALUES
    ('PRY-2024-001', 'CON-001', 'Líder de Proyecto',    80),
    ('PRY-2024-001', 'CON-003', 'Consultor de Apoyo',   40),
    ('PRY-2024-002', 'CON-002', 'Líder de Proyecto',   100);

INSERT INTO propuestas VALUES (
    'PROP-2024-001', '2023-12-01', 'CLI-001',
    'Propuesta Transformación Digital 2024',
    'SRV-001', 'Design Thinking + Lean',
    '1 Gerente, 2 Seniors', 'Enero–Marzo 2024',
    48000.00, '50% inicio, 50% cierre', 30, 'aceptada'
);

INSERT INTO propuestas VALUES (
    'PROP-2024-002', '2024-02-10', 'CLI-002',
    'Propuesta Reestructuración Financiera',
    'SRV-002', 'Análisis DCF + Benchmarking',
    '1 Senior Finanzas', 'Marzo–Abril 2024',
    22000.00, '40% inicio, 60% entrega final', 45, 'aceptada'
);

INSERT INTO fases VALUES (
    'FASE-001', 'PRY-2024-001', 'Diagnóstico AS-IS',
    'Levantamiento y análisis de procesos actuales',
    '2024-01-15', '2024-01-15', '2024-02-15', '2024-02-14',
    'CON-001', 'ENT-001', 160, 'Acceso a sistemas cliente', NULL, 100
);

INSERT INTO fases VALUES (
    'FASE-002', 'PRY-2024-001', 'Diseño TO-BE',
    'Definición de arquitectura de procesos futuros',
    '2024-02-15', '2024-02-16', '2024-03-15', NULL,
    'CON-001', 'ENT-002', 120, 'Talleres con equipo cliente', 'FASE-001', 60
);

INSERT INTO entregables VALUES (
    'ENT-001', 'PRY-2024-001', 'FASE-001',
    'Informe de Diagnóstico AS-IS', 'informe',
    'Análisis detallado de procesos actuales con brechas identificadas',
    'CON-001', 'CON-003',
    '2024-02-15', '2024-02-14',
    'aprobado', '2.1', TRUE
);

INSERT INTO entregables VALUES (
    'ENT-002', 'PRY-2024-001', 'FASE-002',
    'Arquitectura de Procesos TO-BE', 'modelo',
    'Modelo objetivo de procesos digitalizados con flujos BPMN',
    'CON-001', NULL,
    '2024-03-15', NULL,
    'en revisión', '1.0', FALSE
);

INSERT INTO horas_trabajadas
    (consultor_codigo, proyecto_numero, fecha, actividad_realizada,
     horas_dedicadas, lugar, descripcion_detallada, resultados_obtenidos,
     dificultades, horas_facturables)
VALUES
    ('CON-001', 'PRY-2024-001', '2024-01-20',
     'Entrevistas con gerencias', 8, 'cliente',
     'Sesiones de levantamiento con 5 gerentes de área',
     'Mapeo completo del proceso de ventas',
     'Disponibilidad limitada del equipo cliente', 8),

    ('CON-001', 'PRY-2024-001', '2024-01-22',
     'Análisis documental', 6, 'oficina',
     'Revisión de manuales de procesos y políticas internas',
     'Identificación de 12 brechas críticas',
     NULL, 6),

    ('CON-003', 'PRY-2024-001', '2024-01-23',
     'Encuesta de clima organizacional', 4, 'cliente',
     'Aplicación de encuesta a 45 colaboradores',
     'Tasa de respuesta del 89%',
     NULL, 4);

INSERT INTO facturas VALUES (
    'FAC-2024-001', '2024-02-28',
    'CLI-001', 'PRY-2024-001',
    '2024-01-15', '2024-02-28',
    'Fase 1: Diagnóstico AS-IS — Honorarios profesionales',
    24000.00, 350.00, 0, 2914.00,
    'Contado 30 días', 'pagada'
);

INSERT INTO conocimiento VALUES (
    'CON-K-001',
    'Metodología de Diagnóstico Digital para PYMES',
    'metodología', 'Tecnología / Transversal',
    'CON-001', '2024-02-28',
    'Framework probado para evaluación de madurez digital en empresas medianas ecuatorianas',
    'transformación digital, diagnóstico, madurez, PYME',
    'metodologia_diagnostico_digital_v2.pdf',
    'interno', 'alto'
);

INSERT INTO conocimiento VALUES (
    'CON-K-002',
    'Herramienta de Valoración Rápida de Empresas',
    'herramienta', 'Finanzas / Transversal',
    'CON-002', '2024-03-10',
    'Modelo Excel para valoración DCF y múltiplos en PYMES y empresas medianas',
    'valoración, DCF, múltiplos, finanzas',
    'herramienta_valoracion_v3.xlsx',
    'restringido', 'alto'
);
