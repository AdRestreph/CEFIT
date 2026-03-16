-- ============================================================
-- 03_datos_ejemplo.sql
-- Datos de ejemplo para todas las tablas
-- Sistema de Gestion - Soluciones Empresariales
-- ============================================================

USE SITEMA_DE_GESTION_SOLUCIONES_EMPRESARIALES;

-- ────────────────────────────────────────────────────────────
-- CLIENTES (muestra — ver insert_100_clientes.sql para el set completo)
-- ────────────────────────────────────────────────────────────
INSERT INTO clientes VALUES ('CLI-001','corporativo','TechCorp Ecuador S.A.','Tecnología','1791234567001','Av. Amazonas N39-234, Quito','02-2345678','www.techcorp.ec','María Fernanda López','Gerente General','mlopez@techcorp.ec','099-1234567','2023-03-15','referido','alto');
INSERT INTO clientes VALUES ('CLI-002','PYME','Distribuidora El Sol Cía. Ltda.','Comercio','0992345678001','Calle 9 de Octubre 456, Guayaquil','04-3456789',NULL,'Carlos Rivas','Propietario','crivas@elsol.com.ec','098-7654321','2024-01-10','evento','medio');
INSERT INTO clientes VALUES ('CLI-003','corporativo','Banco Pichincha S.A.','Financiero','1790011674001','Av. Amazonas y Unión Nacional, Quito','02-2980980','www.pichincha.com','Roberto Andrade','Gerente Financiero','randrade@pichincha.com','099-3456789','2023-05-10','referido','alto');
INSERT INTO clientes VALUES ('CLI-004','gobierno','Ministerio de Salud Pública','Salud','1760001550001','Av. Queseras del Medio, Quito','02-3814400','www.salud.gob.ec','Patricia Morales','Directora Administrativa','pmorales@msp.gob.ec','098-7654321','2023-06-15','evento','alto');
INSERT INTO clientes VALUES ('CLI-005','PYME','Importadora Andina Cía. Ltda.','Comercio','0990123456001','Calle Chimborazo 234, Ambato','03-2823456','www.importadoraandina.com','Javier Salazar','Propietario','jsalazar@andina.com','099-1122334','2023-07-20','web','medio');

-- ────────────────────────────────────────────────────────────
-- CONSULTORES
-- ────────────────────────────────────────────────────────────
INSERT INTO consultores VALUES ('CON-001','Andrés','Mejía Torres','1723456789','MBA - USFQ','PMP, Six Sigma Black Belt','estrategia, operaciones',10,'senior',120.00,'Español, Inglés','tiempo completo');
INSERT INTO consultores VALUES ('CON-002','Valeria','Sánchez Ruiz','1745678901','Ing. Financiera - PUCE','CFA Level II','finanzas, estrategia',6,'senior',95.00,'Español, Inglés, Francés','tiempo completo');
INSERT INTO consultores VALUES ('CON-003','Diego','Paredes Mora','1756789012','Psicología Organizacional - UCE','SHRM-CP','recursos_humanos, marketing',3,'junior',55.00,'Español','medio tiempo');
INSERT INTO consultores VALUES ('CON-004','Sofía','Vásquez León','1767890123','Ing. Sistemas - EPN','AWS Solutions Architect, Scrum Master','tecnología, operaciones',5,'senior',110.00,'Español, Inglés','tiempo completo');
INSERT INTO consultores VALUES ('CON-005','Rodrigo','Cárdenas Paz','1778901234','MBA Finanzas - IDE','CFA Level III, FRM','finanzas, estrategia',12,'gerente',180.00,'Español, Inglés, Portugués','tiempo completo');

