class Cliente:
    """Representa un registro de la tabla clientes."""

    def __init__(
        self,
        codigo,
        tipo,
        razon_social,
        sector_actividad=None,
        ruc=None,
        direccion=None,
        telefono=None,
        sitio_web=None,
        contacto_principal=None,
        cargo_contacto=None,
        correo_electronico=None,
        telefono_directo=None,
        fecha_primera_relacion=None,
        origen_contacto=None,
        clasificacion_potencial=None
    ):
        self.codigo                 = codigo
        self.tipo                   = tipo
        self.razon_social           = razon_social
        self.sector_actividad       = sector_actividad
        self.ruc                    = ruc
        self.direccion              = direccion
        self.telefono               = telefono
        self.sitio_web              = sitio_web
        self.contacto_principal     = contacto_principal
        self.cargo_contacto         = cargo_contacto
        self.correo_electronico     = correo_electronico
        self.telefono_directo       = telefono_directo
        self.fecha_primera_relacion = fecha_primera_relacion
        self.origen_contacto        = origen_contacto
        self.clasificacion_potencial= clasificacion_potencial

    def __str__(self):
        return f"[{self.codigo}] {self.razon_social} — {self.tipo} — {self.correo_electronico}"