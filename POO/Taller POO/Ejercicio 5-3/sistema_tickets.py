from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List

class Ticket(ABC):
    _contador_tickets = 1000
    """
    Clase abstracta base para todos los tipos de tickets.
    """
    def __init__(self, ruta: str, asiento: str, precio_base: float):
        self.__numero_ticket = Ticket._contador_tickets
        Ticket._contador_tickets += 1
        self.__fecha_emision = datetime.now()
        self.__ruta = ruta
        self.__asiento = asiento
        self.__precio_base = precio_base
        self._tipo_pasajero = "Genérico"
    
    # Getters para acceso controlado (ENCAPSULAMIENTO)
    @property
    def numero_ticket(self) -> int:
        return self.__numero_ticket
    
    @property
    def fecha_emision(self) -> datetime:
        return self.__fecha_emision
    
    @property
    def ruta(self) -> str:
        return self.__ruta
    
    @property
    def asiento(self) -> str:
        return self.__asiento
    
    @property
    def precio_base(self) -> float:
        return self.__precio_base
    
    @property
    def tipo_pasajero(self) -> str:
        return self._tipo_pasajero

    @abstractmethod
    def calcular_precio_final(self) -> float:
        """Calcula el precio final con descuentos específicos."""
        pass
    
    @abstractmethod
    def validar_ticket(self) -> bool:
        """Valida los requisitos específicos del ticket."""
        pass

    def imprimir_ticket(self) -> str:
        """Genera la representación impresa del ticket."""
        precio_final = self.calcular_precio_final()
        validez = "✓ VÁLIDO" if self.validar_ticket() else "✗ INVÁLIDO"
        
        ticket_str = f"""
╔═══════════════════════════════════════════════════════╗
║               TICKET DE TRANSPORTE                    ║
╠═══════════════════════════════════════════════════════╣
║ Número: #{self.__numero_ticket:04d}                            
║ Tipo: {self._tipo_pasajero:<30}
║ Fecha: {self.__fecha_emision.strftime('%d/%m/%Y %H:%M')}              
║ Ruta: {self.__ruta:<40}
║ Asiento: {self.__asiento:<35}
║ Precio Base: ${self.__precio_base:,.2f}                    
║ Precio Final: ${precio_final:,.2f}                   
║ Ahorro: ${self.__precio_base - precio_final:,.2f}                      
║ Estado: {validez:<35}
╚═══════════════════════════════════════════════════════╝
"""
        return ticket_str

    def _aplicar_descuento(self, porcentaje: float) -> float:
        """
        Metodo protegido para aplicar descuentos.
        
        Args:
            porcentaje: Porcentaje de descuento (0-100)
        
        Returns:
            Precio con descuento aplicado
        """
        descuento = self.__precio_base * (porcentaje / 100)
        return self.__precio_base - descuento


class TicketRegular(Ticket):
    """
    Ticket para pasajeros regulares sin descuento.
    Implementa HERENCIA de Ticket.
    """
    
    def __init__(self, ruta: str, asiento: str, precio_base: float, ida_vuelta: bool = False):
        super().__init__(ruta, asiento, precio_base)
        self._tipo_pasajero = "Pasajero Regular"
        self.__ida_vuelta = ida_vuelta
        self.__tarifa_normal = precio_base
    
    @property
    def ida_vuelta(self) -> bool:
        return self.__ida_vuelta
    
    def calcular_precio_final(self) -> float:
        """
        POLIMORFISMO: Implementación específica para pasajero regular.
        Ida y vuelta tiene 10% de descuento.
        """
        if self.__ida_vuelta:
            # Descuento del 10% por ida y vuelta
            return self._aplicar_descuento(10) * 2
        return self.__tarifa_normal
    
    def validar_ticket(self) -> bool:
        """POLIMORFISMO: Validación para ticket regular."""
        # Ticket regular siempre válido si fue emitido
        return True
    
    def imprimir_ticket(self) -> str:
        ticket = super().imprimir_ticket()
        tipo_viaje = "Ida y Vuelta" if self.__ida_vuelta else "Solo Ida"
        return ticket + f"║ Tipo de viaje: {tipo_viaje}\n╚═══════════════════════════════════════════════════════╝\n"