-- ────────────────────────────────────────────────────────────
-- SERVICIOS
-- ────────────────────────────────────────────────────────────
INSERT INTO servicios VALUES ('SRV-001','Transformación Digital','Estrategia','Diagnóstico y hoja de ruta para digitalización empresarial','Diagnóstico AS-IS, Roadmap Digital, Plan de implementación','3 meses','Design Thinking + Agile','Reducción de costos operativos, mejora de eficiencia','2 consultores senior',45000.00,'Banco Nacional 2022, RetailMega 2023');
INSERT INTO servicios VALUES ('SRV-002','Reestructuración Financiera','Finanzas','Análisis y rediseño de estructura de capital y rentabilidad','Modelo financiero, Plan de reestructuración, Dashboard KPIs','6 semanas','Análisis DCF + Benchmarking','Mejora de liquidez y reducción de costos financieros','1 consultor finanzas',22000.00,'GrupoAlfa 2023');
INSERT INTO servicios VALUES ('SRV-003','Gestión del Talento Humano','Recursos Humanos','Diseño e implementación de modelo de gestión por competencias','Diccionario de competencias, Evaluaciones 360°, Plan de desarrollo','2 meses','Assessment Center + Coaching','Retención de talento, mejora del clima organizacional','1 consultor RRHH',18000.00,'Empresa XYZ 2023');
INSERT INTO servicios VALUES ('SRV-004','Estrategia Comercial','Marketing','Diagnóstico y rediseño de modelo comercial y canales de venta','Análisis de mercado, Plan comercial, KPIs de ventas','2 meses','Design Thinking + CRM','Incremento de ventas, expansión de mercado','1 consultor marketing',20000.00,'Retail Sur 2022');
INSERT INTO servicios VALUES ('SRV-005','Excelencia Operacional','Operaciones','Optimización de procesos y reducción de desperdicios','Mapeo de procesos, Plan de mejora, Dashboard operacional','3 meses','Lean Six Sigma + Kaizen','Reducción de costos, mejora de tiempos de ciclo','2 consultores operaciones',35000.00,'Manufactura Norte 2023');

-- ────────────────────────────────────────────────────────────
-- PROYECTOS
-- ────────────────────────────────────────────────────────────
INSERT INTO proyectos VALUES ('PRY-2024-001','Transformación Digital TechCorp','CLI-001','SRV-001','Digitalización de procesos core del negocio','Reducir tiempos de proceso en 40% y costos en 25%','2024-01-15',90,48000.00,'Diagnóstico, Diseño, Implementación, Cierre','en curso','confidencial');
INSERT INTO proyectos VALUES ('PRY-2024-002','Reestructuración Financiera El Sol','CLI-002','SRV-002','Revisión integral de estructura de costos y deuda','Reducir carga financiera en 30% en 12 meses','2024-03-01',45,22000.00,'Diagnóstico, Modelado, Recomendaciones','planificación','interno');
INSERT INTO proyectos VALUES ('PRY-2024-003','Estrategia Comercial Banco Pichincha','CLI-003','SRV-004','Rediseño del modelo comercial para banca empresarial','Incrementar cartera empresarial en 20% en 12 meses','2024-04-01',60,35000.00,'Análisis, Diseño, Implementación','en curso','confidencial');

-- ────────────────────────────────────────────────────────────
-- PROYECTO_CONSULTORES
-- ────────────────────────────────────────────────────────────
INSERT INTO proyecto_consultores (proyecto_numero, consultor_codigo, rol, dedicacion_porcentaje) VALUES ('PRY-2024-001','CON-001','Líder de Proyecto',80);
INSERT INTO proyecto_consultores (proyecto_numero, consultor_codigo, rol, dedicacion_porcentaje) VALUES ('PRY-2024-001','CON-003','Consultor de Apoyo',40);
INSERT INTO proyecto_consultores (proyecto_numero, consultor_codigo, rol, dedicacion_porcentaje) VALUES ('PRY-2024-002','CON-002','Líder de Proyecto',100);
INSERT INTO proyecto_consultores (proyecto_numero, consultor_codigo, rol, dedicacion_porcentaje) VALUES ('PRY-2024-003','CON-005','Líder de Proyecto',60);
INSERT INTO proyecto_consultores (proyecto_numero, consultor_codigo, rol, dedicacion_porcentaje) VALUES ('PRY-2024-003','CON-002','Consultor Finanzas',40);

