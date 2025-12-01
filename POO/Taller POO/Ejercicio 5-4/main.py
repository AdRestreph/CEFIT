from sistema_conductores import ConductorRegular, ConductorEventual, ConductorEntrenamiento, Supervisor
if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN DE CONDUCTORES Y TURNOS ===\n")

    try:
        # 1. Crear Supervisores
        sup1 = Supervisor("Carlos Jefe", "LIC-001", 15, "C", 2500, 500)
        sup2 = Supervisor("Ana Lider", "LIC-002", 12, "C", 2600, 500)

        # 2. Crear Conductores Regulares
        reg1 = ConductorRegular("Juan Perez", "LIC-101", 5, "C", "Mañana", "Bus-01", 1200)
        reg2 = ConductorRegular("Maria Lopez", "LIC-102", 4, "B", "Tarde", "Auto-05", 1100)

        # 3. Crear Conductores Eventuales
        evt1 = ConductorEventual("Pedro Event", "LIC-201", 8, "C", 80.0, "Fines de Semana")
        evt2 = ConductorEventual("Luis Temp", "LIC-202", 10, "C", 85.0, "Noches")

        # 4. Crear Conductores en Entrenamiento
        tra1 = ConductorEntrenamiento("Junior 1", "LIC-301", 0, "B", sup1, fase=1)
        tra2 = ConductorEntrenamiento("Junior 2", "LIC-302", 1, "B", sup2, fase=2)

        # Asignar equipo a supervisores
        sup1.agregar_conductor_a_cargo(reg1)
        sup1.agregar_conductor_a_cargo(tra1)
        sup2.agregar_conductor_a_cargo(reg2)

        # Lista de todos los empleados
        plantilla = [sup1, sup2, reg1, reg2, evt1, evt2, tra1, tra2]

        print("--- ASIGNACIÓN DE TURNOS SEMANALES ---")
        # Simulamos un mes de trabajo (4 semanas)
        # Regular 1 trabaja extra (170 horas)
        for _ in range(21):  # 21 días
            reg1.registrar_turno({'fecha': '2023-10-XX', 'horas': 8})  # 168 horas
        reg1.registrar_turno({'fecha': '2023-10-30', 'horas': 4})  # Total 172h

        # Regular 2 trabaja normal (160 horas)
        for _ in range(20):
            reg2.registrar_turno({'fecha': '2023-10-XX', 'horas': 8})

        # Eventual trabaja 10 dias
        for _ in range(10):
            evt1.registrar_turno({'fecha': '2023-10-XX', 'horas': 8})

        # Trainee trabaja, pero su sueldo es fijo
        tra1.registrar_turno({'fecha': '2023-10-01', 'horas': 6})

        print("\n--- REPORTE DE PLANILLA MENSUAL (POLIMORFISMO) ---")
        print(f"{'EMPLEADO':<35} | {'TIPO':<15} | {'SALARIO ($)':<12} | {'VEHICULO BUS?'}")
        print("-" * 90)

        for conductor in plantilla:
            # Polimorfismo en acción: Se llama al mismo método, pero cada objeto actúa diferente
            salario = conductor.calcular_salario_mensual()
            puede_bus = "SI" if conductor.puede_conducir_vehiculo("Bus") else "NO"

            tipo_clase = conductor.__class__.__name__.replace("Conductor", "")

            print(f"{conductor.nombre:<35} | {tipo_clase:<15} | ${salario:>10.2f} | {puede_bus:^13}")

        print("\n--- PRUEBA DE ENCAPSULAMIENTO ---")
        # Intento de acceso directo a atributo privado (descomentar para ver error)
        # print(reg1.__salario_base) # Esto lanzará AttributeError
        print(f"Intento de leer nombre vía getter: {reg1.nombre}")

        # Evaluación protegida
        reg1.agregar_evaluacion(10, "Excelente desempeño en horas extra")
        print(f"Evaluaciones de {reg1.nombre}: {reg1._evaluaciones}")

    except ValueError as e:
        print(f"Error de validación: {e}")