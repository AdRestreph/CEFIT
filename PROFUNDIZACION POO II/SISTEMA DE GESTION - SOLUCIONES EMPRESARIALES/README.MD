# Sistema de Gestion — Soluciones Empresariales (MVC)

## Arquitectura

Este proyecto sigue el patron **MVC (Modelo — Vista — Controlador)**.

```
mvc_proyecto/
│
├── main.py                         # Punto de entrada
│
├── database/
│   └── connection.py               # Conexion MySQL (sin cambios)
│
├── models/                         # M — Modelo (sin cambios)
│   ├── cliente.py
│   ├── consultor.py
│   ├── servicio.py
│   ├── factura.py
│   └── ...
│
├── repositories/                   # Acceso a datos via Stored Procedures (sin cambios)
│   ├── cliente_repository.py
│   ├── consultor_repository.py
│   └── ...
│
├── controllers/                    # C — Controlador (NUEVA CAPA)
│   ├── cliente_controller.py       # Logica de negocio: buscar, validar, CRUD, imagenes
│   ├── consultor_controller.py
│   ├── servicio_controller.py
│   └── factura_controller.py
│
└── views/                          # V — Vista (refactorizada)
    ├── ventana_principal.py        # Navegacion y tema; crea controllers
    ├── clientes_view.py            # Solo UI, llama al controller
    ├── consultores_view.py
    ├── servicios_view.py
    ├── facturas_view.py
    └── dialogs/
        ├── cliente_form_dialog.py      # Formulario nuevo/editar cliente
        ├── consultor_form_dialog.py
        ├── servicio_form_dialog.py
        ├── factura_form_dialog.py
        └── filtro_exportacion_dialog.py  # Dialogo reutilizable de filtros
```

## Que cambia respecto al original

| Antes | Ahora |
|-------|-------|
| `ui/modulos/clientes_widget.py` mezclaba UI + logica + validacion | `views/clientes_view.py` solo maneja UI |
| Validacion de correo/telefono dentro del widget | `ClienteController.validar()` |
| Busqueda y filtros dentro del widget | `ClienteController.buscar()` |
| Gestion de imagenes dentro del widget | `ClienteController.ruta_imagen/guardar/eliminar` |
| `main.py` pasaba repos directamente a las vistas | `VentanaPrincipal` crea controllers; vistas no ven repos |
| `DialogoFiltroExportacion` duplicado en cada widget | Un solo `filtro_exportacion_dialog.py` reutilizable |

## Flujo de datos

```
main.py
  └─ crea repos
       └─ VentanaPrincipal(repos)
             └─ crea Controllers(repo)
                   └─ crea Views(controller)
                         │
                    [evento usuario]
                         │
                    View._buscar()
                         └─> Controller.buscar()
                                  └─> Repository.search()
                                           └─> DB (Stored Procedure)
                                  <── lista de Models ──┘
                         <── lista de Models ──┘
                    View._cargar_datos(lista)
```

## Instalacion y ejecucion

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar base de datos
# Editar .env con tus credenciales MySQL

# 3. Crear la base de datos (si no existe)
# Ejecutar Config/Query/01_crear_base_datos.sql
# Ejecutar Config/Query/02_stored_procedures.sql
# Ejecutar Config/Query/03_datos_ejemplo.sql  (opcional)

# 4. Ejecutar
python main.py
```

## Agregar un nuevo modulo

1. El **Model** ya existe en `models/`.
2. El **Repository** ya existe en `repositories/`.
3. Crear `controllers/nuevo_controller.py` con metodos: `obtener_todos`, `obtener_por_codigo`, `buscar`, `crear`, `actualizar`, `eliminar`, `validar`.
4. Crear `views/nuevo_view.py` que reciba el controller en `__init__`.
5. Crear `views/dialogs/nuevo_form_dialog.py` para el formulario.
6. Registrar en `VentanaPrincipal._crear_controllers()` y en la lista `modulos`.