class TicketEstudiante(Ticket):
    """
    Ticket para estudiantes con 50% de descuento.
    Implementa HERENCIA de Ticket.
    """
    
    DESCUENTO_ESTUDIANTE = 50
    def __init__(self, ruta: str, asiento: str, precio_base: float, carnet_universitario: str):
        super().__init__(ruta, asiento, precio_base)
        self._tipo_pasajero = "Estudiante"
        self.__carnet_universitario = carnet_universitario
        self.__descuento_50 = self.DESCUENTO_ESTUDIANTE
    
    @property
    def carnet_universitario(self) -> str:
        # Retorna carnet parcialmente oculto (ENCAPSULAMIENTO)
        return f"***{self.__carnet_universitario[-4:]}"
    
    def calcular_precio_final(self) -> float:
        """POLIMORFISMO: Aplica 50% de descuento estudiantil."""
        return self._aplicar_descuento(self.__descuento_50)
    
    def validar_ticket(self) -> bool:
        """POLIMORFISMO: Valida que el carnet tenga formato correcto."""
        # Validar que el carnet tenga al menos 6 caracteres
        return len(self.__carnet_universitario) >= 6
    
    def imprimir_ticket(self) -> str:
        ticket = super().imprimir_ticket()
        return ticket + f"║ Carnet: {self.carnet_universitario}\n║ Descuento: {self.__descuento_50}%\n╚═══════════════════════════════════════════════════════╝\n"


class TicketAdultoMayor(Ticket):
    """
    Ticket para adultos mayores con 30% de descuento.
    Implementa HERENCIA de Ticket.
    """
    
    DESCUENTO_ADULTO_MAYOR = 30
    HORA_INICIO_ESPECIAL = 6
    HORA_FIN_ESPECIAL = 10
    
    def __init__(self, ruta: str, asiento: str, precio_base: float, 
                 cedula: str, horario_especial: bool = False):
        super().__init__(ruta, asiento, precio_base)
        self._tipo_pasajero = "Adulto Mayor"
        self.__cedula = cedula
        self.__descuento_30 = self.DESCUENTO_ADULTO_MAYOR
        self.__horario_especial = horario_especial
    
    @property
    def cedula(self) -> str:
        # Retorna cédula parcialmente oculta (ENCAPSULAMIENTO)
        return f"***{self.__cedula[-3:]}"
    
    def calcular_precio_final(self) -> float:
        """
        POLIMORFISMO: Aplica 30% de descuento para adulto mayor.
        Descuento adicional del 5% en horario especial.
        """
        descuento_total = self.__descuento_30
        if self.__horario_especial:
            descuento_total += 5
        return self._aplicar_descuento(descuento_total)
    
    def validar_ticket(self) -> bool:
        """POLIMORFISMO: Valida cédula y horario especial si aplica."""
        # Validar formato de cédula (mínimo 6 dígitos)
        cedula_valida = len(self.__cedula) >= 6 and self.__cedula.isdigit()
        
        if self.__horario_especial:
            hora_actual = self.fecha_emision.hour
            horario_valido = self.HORA_INICIO_ESPECIAL <= hora_actual <= self.HORA_FIN_ESPECIAL
            return cedula_valida and horario_valido
        
        return cedula_valida
    
    def imprimir_ticket(self) -> str:
        ticket = super().imprimir_ticket()
        horario = "Sí (6:00-10:00)" if self.__horario_especial else "No"
        descuento_total = self.__descuento_30 + (5 if self.__horario_especial else 0)
        return ticket + f"║ Cédula: {self.cedula}\n║ Horario Especial: {horario}\n║ Descuento Total: {descuento_total}%\n╚═══════════════════════════════════════════════════════╝\n"


