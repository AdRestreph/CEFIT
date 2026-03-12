class Fase:
    def __init__(self, codigo, proyecto_numero, nombre, descripcion=None,
                 fecha_inicio_planificada=None, fecha_inicio_real=None,
                 fecha_fin_planificada=None, fecha_fin_real=None,
                 responsable_codigo=None, entregables_asociados=None,
                 esfuerzo_estimado_horas=None, recursos_necesarios=None,
                 dependencias=None, porcentaje_avance=0):
        self.codigo                   = codigo
        self.proyecto_numero          = proyecto_numero
        self.nombre                   = nombre
        self.descripcion              = descripcion
        self.fecha_inicio_planificada = fecha_inicio_planificada
        self.fecha_inicio_real        = fecha_inicio_real
        self.fecha_fin_planificada    = fecha_fin_planificada
        self.fecha_fin_real           = fecha_fin_real
        self.responsable_codigo       = responsable_codigo
        self.entregables_asociados    = entregables_asociados
        self.esfuerzo_estimado_horas  = esfuerzo_estimado_horas
        self.recursos_necesarios      = recursos_necesarios
        self.dependencias             = dependencias
        self.porcentaje_avance        = porcentaje_avance

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} — {self.proyecto_numero} — {self.porcentaje_avance}%"