class HoraTrabajada:
    def __init__(self, consultor_codigo, proyecto_numero, fecha, horas_dedicadas,
                 actividad_realizada=None, lugar=None, descripcion_detallada=None,
                 resultados_obtenidos=None, dificultades=None,
                 horas_facturables=None, id=None):
        self.id                   = id
        self.consultor_codigo     = consultor_codigo
        self.proyecto_numero      = proyecto_numero
        self.fecha                = fecha
        self.actividad_realizada  = actividad_realizada
        self.horas_dedicadas      = horas_dedicadas
        self.lugar                = lugar
        self.descripcion_detallada = descripcion_detallada
        self.resultados_obtenidos = resultados_obtenidos
        self.dificultades         = dificultades
        self.horas_facturables    = horas_facturables

    def __str__(self):
        return f"[{self.id}] {self.consultor_codigo} — {self.fecha} — {self.horas_dedicadas}h — {self.lugar}"