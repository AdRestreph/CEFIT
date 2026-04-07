from models.consultor import Consultor


class ConsultorController:
    """
    Controlador para el modulo de Consultores.
    """

    def __init__(self, repo):
        self.repo = repo

    def obtener_todos(self):
        return self.repo.select_all()

    def obtener_por_codigo(self, codigo):
        return self.repo.select_WHERE_codigo(codigo)

    def buscar(self, termino="", nivel=None, disponibilidad=None):
        resultados = self.repo.search(termino) if termino else self.repo.select_all()
        if nivel:
            resultados = [c for c in resultados if c.nivel == nivel]
        if disponibilidad:
            resultados = [c for c in resultados if c.disponibilidad == disponibilidad]
        return resultados

    def crear(self, datos: dict):
        consultor = self._dict_a_consultor(datos)
        self.repo.insert(consultor)

    def actualizar(self, datos: dict):
        consultor = self._dict_a_consultor(datos)
        self.repo.update(consultor)

    def eliminar(self, codigo):
        self.repo.delete_consultor(codigo)

    def validar(self, datos: dict):
        codigo   = datos.get("codigo_empleado", "").strip()
        nombres  = datos.get("nombres", "").strip()
        apellidos = datos.get("apellidos", "").strip()

        if not codigo:
            return False, "El codigo de empleado es obligatorio."
        if len(codigo) < 3:
            return False, "El codigo debe tener al menos 3 caracteres."
        if not nombres:
            return False, "Los nombres son obligatorios."
        if not apellidos:
            return False, "Los apellidos son obligatorios."
        return True, ""

    def _dict_a_consultor(self, datos: dict) -> Consultor:
        return Consultor(
            codigo_empleado=datos.get("codigo_empleado"),
            nombres=datos.get("nombres"),
            apellidos=datos.get("apellidos"),
            documento_identidad=datos.get("documento_identidad") or None,
            formacion_academica=datos.get("formacion_academica") or None,
            certificaciones=datos.get("certificaciones") or None,
            especialidades=datos.get("especialidades") or None,
            anios_experiencia=datos.get("anios_experiencia") or None,
            nivel=datos.get("nivel") or None,
            tarifa_horaria=datos.get("tarifa_horaria") or None,
            idiomas=datos.get("idiomas") or None,
            disponibilidad=datos.get("disponibilidad") or None,
        )
