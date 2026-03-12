class Conocimiento:
    def __init__(self, codigo, titulo, tipo=None, industria=None, autor_codigo=None,
                 fecha_creacion=None, descripcion=None, palabras_clave=None,
                 archivo_adjunto=None, nivel_acceso=None, potencial_reutilizacion=None):
        self.codigo                 = codigo
        self.titulo                 = titulo
        self.tipo                   = tipo
        self.industria              = industria
        self.autor_codigo           = autor_codigo
        self.fecha_creacion         = fecha_creacion
        self.descripcion            = descripcion
        self.palabras_clave         = palabras_clave
        self.archivo_adjunto        = archivo_adjunto
        self.nivel_acceso           = nivel_acceso
        self.potencial_reutilizacion = potencial_reutilizacion

    def __str__(self):
        return f"[{self.codigo}] {self.titulo} — {self.tipo} — {self.nivel_acceso}"