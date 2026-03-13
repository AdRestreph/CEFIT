class Factura:
    def __init__(self, numero_factura, fecha, cliente_codigo=None, proyecto_numero=None,
                 periodo_inicio=None, periodo_fin=None, servicios_prestados=None,
                 honorarios=0, gastos_reembolsables=0, descuentos=0,
                 impuestos=0, condiciones_pago=None, estado=None):
        self.numero_factura      = numero_factura
        self.fecha               = fecha
        self.cliente_codigo      = cliente_codigo
        self.proyecto_numero     = proyecto_numero
        self.periodo_inicio      = periodo_inicio
        self.periodo_fin         = periodo_fin
        self.servicios_prestados = servicios_prestados
        self.honorarios          = honorarios
        self.gastos_reembolsables = gastos_reembolsables
        self.descuentos          = descuentos
        self.impuestos           = impuestos
        self.condiciones_pago    = condiciones_pago
        self.estado              = estado

    def __str__(self):
        return f"[{self.numero_factura}] {self.cliente_codigo} — ${self.honorarios} — {self.estado}"