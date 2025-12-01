import abc
from datetime import datetime

class Ticket(abc.ABC):
    """
    Clase abstracta que define la plantilla para cualquier ticket de viaje.
    - Abstracción: Define interfaces obligatorias.
    - Encapsulamiento: Protege datos sensibles del ticket.
    """

    def __init__(self, numero_ticket, ruta, asiento, precio_base):
        # Validación básica de datos de entrada
        if not numero_ticket or not isinstance(numero_ticket, str):
            raise ValueError("El número de ticket es inválido.")
        if precio_base < 0:
            raise ValueError("El precio base no puede ser negativo.")

        # Atributos Privados (Encapsulamiento Fuerte)
        self.__numero_ticket = numero_ticket
        self.__fecha_emision = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__ruta = ruta
        self.__asiento = asiento
        self.__precio_base = precio_base

        # Atributo Protegido (Accesible por subclases)
        self._tipo_pasajero = "Genérico"

    # Getters para atributos privados necesarios para lectura
    @property
    def numero_ticket(self):
        return self.__numero_ticket

    @property
    def precio_base(self):
        return self.__precio_base

    @property
    def ruta(self):
        return self.__ruta

    def imprimir_ticket(self):
        """Metodo concreto que imprime los detalles básicos del ticket."""
        # Llama a __str__ implícitamente
        print(self)

    # Métodos Abstractos (Contrato para las subclases)
    @abc.abstractmethod
    def calcular_precio_final(self):
        """Debe retornar el precio float final tras aplicar reglas de negocio."""
        pass

    @abc.abstractmethod
    def validar_ticket(self):
        """Debe retornar bool indicando si el ticket cumple requisitos para viajar."""
        pass

    def __str__(self):
        return (f"[{self.__numero_ticket}] Pasajero: {self._tipo_pasajero} | "
                f"Ruta: {self.__ruta} | Asiento: {self.__asiento}")


class TicketRegular(Ticket):
    """
    Ticket para pasajeros sin descuentos especiales.
    Puede ser ida y vuelta.
    """

    def __init__(self, numero_ticket, ruta, asiento, precio_base, ida_vuelta=False):
        super().__init__(numero_ticket, ruta, asiento, precio_base)
        self._tipo_pasajero = "Regular"
        self.__ida_vuelta = ida_vuelta

    # Metodo privado para cálculos internos (Encapsulamiento)
    def __calcular_recargo_retorno(self):
        # Si es ida y vuelta, cobramos el doble pero con un 10% de descuento global
        if self.__ida_vuelta:
            return (self.precio_base * 2) * 0.90
        return self.precio_base

    # POLIMORFISMO
    def calcular_precio_final(self):
        return self.__calcular_recargo_retorno()

    # POLIMORFISMO
    def validar_ticket(self):
        # El ticket regular siempre es válido si se pagó
        return True

    def __str__(self):
        tipo_viaje = "Ida y Vuelta" if self.__ida_vuelta else "Solo Ida"
        return super().__str__() + f" | Tipo: {tipo_viaje}"


class TicketEstudiante(Ticket):
    """
    Ticket con 50% de descuento. Requiere carnet.
    """

    def __init__(self, numero_ticket, ruta, asiento, precio_base, carnet_universitario):
        super().__init__(numero_ticket, ruta, asiento, precio_base)
        self._tipo_pasajero = "Estudiante"
        self.__carnet_universitario = carnet_universitario
        self.__descuento_50 = 0.50

    # Metodo privado requerido (Encapsulamiento)
    def __aplicar_descuento(self):
        return self.precio_base * (1 - self.__descuento_50)

    # POLIMORFISMO
    def calcular_precio_final(self):
        return self.__aplicar_descuento()

    # POLIMORFISMO
    def validar_ticket(self):
        # Valida que exista un carnet registrado
        if self.__carnet_universitario and len(self.__carnet_universitario) > 3:
            return True
        print(f"ERROR: Ticket {self.numero_ticket} inválido (Carnet nulo o muy corto).")
        return False

    def __str__(self):
        return super().__str__() + f" | Carnet: {self.__carnet_universitario}"


class TicketAdultoMayor(Ticket):
    """
    Ticket con 30% de descuento. Restricción de horario.
    """

    def __init__(self, numero_ticket, ruta, asiento, precio_base, cedula, horario_especial=False):
        super().__init__(numero_ticket, ruta, asiento, precio_base)
        self._tipo_pasajero = "Adulto Mayor"
        self.__cedula = cedula
        self.__descuento_30 = 0.30
        self.__horario_especial = horario_especial  # True si viaja en horas pico (sin descuento extra)

    # Metodo privado (Encapsulamiento)
    def __aplicar_descuento(self):
        # Si viaja en horario especial (pico), el descuento es menor (ej. 10%)
        descuento = 0.10 if self.__horario_especial else self.__descuento_30
        return self.precio_base * (1 - descuento)

    # POLIMORFISMO
    def calcular_precio_final(self):
        return self.__aplicar_descuento()

    # POLIMORFISMO
    def validar_ticket(self):
        # Valida que la cédula sea numérica y válida
        if self.__cedula.isdigit() and len(self.__cedula) >= 6:
            return True
        print(f"ERROR: Ticket {self.numero_ticket} inválido (Cédula incorrecta).")
        return False

    def __str__(self):
        nota = "Horario Pico" if self.__horario_especial else "Horario Valle"
        return super().__str__() + f" | Doc: {self.__cedula} ({nota})"


class TicketTurista(Ticket):
    """
    Ticket tipo 'Pase'. Multiviaje incrementa precio base.
    """

    def __init__(self, numero_ticket, ruta, asiento, precio_base, pase_turistico, multiviaje=False):
        super().__init__(numero_ticket, ruta, asiento, precio_base)
        self._tipo_pasajero = "Turista"
        self.__pase_turistico = pase_turistico
        self.__dias_validez = 7  # Fijo por defecto
        self.__multiviaje = multiviaje

    # Metodo privado (Encapsulamiento)
    def __calcular_tarifa_package(self):
        # Si es multiviaje, el precio base aumenta un 50%
        factor = 1.5 if self.__multiviaje else 1.0
        return self.precio_base * factor

    # POLIMORFISMO
    def calcular_precio_final(self):
        return self.__calcular_tarifa_package()

    # POLIMORFISMO
    def validar_ticket(self):
        # Valida que el pase empiece con 'TUR-'
        if self.__pase_turistico.startswith("TUR-"):
            return True
        print(f"ERROR: Ticket {self.numero_ticket} inválido (Pase turístico desconocido).")
        return False

    def __str__(self):
        mod = "Multiviaje" if self.__multiviaje else "Simple"
        return super().__str__() + f" | Pase: {self.__pase_turistico} [{mod}]"