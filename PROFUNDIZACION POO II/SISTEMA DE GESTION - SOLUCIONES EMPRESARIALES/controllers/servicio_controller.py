from models.servicio import Servicio


class ServicioController:
    """Controlador para el modulo de Servicios."""

    def __init__(self, repo):
        self.repo = repo

    def obtener_todos(self):
        return self.repo.select_all()

    def obtener_por_codigo(self, codigo):
        return self.repo.select_WHERE_codigo(codigo)

    def buscar(self, termino="", tipo=None, estado=None):
        resultados = self.repo.search(termino) if termino else self.repo.select_all()
        if tipo:
            resultados = [s for s in resultados if s.tipo == tipo]
        if estado:
            resultados = [s for s in resultados if s.estado == estado]
        return resultados

    def crear(self, datos: dict):
        servicio = self._dict_a_servicio(datos)
        self.repo.insert(servicio)

    def actualizar(self, datos: dict):
        servicio = self._dict_a_servicio(datos)
        self.repo.update(servicio)

    def eliminar(self, codigo):
        self.repo.delete_servicio(codigo)

    def validar(self, datos: dict):
        codigo = datos.get("codigo", "").strip()
        nombre = datos.get("nombre", "").strip()
        if not codigo:
            return False, "El codigo es obligatorio."
        if not nombre:
            return False, "El nombre del servicio es obligatorio."
        return True, ""

    def _dict_a_servicio(self, datos: dict) -> Servicio:
        return Servicio(
            codigo=datos.get("codigo"),
            nombre=datos.get("nombre"),
            tipo=datos.get("tipo") or None,
            descripcion=datos.get("descripcion") or None,
            precio_base=datos.get("precio_base") or None,
            unidad_cobro=datos.get("unidad_cobro") or None,
            estado=datos.get("estado") or None,
        )
