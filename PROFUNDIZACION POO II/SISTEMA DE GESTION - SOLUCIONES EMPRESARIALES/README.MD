# Sistema de Gestión — Soluciones Empresariales

Sistema de gestión empresarial desarrollado con Python y PyQt6, conectado a MySQL mediante procedimientos almacenados. Incluye módulos de Clientes, Consultores, Servicios y Facturas con exportación a Excel y PDF, gestión de imágenes y temas visuales intercambiables.

---
## Entregables

### Video: 


### Canva (presentacion): [Presentacion soluciones empresariales PDF](assets/presentacion/presentacion_soluciones_empresariales.pptx.pdf)

---

## Requisitos del sistema

- Python 3.10 o superior
- MySQL 8.0 o superior
- PyCharm (recomendado) o cualquier editor compatible
- Windows 10/11

---
## Diagrama de casos de uso
![digrama de casos de uso.png](assets/presentacion/digrama%20de%20casos%20de%20uso.png)
---
## Estructura del proyecto

```
SISTEMA DE GESTION - SOLUCIONES EMPRESARIALES/
│
├── main.py                          ← Punto de entrada
├── .env                             ← Credenciales de BD (no subir a Git)
├── .gitignore
├── README.md
│
├── database/
│   ├── __init__.py
│   └── connection.py                ← Conexión a MySQL
│
├── models/
│   ├── __init__.py
│   ├── cliente.py
│   ├── consultor.py
│   ├── servicio.py
│   ├── factura.py
│   ├── proyecto.py
│   ├── propuesta.py
│   ├── fase.py
│   ├── entregable.py
│   ├── hora_trabajada.py
│   ├── conocimiento.py
│   └── proyecto_consultor.py
│
├── repositories/
│   ├── __init__.py
│   ├── cliente_repository.py
│   ├── consultor_repository.py
│   ├── servicio_repository.py
│   ├── factura_repository.py
│   ├── proyecto_repository.py
│   ├── propuesta_repository.py
│   ├── fase_repository.py
│   ├── entregable_repository.py
│   ├── hora_trabajada_repository.py
│   ├── conocimiento_repository.py
│   └── proyecto_consultor_repository.py
│
├── ui/
│   ├── __init__.py
│   ├── themes.py                    ← Paletas Charcoal Pro e Ivory Gold
│   ├── iconos/                    ← Íconos FontAwesome via qtawesome
│        ├── iconos.py
│   ├── ventana_principal.py         ← Ventana principal con sidebar
│   └── modulos/
│       ├── __init__.py
│       ├── clientes_widget.py
│       ├── consultores_widget.py
│       ├── servicios_widget.py
│       └── facturas_widget.py
│
└── assets/
    ├── clientes/                    ← Imágenes de clientes (auto-generada)
    └── consultores/                 ← Fotos de consultores (auto-generada)
```

---

## Instalación paso a paso

### 1. Clonar o descargar el proyecto

Descarga el proyecto y colócalo en tu directorio de trabajo.

### 2. Crear el entorno virtual

Abre la terminal en la carpeta raíz del proyecto y ejecuta:

```bash
python -m venv venv
```

Activar en Windows:
```bash
venv\Scripts\activate
```

Activar en Mac/Linux:
```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install mysql-connector-python
pip install python-dotenv
pip install PyQt6
pip install qtawesome
pip install openpyxl
pip install reportlab
pip install Pillow
```

O instalar todo de una vez si tienes el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Abre MySQL Workbench o DataGrip y ejecuta en orden:

1. `sql/01_crear_base_datos.sql` — crea las tablas
2. `sql/02_stored_procedures.sql` — crea los procedimientos almacenados
3. `sql/03_datos_ejemplo.sql` — inserta datos de prueba (opcional)

### 5. Crear el archivo `.env`

