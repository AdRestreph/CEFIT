class Entregable:
    def __init__(self, codigo, proyecto_numero, fase_codigo, titulo, tipo=None,
                 descripcion=None, autor_principal_codigo=None, colaboradores=None,
                 fecha_entrega_planificada=None, fecha_entrega_real=None,
                 estado_revision=None, version_actual='1.0', aprobacion_cliente=False):
        self.codigo                    = codigo
        self.proyecto_numero           = proyecto_numero
        self.fase_codigo               = fase_codigo
        self.titulo                    = titulo
        self.tipo                      = tipo
        self.descripcion               = descripcion
        self.autor_principal_codigo    = autor_principal_codigo
        self.colaboradores             = colaboradores
        self.fecha_entrega_planificada = fecha_entrega_planificada
        self.fecha_entrega_real        = fecha_entrega_real
        self.estado_revision           = estado_revision
        self.version_actual            = version_actual
        self.aprobacion_cliente        = aprobacion_cliente

    def __str__(self):
        return f"[{self.codigo}] {self.titulo} — v{self.version_actual} — {self.estado_revision}"