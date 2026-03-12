class Proyecto:
    def __init__(self, numero, titulo, cliente_codigo=None, servicio_codigo=None,
                 alcance=None, objetivos=None, fecha_inicio=None,
                 duracion_prevista_dias=None, presupuesto_aprobado=None,
                 fases_principales=None, estado=None, nivel_confidencialidad=None):
        self.numero                 = numero
        self.titulo                 = titulo
        self.cliente_codigo         = cliente_codigo
        self.servicio_codigo        = servicio_codigo
        self.alcance                = alcance
        self.objetivos              = objetivos
        self.fecha_inicio           = fecha_inicio
        self.duracion_prevista_dias = duracion_prevista_dias
        self.presupuesto_aprobado   = presupuesto_aprobado
        self.fases_principales      = fases_principales
        self.estado                 = estado
        self.nivel_confidencialidad = nivel_confidencialidad

    def __str__(self):
        return f"[{self.numero}] {self.titulo} — {self.estado} — ${self.presupuesto_aprobado}"