-- ────────────────────────────────────────────────────────────
-- PROPUESTAS
-- ────────────────────────────────────────────────────────────
INSERT INTO propuestas VALUES ('PROP-2024-001','2023-12-01','CLI-001','Propuesta Transformación Digital 2024','SRV-001','Design Thinking + Lean','1 Gerente, 2 Seniors','Enero–Marzo 2024',48000.00,'50% inicio, 50% cierre',30,'aceptada');
INSERT INTO propuestas VALUES ('PROP-2024-002','2024-02-10','CLI-002','Propuesta Reestructuración Financiera','SRV-002','Análisis DCF + Benchmarking','1 Senior Finanzas','Marzo–Abril 2024',22000.00,'40% inicio, 60% entrega final',45,'aceptada');
INSERT INTO propuestas VALUES ('PROP-2024-003','2024-03-15','CLI-003','Propuesta Estrategia Comercial','SRV-004','CRM + Design Thinking','1 Gerente, 1 Senior','Abril–Junio 2024',35000.00,'30% inicio, 40% avance, 30% cierre',30,'aceptada');
INSERT INTO propuestas VALUES ('PROP-2024-004','2024-05-01','CLI-004','Propuesta Gestión del Talento MSP','SRV-003','Assessment Center','2 Seniors RRHH','Junio–Agosto 2024',25000.00,'50% inicio, 50% cierre',60,'en evaluación');

-- ────────────────────────────────────────────────────────────
-- FASES
-- ────────────────────────────────────────────────────────────
INSERT INTO fases VALUES ('FASE-001','PRY-2024-001','Diagnóstico AS-IS','Levantamiento y análisis de procesos actuales','2024-01-15','2024-01-15','2024-02-15','2024-02-14','CON-001','ENT-001',160,'Acceso a sistemas cliente',NULL,100);
INSERT INTO fases VALUES ('FASE-002','PRY-2024-001','Diseño TO-BE','Definición de arquitectura de procesos futuros','2024-02-15','2024-02-16','2024-03-15',NULL,'CON-001','ENT-002',120,'Talleres con equipo cliente','FASE-001',60);
INSERT INTO fases VALUES ('FASE-003','PRY-2024-002','Diagnóstico Financiero','Levantamiento de estructura financiera actual','2024-03-01','2024-03-01','2024-03-20','2024-03-18','CON-002',NULL,80,'Acceso a estados financieros',NULL,100);
INSERT INTO fases VALUES ('FASE-004','PRY-2024-002','Modelado Financiero','Construcción del modelo de reestructuración','2024-03-21','2024-03-21','2024-04-10',NULL,'CON-002',NULL,100,'Software financiero','FASE-003',40);

-- ────────────────────────────────────────────────────────────
-- ENTREGABLES
-- ────────────────────────────────────────────────────────────
INSERT INTO entregables VALUES ('ENT-001','PRY-2024-001','FASE-001','Informe de Diagnóstico AS-IS','informe','Análisis detallado de procesos actuales con brechas identificadas','CON-001','CON-003','2024-02-15','2024-02-14','aprobado','2.1',TRUE);
INSERT INTO entregables VALUES ('ENT-002','PRY-2024-001','FASE-002','Arquitectura de Procesos TO-BE','modelo','Modelo objetivo de procesos digitalizados con flujos BPMN','CON-001',NULL,'2024-03-15',NULL,'en revisión','1.0',FALSE);
INSERT INTO entregables VALUES ('ENT-003','PRY-2024-002','FASE-003','Diagnóstico Financiero','informe','Análisis de estructura de capital, liquidez y rentabilidad','CON-002',NULL,'2024-03-20','2024-03-18','aprobado','1.0',TRUE);

