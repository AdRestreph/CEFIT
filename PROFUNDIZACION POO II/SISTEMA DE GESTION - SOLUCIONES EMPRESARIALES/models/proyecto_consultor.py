class ProyectoConsultor:
    def __init__(self, proyecto_numero, consultor_codigo, rol=None,
                 dedicacion_porcentaje=None, id=None):
        self.id                   = id
        self.proyecto_numero      = proyecto_numero
        self.consultor_codigo     = consultor_codigo
        self.rol                  = rol
        self.dedicacion_porcentaje = dedicacion_porcentaje

    def __str__(self):
        return f"[{self.proyecto_numero}] {self.consultor_codigo} — {self.rol} — {self.dedicacion_porcentaje}%"