class TicketTurista(Ticket):
    """
    Ticket para turistas con pase turístico multiviaje.
    Implementa HERENCIA de Ticket.
    """
    
    def __init__(self, ruta: str, asiento: str, precio_base: float,
                 pase_turistico: str, dias_validez: int = 7, multiviaje: bool = True):
        super().__init__(ruta, asiento, precio_base)
        self._tipo_pasajero = "Turista"
        self.__pase_turistico = pase_turistico
        self.__dias_validez = dias_validez
        self.__multiviaje = multiviaje
        self.__fecha_vencimiento = self.fecha_emision + timedelta(days=dias_validez)
    
    @property
    def pase_turistico(self) -> str:
        return self.__pase_turistico
    
    @property
    def fecha_vencimiento(self) -> datetime:
        return self.__fecha_vencimiento
    
    def calcular_precio_final(self) -> float:
        """
        POLIMORFISMO: Precio package para turistas.
        Package multiviaje tiene descuento del 20%.
        """
        if self.__multiviaje:
            return self._aplicar_descuento(20)
        return self.precio_base
    
    def validar_ticket(self) -> bool:
        """POLIMORFISMO: Valida pase turístico y vigencia."""
        # Validar formato de pase (debe empezar con 'PT-')
        pase_valido = self.__pase_turistico.startswith('PT-')
        
        # Validar que no haya vencido
        vigente = datetime.now() <= self.__fecha_vencimiento
        
        return pase_valido and vigente
    
    def imprimir_ticket(self) -> str:
        ticket = super().imprimir_ticket()
        tipo = "Multiviaje" if self.__multiviaje else "Viaje único"
        return ticket + f"║ Pase: {self.__pase_turistico}\n║ Tipo: {tipo}\n║ Válido hasta: {self.__fecha_vencimiento.strftime('%d/%m/%Y')}\n║ Días de validez: {self.__dias_validez}\n╚═══════════════════════════════════════════════════════╝\n"


class SistemaTickets:
    """
    Clase para gestionar la emisión y validación de tickets.
    Demuestra POLIMORFISMO en acción.
    """
    
    def __init__(self):
        self.__tickets_emitidos: List[Ticket] = []
    
    def emitir_ticket(self, ticket: Ticket) -> None:
        """Emite un ticket y lo agrega al sistema."""
        self.__tickets_emitidos.append(ticket)
        print(ticket.imprimir_ticket())
    
    def validar_todos_tickets(self) -> None:
        """Valida todos los tickets de forma POLIMÓRFICA."""
        print("\n" + "="*60)
        print("VALIDACIÓN DE TICKETS (POLIMORFISMO EN ACCIÓN)")
        print("="*60)
        
        for ticket in self.__tickets_emitidos:
            estado = "✓ VÁLIDO" if ticket.validar_ticket() else "✗ INVÁLIDO"
            print(f"Ticket #{ticket.numero_ticket:04d} - {ticket.tipo_pasajero}: {estado}")
    
    def calcular_ingresos_totales(self) -> float:
        """Calcula ingresos totales de forma POLIMÓRFICA."""
        total = sum(ticket.calcular_precio_final() for ticket in self.__tickets_emitidos)
        return total
    
    def generar_reporte(self) -> None:
        """Genera reporte completo del sistema."""
        print("\n" + "="*60)
        print("REPORTE FINANCIERO DEL SISTEMA")
        print("="*60)
        
        # Agrupar por tipo de pasajero
        tipos = {}
        for ticket in self.__tickets_emitidos:
            tipo = ticket.tipo_pasajero
            precio = ticket.calcular_precio_final()
            
            if tipo not in tipos:
                tipos[tipo] = {'cantidad': 0, 'ingresos': 0}
            
            tipos[tipo]['cantidad'] += 1
            tipos[tipo]['ingresos'] += precio
        
        # Imprimir reporte
        for tipo, datos in tipos.items():
            print(f"\n{tipo}:")
            print(f"  Cantidad: {datos['cantidad']} tickets")
            print(f"  Ingresos: ${datos['ingresos']:,.2f}")
        
        total = self.calcular_ingresos_totales()
        print(f"\n{'─'*60}")
        print(f"INGRESOS TOTALES: ${total:,.2f}")
        print(f"TICKETS EMITIDOS: {len(self.__tickets_emitidos)}")
        print("="*60)
