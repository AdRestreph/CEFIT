import os
import shutil
from models.cliente import Cliente

CARPETA_IMAGENES = os.path.join(os.path.dirname(__file__), "..", "assets", "clientes")
os.makedirs(CARPETA_IMAGENES, exist_ok=True)


class ClienteController:
    """
    Controlador para el modulo de Clientes.
    Separa la logica de negocio de la vista (ClientesView).
    """

    def __init__(self, repo):
        self.repo = repo

    # ------------------------------------------------------------------ CRUD

    def obtener_todos(self):
        """Retorna la lista completa de clientes."""
        return self.repo.select_all()

    def obtener_por_codigo(self, codigo):
        """Retorna un cliente por su codigo primario."""
        return self.repo.select_WHERE_codigo(codigo)

    def buscar(self, termino="", tipo=None, clasificacion=None):
        """
        Busca clientes por termino libre y aplica filtros opcionales
        de tipo y clasificacion.
        """
        resultados = self.repo.search(termino) if termino else self.repo.select_all()
        if tipo:
            resultados = [c for c in resultados if c.tipo == tipo]
        if clasificacion:
            resultados = [c for c in resultados if c.clasificacion_potencial == clasificacion]
        return resultados

    def crear(self, datos: dict, ruta_imagen=None):
        """Crea un nuevo cliente y gestiona su imagen si se provee."""
        cliente = self._dict_a_cliente(datos)
        self.repo.insert(cliente)
        if ruta_imagen:
            self._guardar_imagen(cliente.codigo, ruta_imagen)

    def actualizar(self, datos: dict, ruta_imagen=None):
        """Actualiza un cliente existente y gestiona su imagen."""
        cliente = self._dict_a_cliente(datos)
        self.repo.update(cliente)
        if ruta_imagen:
            self._guardar_imagen(cliente.codigo, ruta_imagen)

    def eliminar(self, codigo):
        """Elimina un cliente y su imagen asociada si existe."""
        self.repo.delete_cliente(codigo)
        self._eliminar_imagen(codigo)

    # ----------------------------------------------------------- Exportacion

    def obtener_para_exportar(self, tipo=None, clasificacion=None):
        """Retorna clientes filtrados para exportacion."""
        return self.buscar(tipo=tipo, clasificacion=clasificacion)

    # ------------------------------------------------------ Gestion imagenes

    def ruta_imagen(self, codigo):
        """Retorna la ruta de la imagen del cliente si existe, sino None."""
        for ext in [".jpg", ".png", ".gif"]:
            ruta = os.path.join(CARPETA_IMAGENES, f"{codigo}{ext}")
            if os.path.exists(ruta):
                return ruta
        return None

    def _guardar_imagen(self, codigo, ruta_origen):
        ext = os.path.splitext(ruta_origen)[1].lower()
        destino = os.path.join(CARPETA_IMAGENES, f"{codigo}{ext}")
        if ruta_origen != destino:
            shutil.copy2(ruta_origen, destino)

    def _eliminar_imagen(self, codigo):
        for ext in [".jpg", ".png", ".gif"]:
            ruta = os.path.join(CARPETA_IMAGENES, f"{codigo}{ext}")
            if os.path.exists(ruta):
                os.remove(ruta)

    # ------------------------------------------------------------ Validacion

    def validar(self, datos: dict):
        """
        Valida los datos del formulario.
        Retorna (True, "") si es valido, o (False, mensaje) si hay error.
        """
        import re

        codigo = datos.get("codigo", "").strip()
        razon  = datos.get("razon_social", "").strip()
        correo = datos.get("correo_electronico", "").strip()
        tel    = datos.get("telefono", "").strip()

        if not codigo:
            return False, "El codigo es obligatorio."
        if len(codigo) < 3:
            return False, "El codigo debe tener al menos 3 caracteres."
        if not razon:
            return False, "La razon social es obligatoria."
        if len(razon) < 3:
            return False, "La razon social debe tener al menos 3 caracteres."
        if correo and not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", correo):
            return False, "El formato del correo no es valido."
        if tel and not re.match(r"^[\d\+\-\(\)\s]+$", tel):
            return False, "El telefono solo puede contener numeros y + - ( )"
        return True, ""

    # ---------------------------------------------------------- Helpers

    def _dict_a_cliente(self, datos: dict) -> Cliente:
        return Cliente(
            codigo=datos.get("codigo"),
            tipo=datos.get("tipo"),
            razon_social=datos.get("razon_social"),
            sector_actividad=datos.get("sector_actividad") or None,
            ruc=datos.get("ruc") or None,
            direccion=datos.get("direccion") or None,
            telefono=datos.get("telefono") or None,
            sitio_web=datos.get("sitio_web") or None,
            contacto_principal=datos.get("contacto_principal") or None,
            cargo_contacto=datos.get("cargo_contacto") or None,
            correo_electronico=datos.get("correo_electronico") or None,
            telefono_directo=datos.get("telefono_directo") or None,
            fecha_primera_relacion=datos.get("fecha_primera_relacion"),
            origen_contacto=datos.get("origen_contacto") or None,
            clasificacion_potencial=datos.get("clasificacion_potencial") or None,
        )
