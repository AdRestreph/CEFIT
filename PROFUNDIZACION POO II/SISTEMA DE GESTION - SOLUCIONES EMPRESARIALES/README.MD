# PROYECTO SISTEMA DE GESTIÓN - SOLUCIONES EMPRESARIALES

## DOCUMENTACIÓN

| Archivo | Descripción |
|---|---|
| `soluciones_empresariales.sql` | Script DDL completo: tablas, relaciones, datos de ejemplo y vistas |
| `config/database.py` | Conexión centralizada a MySQL con SQLAlchemy |
| `repositories/clientes.py` | Operaciones CRUD sobre la tabla clientes |
| `repositories/proyectos.py` | Operaciones CRUD sobre la tabla proyectos y asignación de equipo |
| `repositories/horas.py` | Registro y resumen de horas trabajadas por consultor |
| `repositories/facturas.py` | Emisión y consulta de facturas por cliente y proyecto |
| `main.py` | Punto de entrada para probar la conexión y las operaciones |
| `requirements.txt` | Dependencias del proyecto |
| `.env.example` | Plantilla de variables de entorno |


## INTRODUCCIÓN AL PROYECTO

Este sistema fue desarrollado para gestionar las operaciones internas de la firma de consultoría **Soluciones Empresariales S.A.** Centraliza la información de clientes, consultores, servicios, proyectos y facturación en una base de datos relacional, con acceso desde Python a través de una capa de repositorios organizada por módulo.

El sistema cubre diez entidades principales:

- **Clientes** — registro completo con datos de empresa y contacto principal
- **Consultores** — perfil profesional, especialidades, nivel jerárquico y tarifa horaria
- **Servicios** — catálogo de servicios ofrecidos con metodología y tarifario referencial
- **Proyectos** — gestión del ciclo de vida con equipo asignado, presupuesto y estado
- **Propuestas comerciales** — seguimiento desde presentación hasta aceptación o rechazo
- **Fases y actividades** — planificación y avance de cada etapa del proyecto
- **Entregables** — control de versiones y aprobación por parte del cliente
- **Horas trabajadas** — registro diario por consultor con horas facturables
- **Facturación** — emisión y seguimiento de facturas por proyecto
- **Gestión del conocimiento** — catalogación de metodologías y casos de estudio reutilizables


## TECNOLOGÍAS

- **Python 3.11+**
- **MySQL / MariaDB**
- **SQLAlchemy 2.0** — manejo de sesiones y conexión al pool
- **PyMySQL** — driver de conexión a MySQL
- **python-dotenv** — gestión de variables de entorno
- **PyCharm** — entorno de desarrollo
- **DataGrip** — administración y consulta de la base de datos


## ESTRUCTURA DEL PROYECTO

```
soluciones_empresariales/
│
├── config/
│   └── database.py          # Engine, sesiones y verificación de conexión
│
├── repositories/            # Una función por operación, un archivo por tabla
│   ├── clientes.py
│   ├── proyectos.py
│   ├── horas.py
│   └── facturas.py
│
├── main.py                  # Punto de entrada y pruebas
├── requirements.txt         # Dependencias
├── .env                     # Credenciales reales (no subir a Git)
├── .env.example             # Plantilla de credenciales
├── .gitignore
└── README.md
```


## INSTALACIÓN Y CONFIGURACIÓN

**1. Clonar o descargar el proyecto y abrirlo en PyCharm.**

**2. Crear el entorno virtual** desde PyCharm:
`File → Settings → Project → Python Interpreter → Add → Virtualenv → New`

**3. Instalar dependencias** desde la terminal integrada de PyCharm:
```bash
pip install -r requirements.txt
```

**4. Configurar las credenciales** copiando el archivo de ejemplo:
```bash
cp .env.example .env
```
Luego editar `.env` con los datos reales de conexión a MySQL. Estos datos se encuentran en DataGrip en: `tu conexión → clic derecho → Properties → General`.

```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=soluciones_empresariales
DB_USER=root
DB_PASSWORD=tu_password
```

**5. Crear la base de datos** ejecutando el script SQL en DataGrip:
```
soluciones_empresariales.sql
```

**6. Verificar la conexión** ejecutando `main.py` desde PyCharm:
```bash
python main.py
```
Si todo está correcto verás:
```
✅ Conexión exitosa → localhost:3306/soluciones_empresariales
```


## NOTAS INTRODUCTORIAS

- El archivo `.env` contiene las credenciales de base de datos y **nunca debe subirse a Git**. Ya está incluido en `.gitignore`.
- Cada integrante debe crear su propio `.env` con sus credenciales locales.
- Cuando se agregue una nueva librería al proyecto, actualizar `requirements.txt` con:
```bash
pip freeze > requirements.txt
```
- Las consultas SQL siempre usan parámetros con `:nombre` para prevenir inyección SQL. No usar f-strings para armar queries.