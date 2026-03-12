class Consultor:
    def __init__(self, codigo_empleado, nombres, apellidos, documento_identidad=None,
                 formacion_academica=None, certificaciones=None, especialidades=None,
                 anios_experiencia=None, nivel=None, tarifa_horaria=None,
                 idiomas=None, disponibilidad=None):
        self.codigo_empleado     = codigo_empleado
        self.nombres             = nombres
        self.apellidos           = apellidos
        self.documento_identidad = documento_identidad
        self.formacion_academica = formacion_academica
        self.certificaciones     = certificaciones
        self.especialidades      = especialidades
        self.anios_experiencia   = anios_experiencia
        self.nivel               = nivel
        self.tarifa_horaria      = tarifa_horaria
        self.idiomas             = idiomas
        self.disponibilidad      = disponibilidad

    def __str__(self):
        return f"[{self.codigo_empleado}] {self.nombres} {self.apellidos} — {self.nivel} — {self.disponibilidad}"