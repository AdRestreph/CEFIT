from sistema_tickets import SistemaTickets, TicketRegular, TicketEstudiante, TicketAdultoMayor, TicketTurista
def main():
    """Función principal para demostrar el sistema completo."""

    print("╔═══════════════════════════════════════════════════════╗")
    print("║    SISTEMA DE GESTIÓN DE TICKETS DE TRANSPORTE       ║")
    print("║        Demostración de los 4 Pilares de POO          ║")
    print("╚═══════════════════════════════════════════════════════╝\n")

    sistema = SistemaTickets()

    # ========== EMITIR 3 TICKETS REGULARES ==========
    print("\n" + "█" * 60)
    print("TICKETS REGULARES")
    print("█" * 60)

    sistema.emitir_ticket(TicketRegular(
        ruta="Medellín - Bogotá",
        asiento="A12",
        precio_base=85000,
        ida_vuelta=False
    ))

    sistema.emitir_ticket(TicketRegular(
        ruta="Cali - Cartagena",
        asiento="B07",
        precio_base=120000,
        ida_vuelta=True
    ))

    sistema.emitir_ticket(TicketRegular(
        ruta="Barranquilla - Medellín",
        asiento="C15",
        precio_base=95000,
        ida_vuelta=False
    ))

    # ========== EMITIR 3 TICKETS ESTUDIANTES ==========
    print("\n" + "█" * 60)
    print("TICKETS ESTUDIANTES")
    print("█" * 60)

    sistema.emitir_ticket(TicketEstudiante(
        ruta="Medellín - Manizales",
        asiento="D03",
        precio_base=45000,
        carnet_universitario="UNAL202401"
    ))

    sistema.emitir_ticket(TicketEstudiante(
        ruta="Bogotá - Bucaramanga",
        asiento="E10",
        precio_base=75000,
        carnet_universitario="UdeA202305"
    ))

    sistema.emitir_ticket(TicketEstudiante(
        ruta="Pereira - Cali",
        asiento="F08",
        precio_base=55000,
        carnet_universitario="UIS202402"
    ))

    # ========== EMITIR 3 TICKETS ADULTOS MAYORES ==========
    print("\n" + "█" * 60)
    print("TICKETS ADULTOS MAYORES")
    print("█" * 60)

    sistema.emitir_ticket(TicketAdultoMayor(
        ruta="Medellín - Rionegro",
        asiento="G05",
        precio_base=25000,
        cedula="8234567",
        horario_especial=True
    ))

    sistema.emitir_ticket(TicketAdultoMayor(
        ruta="Bogotá - Villavicencio",
        asiento="H12",
        precio_base=65000,
        cedula="10456789",
        horario_especial=False
    ))

    sistema.emitir_ticket(TicketAdultoMayor(
        ruta="Cali - Popayán",
        asiento="I09",
        precio_base=48000,
        cedula="7123456",
        horario_especial=True
    ))

    # ========== EMITIR 3 TICKETS TURISTAS ==========
    print("\n" + "█" * 60)
    print("TICKETS TURISTAS")
    print("█" * 60)

    sistema.emitir_ticket(TicketTurista(
        ruta="Cartagena - Santa Marta",
        asiento="J06",
        precio_base=90000,
        pase_turistico="PT-2024-001",
        dias_validez=7,
        multiviaje=True
    ))

    sistema.emitir_ticket(TicketTurista(
        ruta="Medellín - Guatapé",
        asiento="K11",
        precio_base=35000,
        pase_turistico="PT-2024-002",
        dias_validez=3,
        multiviaje=True
    ))

    sistema.emitir_ticket(TicketTurista(
        ruta="Bogotá - Zipaquirá",
        asiento="L04",
        precio_base=42000,
        pase_turistico="PT-2024-003",
        dias_validez=5,
        multiviaje=False
    ))

    # ========== VALIDACIÓN POLIMÓRFICA ==========
    sistema.validar_todos_tickets()

    # ========== REPORTE FINANCIERO ==========
    sistema.generar_reporte()


if __name__ == "__main__":
    main()