class Servicio:
    def __init__(self, codigo, nombre_comercial, categoria=None, descripcion=None,
                 entregables_tipicos=None, duracion_estimada=None, metodologia=None,
                 beneficios_cliente=None, equipo_minimo=None, tarifario_referencial=None,
                 casos_exito=None):
        self.codigo                = codigo
        self.nombre_comercial      = nombre_comercial
        self.categoria             = categoria
        self.descripcion           = descripcion
        self.entregables_tipicos   = entregables_tipicos
        self.duracion_estimada     = duracion_estimada
        self.metodologia           = metodologia
        self.beneficios_cliente    = beneficios_cliente
        self.equipo_minimo         = equipo_minimo
        self.tarifario_referencial = tarifario_referencial
        self.casos_exito           = casos_exito

    def __str__(self):
        return f"[{self.codigo}] {self.nombre_comercial} — {self.categoria} — ${self.tarifario_referencial}"