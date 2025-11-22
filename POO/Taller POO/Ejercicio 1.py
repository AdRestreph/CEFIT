"""
EJERCICIO 5.3: SISTEMA DE PASAJEROS Y TICKETS
------------------------------------------------------------------------------------------------------------------------
CONTEXTO:
Emitir tickets para pasajeros regulares, estudiantes, adultos mayores
y turistas, cada uno con descuentos y validaciones diferentes.

REQUERIMIENTOS:
1. Crear clase abstracta "Ticket" (ABSTRACCION):
   - Atributos privados: numero_ticket, fecha_emision, ruta, asiento
   - Atributo protegido: _tipo_pasajero
   - Metodo abstracto: calcular_precio_final()
   - Metodo abstracto: validar_ticket()
   - Metodo concreto: imprimir_ticket()

2. Clases derivadas (HERENCIA):
   - TicketRegular: tarifa_normal, ida_vuelta
   - TicketEstudiante: carnet_universitario, descuento_50
   - TicketAdultoMayor: cedula, descuento_30, horario_especial
   - TicketTurista: pase_turistico, dias_validez, multiviaje

3. ENCAPSULAMIENTO:
   - Precio con calculos internos privados
   - Metodo privado __aplicar_descuento()
   - Validacion de documentos

4. POLIMORFISMO:
   - calcular_precio_final() con descuentos: 0%, 50%, 30%, package
   - validar_ticket() verifica diferentes requisitos

ENTREGABLES:
- Todas las clases implementadas
- Emitir 3 tickets de cada tipo
- Calcular ingresos totales
- Validar tickets de forma polimórfica
"""

import abc  as ABC

class Ticket(ABC):
    def __init__(self, numero_ticket, fecha_emision, ruta, asiento):
        self.__numero_ticket = numero_ticket
        self.__fecha_emision = fecha_emision
        self.__ruta = ruta
        self.__asiento = asiento
        self._tipo_pasajero = None

    @ABC.abstractmethod
    def calcular_precio_final(self):
        pass

    @ABC.abstractmethod
    def validar_ticket(self):
        pass

    def imprimir_ticket(self):
        print(f"Ticket Número: {self.__numero_ticket}")
        print(f"Fecha de Emisión: {self.__fecha_emision}")
        print(f"Ruta: {self.__ruta}")
        print(f"Asiento: {self.__asiento}")
        print(f"Tipo de Pasajero: {self._tipo_pasajero}")