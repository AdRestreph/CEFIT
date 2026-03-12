class Propuesta:
    def __init__(self, numero, fecha_presentacion=None, cliente_codigo=None,
                 titulo=None, servicios_incluidos=None, enfoque_metodologico=None,
                 equipo_propuesto=None, cronograma_tentativo=None,
                 inversion_requerida=None, condiciones_comerciales=None,
                 validez_dias=None, estado=None):
        self.numero                 = numero
        self.fecha_presentacion     = fecha_presentacion
        self.cliente_codigo         = cliente_codigo
        self.titulo                 = titulo
        self.servicios_incluidos    = servicios_incluidos
        self.enfoque_metodologico   = enfoque_metodologico
        self.equipo_propuesto       = equipo_propuesto
        self.cronograma_tentativo   = cronograma_tentativo
        self.inversion_requerida    = inversion_requerida
        self.condiciones_comerciales = condiciones_comerciales
        self.validez_dias           = validez_dias
        self.estado                 = estado

    def __str__(self):
        return f"[{self.numero}] {self.titulo} — {self.estado} — ${self.inversion_requerida}"