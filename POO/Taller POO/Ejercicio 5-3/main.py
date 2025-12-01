from sistema_tickets import TicketRegular, TicketEstudiante, TicketAdultoMayor, TicketTurista
if __name__ == "__main__":
    print("=== SISTEMA DE EMISIÓN DE TICKETS DE VIAJE ===\n")

    lista_tickets = []
    precio_base_ruta = 100.00  # Precio estándar para las pruebas

    try:
        # --- CREACIÓN DE OBJETOS (3 de cada tipo) ---

        # 1. Tickets Regulares
        lista_tickets.append(TicketRegular("REG-001", "Madrid-Barcelona", "12A", precio_base_ruta, ida_vuelta=False))
        lista_tickets.append(TicketRegular("REG-002", "Madrid-Barcelona", "12B", precio_base_ruta, ida_vuelta=True))
        lista_tickets.append(TicketRegular("REG-003", "Sevilla-Valencia", "45C", precio_base_ruta, ida_vuelta=False))

        # 2. Tickets Estudiante
        lista_tickets.append(TicketEstudiante("EST-001", "Madrid-Barcelona", "14A", precio_base_ruta, "UNI-2023-A"))
        lista_tickets.append(TicketEstudiante("EST-002", "Bilbao-Madrid", "05F", precio_base_ruta, "UNI-9999-X"))
        lista_tickets.append(
            TicketEstudiante("EST-003", "Vigo-Madrid", "02A", precio_base_ruta, ""))  # Carnet inválido para prueba

        # 3. Tickets Adulto Mayor
        lista_tickets.append(
            TicketAdultoMayor("MAY-001", "Madrid-Toledo", "01A", precio_base_ruta, "50001234", horario_especial=False))
        lista_tickets.append(
            TicketAdultoMayor("MAY-002", "Madrid-Toledo", "01B", precio_base_ruta, "50005678", horario_especial=True))
        lista_tickets.append(TicketAdultoMayor("MAY-003", "Madrid-Sur", "02C", precio_base_ruta, "ABC-Error",
                                               horario_especial=False))  # Cédula inválida

        # 4. Tickets Turista
        lista_tickets.append(
            TicketTurista("TUR-001", "City-Tour", "N/A", precio_base_ruta, "TUR-USA-01", multiviaje=True))
        lista_tickets.append(
            TicketTurista("TUR-002", "City-Tour", "N/A", precio_base_ruta, "TUR-JAP-02", multiviaje=False))
        lista_tickets.append(TicketTurista("TUR-003", "Museos-Pack", "N/A", precio_base_ruta, "INVALIDO-01",
                                           multiviaje=False))  # Pase inválido

        # --- PROCESAMIENTO POLIMÓRFICO ---

        print(f"{'ID TICKET':<10} | {'TIPO':<15} | {'ESTADO':<10} | {'PRECIO FINAL'}")
        print("-" * 60)

        ingresos_totales = 0.0
        tickets_validos_count = 0

        for t in lista_tickets:
            # 1. Validación Polimórfica: Cada ticket sabe cómo validarse
            es_valido = t.validar_ticket()
            estado_str = "VÁLIDO" if es_valido else "INVÁLIDO"

            # 2. Cálculo Polimórfico: Cada ticket aplica sus propios descuentos/reglas
            precio_final = t.calcular_precio_final()

            if es_valido:
                ingresos_totales += precio_final
                tickets_validos_count += 1

            # Imprimir fila de resumen
            print(f"{t.numero_ticket:<10} | {t._tipo_pasajero:<15} | {estado_str:<10} | ${precio_final:>8.2f}")

        print("-" * 60)
        print(f"INGRESOS TOTALES DEL DÍA: ${ingresos_totales:,.2f}")
        print(f"TICKETS PROCESADOS: {len(lista_tickets)} | VÁLIDOS: {tickets_validos_count}")

        print("\n--- DETALLE DE TICKETS (Uso de __str__) ---")
        for t in lista_tickets[:4]:  # Solo imprimimos los primeros 4 para no saturar consola
            t.imprimir_ticket()

    except ValueError as e:
        print(f"Error crítico en creación de datos: {e}")