-- ────────────────────────────────────────────────────────────
-- HORAS TRABAJADAS
-- ────────────────────────────────────────────────────────────
INSERT INTO horas_trabajadas (consultor_codigo,proyecto_numero,fecha,actividad_realizada,horas_dedicadas,lugar,descripcion_detallada,resultados_obtenidos,dificultades,horas_facturables) VALUES ('CON-001','PRY-2024-001','2024-01-20','Entrevistas con gerencias',8,'cliente','Sesiones de levantamiento con 5 gerentes de área','Mapeo completo del proceso de ventas','Disponibilidad limitada del equipo cliente',8);
INSERT INTO horas_trabajadas (consultor_codigo,proyecto_numero,fecha,actividad_realizada,horas_dedicadas,lugar,descripcion_detallada,resultados_obtenidos,dificultades,horas_facturables) VALUES ('CON-001','PRY-2024-001','2024-01-22','Análisis documental',6,'oficina','Revisión de manuales de procesos y políticas internas','Identificación de 12 brechas críticas',NULL,6);
INSERT INTO horas_trabajadas (consultor_codigo,proyecto_numero,fecha,actividad_realizada,horas_dedicadas,lugar,descripcion_detallada,resultados_obtenidos,dificultades,horas_facturables) VALUES ('CON-003','PRY-2024-001','2024-01-23','Encuesta de clima organizacional',4,'cliente','Aplicación de encuesta a 45 colaboradores','Tasa de respuesta del 89%',NULL,4);
INSERT INTO horas_trabajadas (consultor_codigo,proyecto_numero,fecha,actividad_realizada,horas_dedicadas,lugar,descripcion_detallada,resultados_obtenidos,dificultades,horas_facturables) VALUES ('CON-002','PRY-2024-002','2024-03-05','Revisión estados financieros',6,'remoto','Análisis de balances 2021-2023','Identificación de ratio deuda/patrimonio crítico',NULL,6);
INSERT INTO horas_trabajadas (consultor_codigo,proyecto_numero,fecha,actividad_realizada,horas_dedicadas,lugar,descripcion_detallada,resultados_obtenidos,dificultades,horas_facturables) VALUES ('CON-002','PRY-2024-002','2024-03-08','Reunión con directivos',4,'cliente','Presentación de hallazgos preliminares','Validación de datos con equipo financiero',NULL,4);

-- ────────────────────────────────────────────────────────────
-- FACTURAS
-- ────────────────────────────────────────────────────────────
INSERT INTO facturas VALUES ('FAC-2024-001','2024-02-28','CLI-001','PRY-2024-001','2024-01-15','2024-02-28','Fase 1: Diagnóstico AS-IS — Honorarios profesionales',24000.00,350.00,0,2914.00,'Contado 30 días','pagada');
INSERT INTO facturas VALUES ('FAC-2024-002','2024-03-31','CLI-002','PRY-2024-002','2024-03-01','2024-03-31','Fase 1: Diagnóstico Financiero — Honorarios profesionales',8800.00,150.00,0,1067.00,'Contado 30 días','pagada');
INSERT INTO facturas VALUES ('FAC-2024-003','2024-04-30','CLI-001','PRY-2024-001','2024-03-01','2024-04-30','Fase 2: Diseño TO-BE — Honorarios profesionales',24000.00,200.00,0,2914.00,'Contado 30 días','enviada');
INSERT INTO facturas VALUES ('FAC-2024-004','2024-05-15','CLI-003','PRY-2024-003','2024-04-01','2024-05-15','Avance 30%: Análisis Comercial — Honorarios profesionales',10500.00,0.00,0,1260.00,'Contado 15 días','emitida');

-- ────────────────────────────────────────────────────────────
-- CONOCIMIENTO
-- ────────────────────────────────────────────────────────────
INSERT INTO conocimiento VALUES ('CON-K-001','Metodología de Diagnóstico Digital para PYMES','metodología','Tecnología / Transversal','CON-001','2024-02-28','Framework probado para evaluación de madurez digital en empresas medianas ecuatorianas','transformación digital, diagnóstico, madurez, PYME','metodologia_diagnostico_digital_v2.pdf','interno','alto');
INSERT INTO conocimiento VALUES ('CON-K-002','Herramienta de Valoración Rápida de Empresas','herramienta','Finanzas / Transversal','CON-002','2024-03-10','Modelo Excel para valoración DCF y múltiplos en PYMES y empresas medianas','valoración, DCF, múltiplos, finanzas','herramienta_valoracion_v3.xlsx','restringido','alto');
INSERT INTO conocimiento VALUES ('CON-K-003','Caso de Estudio: Transformación Digital TechCorp','caso de estudio','Tecnología','CON-001','2024-06-30','Documentación del proceso de transformación digital con resultados y lecciones aprendidas','transformación digital, caso de éxito, tecnología','caso_techcorp_2024.pdf','interno','alto');
INSERT INTO conocimiento VALUES ('CON-K-004','Guía de Gestión por Competencias','metodología','Recursos Humanos / Transversal','CON-003','2024-04-15','Framework para implementación de modelo de gestión por competencias en empresas medianas','competencias, talento humano, evaluación 360','guia_competencias_v1.pdf','público','medio');