En la raíz del proyecto crea un archivo llamado `.env` con tus credenciales:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_contraseña_aqui
DB_NAME=SITEMA_DE_GESTION_SOLUCIONES_EMPRESARIALES
DB_PORT=3306
```

> ⚠️ Nunca compartas ni subas este archivo a repositorios públicos.

### 6. Configurar PyCharm

1. Abre PyCharm y selecciona **Open** → carpeta del proyecto
2. Ve a **File → Settings → Project → Python Interpreter**
3. Selecciona el intérprete del entorno virtual creado (`venv`)
4. Clic derecho en la carpeta raíz del proyecto → **Mark Directory as → Sources Root**

---

## Ejecución

Desde PyCharm, abre `main.py` y presiona el botón **Run**, o desde la terminal:

```bash
python main.py
```

Al iniciar verás en la consola:
```
✅ Conexion exitosa
```

Y se abrirá la ventana principal de la aplicación.

---

## Uso de la aplicación

### Navegación

Usa el **menú lateral izquierdo** para navegar entre módulos. El módulo activo se resalta en dorado.

### Módulos disponibles

| Módulo | Funcionalidades |
|---|---|
| Clientes | CRUD completo, búsqueda, filtros, imagen, exportar Excel/PDF |
| Consultores | CRUD completo, búsqueda, filtros, foto de perfil, exportar Excel/PDF |
| Servicios | CRUD completo, búsqueda, filtros por categoría, exportar Excel/PDF |
| Facturas | CRUD completo, búsqueda, filtros por estado y fechas, total automático, exportar Excel/PDF |

### Operaciones CRUD

- **Nuevo** — abre el formulario vacío para crear un registro
- **Editar** — selecciona una fila y haz clic para modificarla
- **Eliminar** — selecciona una fila y confirma la eliminación

> ⚠️ El sistema protege la integridad referencial. No puedes eliminar un cliente que tenga proyectos o facturas asociadas.

### Búsqueda y filtros

Escribe en el campo de búsqueda y presiona **Enter** o el botón **Buscar**. Usa los desplegables para filtrar por tipo, nivel, estado u otras categorías según el módulo. El botón **Limpiar** restablece todos los filtros.

### Exportación

1. Haz clic en **Exportar Excel** o **Exportar PDF**
2. Se abrirá un diálogo de filtros para seleccionar qué datos exportar
3. Elige la carpeta y nombre del archivo
4. El archivo se genera automáticamente con formato profesional

### Gestión de imágenes (Clientes y Consultores)

En el formulario de edición verás el panel de imagen a la derecha:

1. Haz clic en **Cargar imagen**
2. Selecciona un archivo JPG, PNG o GIF (máximo 5MB)
3. La imagen se valida automáticamente con Pillow
4. Al guardar, la imagen se copia a `assets/clientes/` o `assets/consultores/`

### Cambio de tema

En la parte inferior del sidebar hay un selector de tema:

- **Charcoal Pro** — fondo oscuro con acentos dorados (predeterminado)
- **Ivory Gold** — fondo claro en crema con detalles dorados

---

## Notas técnicas importantes

### Por qué `use_pure=True` en la conexión

En Windows, la extensión C de `mysql-connector` puede causar un crash al combinarse con PyQt6. El parámetro `use_pure=True` fuerza el uso de la implementación Python pura del conector, resolviendo este conflicto.

### Procedimientos almacenados

Todas las operaciones CRUD se realizan a través de procedimientos almacenados en MySQL. Esto significa que la aplicación **nunca ejecuta SQL directo** sobre las tablas, protegiendo la integridad de los datos y facilitando auditorías.

### Arquitectura

El proyecto usa una arquitectura **monolítica en capas**:

```
UI (PyQt6)
    └─► Repositories (llaman SPs)
            └─► MySQL (SPs operan sobre tablas)
```

Cada capa tiene una responsabilidad única y no se mezclan entre sí.

---

## Dependencias

```
mysql-connector-python
python-dotenv
PyQt6
qtawesome
openpyxl
reportlab
Pillow
```

---

## Autor
Andres David Restrepo Hernandez
Desarrollado como proyecto académico de profundización en Programación Orientada a Objetos II — CEFIT, 2026.