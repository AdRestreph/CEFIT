# TALLER
## Ejercicio 21

El centro de convenciones "Espacios Magníficos S.A." necesita un sistema para gestionar sus instalaciones y eventos. 

1. Cada recinto se registra con código único, nombre, tipo (salón, auditorio, sala de reuniones), ubicación dentro del complejo, dimensiones, capacidad según configuración (teatro, escuela, banquete), características técnicas, tarifas por hora/día y disponibilidad.

2. Los equipamientos incluyen código de inventario, tipo (audiovisual, mobiliario, decoración), descripción detallada, cantidad disponible, estado, ubicación de almacenamiento, valor de reposición, vida útil estimada y mantenimiento requerido.

3. Los servicios ofrecidos tienen código, nombre, categoría (catering, decoración, técnico, seguridad), descripción, proveedor interno/externo, condiciones de contratación, precio base, unidad de facturación (hora, persona, evento) y plazo mínimo de solicitud.

4. Los clientes se identifican con código único, tipo (corporativo, agencia, particular), razón social o nombre, documento fiscal, dirección, teléfono, correo electrónico, persona de contacto, eventos anteriores realizados, clasificación por volumen y condiciones especiales acordadas.

5. Los eventos programados documentan número único, título, tipo (congreso, boda, feria, concierto), cliente, fecha y hora inicio, fecha y hora fin, recintos reservados, montaje solicitado, número estimado de asistentes, servicios contratados, presupuesto aprobado, estado actual y responsable interno.

6. Las cotizaciones incluyen número secuencial, fecha de emisión, validez, cliente, evento propuesto, recintos sugeridos, servicios incluidos, detalle de costos, condiciones de pago, requisitos de confirmación, descuentos aplicables y observaciones.

7. Los contratos de eventos tienen número, fecha de firma, cliente, evento, condiciones generales, desglose de servicios, cronograma de pagos, políticas de cancelación, penalizaciones, cláusulas especiales, anexos y firmas autorizadas.

8. La planificación detalla código de evento, cronograma de actividades, horarios específicos, recintos y su configuración por franja horaria, necesidades técnicas, servicios de catering con horarios y menús, personal asignado y observaciones particulares.

9. El personal para eventos incluye código de empleado, nombres, apellidos, especialidad (coordinador, técnico, camarero, seguridad), disponibilidad por fechas, eventos asignados, horario asignado, responsabilidades específicas y tarifa aplicable.

10. Las evaluaciones post-evento documentan código, evento, fecha de evaluación, aspectos valorados, puntuación obtenida, comentarios del cliente, incidencias reportadas, lecciones aprendidas y recomendaciones para futuros eventos.

# INSTRUCCIONES GENERALES
 
##Crear modelo Entidad-Relación: 
•	Identificar correctamente entidades, atributos y relaciones
•	Determinar cardinalidades (1:1, 1:M, N:M)
•	Diseñar el diagrama E-R de forma clara y completa

##Implementar eliminación en cascada: 
•	Identificar relaciones padre-hijo donde sea apropiado aplicar ON DELETE CASCADE
•	Implementar la restricción ON DELETE CASCADE en las claves foráneas relevantes

##Definir índices apropiados: 
•	Crear índices simples para columnas frecuentemente buscadas
•	Crear índices compuestos para búsquedas combinadas
•	Crear índices únicos para campos que no deben duplicarse
•	Crear índices de texto completo donde sea aplicable

##Implementar consultas con WHERE: 
•	Filtrar utilizando operadores de comparación (=, <>, >, <, >=, <=)
•	Combinar condiciones con operadores lógicos (AND, OR, NOT)
•	Usar operadores especiales (BETWEEN, IN, LIKE, IS NULL)

##Crear consultas con ORDER BY: 
•	Ordenar resultados por campos relevantes
•	Implementar ordenamiento ascendente y descendente
•	Ordenar por múltiples campos

##Aplicar funciones de agregación: 
•	Utilizar MIN/MAX para valores extremos
•	Emplear COUNT para conteos de registros
•	Implementar AVG para promedios
•	Usar SUM para totales

##Incorporar LIMIT en consultas: 
•	Restringir número de resultados
•	Implementar paginación

##Manejar valores NULL: 
•	Definir campos que permitan o no valores nulos
•	Filtrar por campos nulos/no nulos
•	Usar funciones COALESCE/IFNULL cuando sea apropiado
  
##Aplicar búsquedas con LIKE: 
•	Buscar patrones en campos de texto
•	Utilizar comodines % y _ adecuadamente

##Utilizar operador IN: 
•	Filtrar por listas de valores
•	Crear subconsultas con IN

##Implementar funciones de fecha: 
•	Extraer componentes de fechas
•	Realizar cálculos entre fechas
•	Agrupar por períodos de tiempo

##Crear consultas combinadas: 
•	Combinar múltiples operadores y funciones
•	Crear consultas jerárquicas

