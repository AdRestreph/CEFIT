from models.factura import Factura


class FacturaController:
    """Controlador para el modulo de Facturas."""

    def __init__(self, repo):
        self.repo = repo

    def obtener_todos(self):
        return self.repo.select_all()

    def obtener_por_codigo(self, codigo):
        return self.repo.select_WHERE_codigo(codigo)

    def buscar(self, termino="", estado=None):
        resultados = self.repo.search(termino) if termino else self.repo.select_all()
        if estado:
            resultados = [f for f in resultados if f.estado == estado]
        return resultados

    def crear(self, datos: dict):
        factura = self._dict_a_factura(datos)
        self.repo.insert(factura)

    def actualizar(self, datos: dict):
        factura = self._dict_a_factura(datos)
        self.repo.update(factura)

    def eliminar(self, codigo):
        self.repo.delete_factura(codigo)

    def validar(self, datos: dict):
        codigo = datos.get("codigo", "").strip()
        cliente = datos.get("codigo_cliente", "").strip()
        if not codigo:
            return False, "El codigo de factura es obligatorio."
        if not cliente:
            return False, "El cliente es obligatorio."
        return True, ""

    def _dict_a_factura(self, datos: dict) -> Factura:
        return Factura(
            codigo=datos.get("codigo"),
            codigo_cliente=datos.get("codigo_cliente") or None,
            codigo_proyecto=datos.get("codigo_proyecto") or None,
            fecha_emision=datos.get("fecha_emision") or None,
            fecha_vencimiento=datos.get("fecha_vencimiento") or None,
            monto_total=datos.get("monto_total") or None,
            estado=datos.get("estado") or None,
            notas=datos.get("notas") or None,
        )
