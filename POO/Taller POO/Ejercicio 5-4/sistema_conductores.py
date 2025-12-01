import abc

class Conductor(abc.ABC):

    def __init__(self, nombre, licencia, anos_experiencia, categoria):
        # Validación de datos de entrada
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena no vacía.")
        if anos_experiencia < 0:
            raise ValueError("Los años de experiencia no pueden ser negativos.")

        # Atributos Privados (Encapsulamiento fuerte)
        self.__nombre = nombre
        self.__licencia = licencia
        self.__anos_experiencia = anos_experiencia
        self.__categoria = categoria

        # Atributos Protegidos (Accesibles por herencia)
        self._turnos_trabajados = []  # Lista de diccionarios {fecha, horas}
        self._evaluaciones = []  # Requerimiento: Evaluaciones protegidas

    # Getters para acceder a atributos privados (Encapsulamiento)
    @property
    def nombre(self):
        return self.__nombre

    @property
    def categoria(self):
        return self.__categoria

    @property
    def anos_experiencia(self):
        return self.__anos_experiencia

    def registrar_turno(self, turno):
        """
        Metodo concreto para registrar un turno.
        :param turno: Diccionario con detalles del turno {'fecha': str, 'horas': int}
        """
        if not isinstance(turno, dict) or 'horas' not in turno:
            raise ValueError("El formato del turno es incorrecto.")
        self._turnos_trabajados.append(turno)
        print(f"Turno registrado para {self.__nombre}: {turno['horas']} horas.")

    def agregar_evaluacion(self, nota, comentario):
        """Agrega una evaluación a la lista protegida."""
        self._evaluaciones.append({'nota': nota, 'comentario': comentario})

    # Métodos Abstractos (Deben ser implementados por las clases hijas)
    @abc.abstractmethod
    def calcular_salario_mensual(self):
        """Calcula el salario según el tipo de contrato."""
        pass

    @abc.abstractmethod
    def puede_conducir_vehiculo(self, tipo_vehiculo):
        """Valida si el conductor puede manejar cierto vehículo."""
        pass

    def __str__(self):
        return f"Conductor: {self.__nombre} | Licencia: {self.__licencia} | Cat: {self.__categoria}"

class ConductorRegular(Conductor):
    """
    Conductor con contrato fijo.
    Calcula salario base + horas extras.
    """

    def __init__(self, nombre, licencia, anos_experiencia, categoria, turno_fijo, vehiculo_asignado, salario_base):
        super().__init__(nombre, licencia, anos_experiencia, categoria)
        self.__turno_fijo = turno_fijo
        self.__vehiculo_asignado = vehiculo_asignado
        self.__salario_base = salario_base

    # Metodo Privado propio de esta clase (Encapsulamiento específico)
    def __calcular_horas_extras(self):
        """Calcula el monto por horas extras (más de 40 horas semanales/160 mensuales)."""
        total_horas = sum(t['horas'] for t in self._turnos_trabajados)
        horas_base = 160
        precio_hora_extra = 20.0  # Valor arbitrario para el ejemplo

        if total_horas > horas_base:
            return (total_horas - horas_base) * precio_hora_extra
        return 0.0

    # POLIMORFISMO: Implementación específica de salario
    def calcular_salario_mensual(self):
        monto_extras = self.__calcular_horas_extras()
        total = self.__salario_base + monto_extras
        return total

    # POLIMORFISMO: Validación de licencia
    def puede_conducir_vehiculo(self, tipo_vehiculo):
        # Lógica simplificada: Categoría C es profesional
        if self.categoria == 'C' or (self.categoria == 'B' and tipo_vehiculo == 'Automovil'):
            return True
        return False

    def __str__(self):
        return super().__str__() + f" [REGULAR] - Vehículo: {self.__vehiculo_asignado}"


class ConductorEventual(Conductor):
    """
    Conductor que cobra por día/turno trabajado.
    """

    def __init__(self, nombre, licencia, anos_experiencia, categoria, tarifa_dia, disponibilidad):
        super().__init__(nombre, licencia, anos_experiencia, categoria)
        self.__tarifa_dia = tarifa_dia
        self.__disponibilidad = disponibilidad  # Ejemplo: "Fines de semana"

    # POLIMORFISMO
    def calcular_salario_mensual(self):
        # Asumimos que cada turno registrado cuenta como un día trabajado
        dias_trabajados = len(self._turnos_trabajados)
        return dias_trabajados * self.__tarifa_dia

    # POLIMORFISMO
    def puede_conducir_vehiculo(self, tipo_vehiculo):
        # Los eventuales suelen tener restricciones más estrictas
        if self.categoria == 'C' and tipo_vehiculo in ['Camion', 'Bus']:
            return True
        elif self.categoria == 'B' and tipo_vehiculo == 'Automovil':
            return True
        return False

    def __str__(self):
        return super().__str__() + f" [EVENTUAL] - Disp: {self.__disponibilidad}"


class ConductorEntrenamiento(Conductor):
    """
    Conductor en fase de aprendizaje. Salario reducido.
    """

    def __init__(self, nombre, licencia, anos_experiencia, categoria, supervisor, fase):
        super().__init__(nombre, licencia, anos_experiencia, categoria)
        self.__supervisor = supervisor  # Nombre u objeto del supervisor
        self.__fase_entrenamiento = fase
        self.__salario_reducido = 800.0  # Valor fijo bajo

    # POLIMORFISMO: Salario fijo reducido sin importar horas
    def calcular_salario_mensual(self):
        return self.__salario_reducido

    # POLIMORFISMO: Solo puede conducir si tiene supervisor y es vehículo ligero
    def puede_conducir_vehiculo(self, tipo_vehiculo):
        if tipo_vehiculo == 'Automovil' and self.__fase_entrenamiento > 1:
            return True
        return False

    def __str__(self):
        sup_nombre = self.__supervisor.nombre if isinstance(self.__supervisor, Conductor) else self.__supervisor
        return super().__str__() + f" [TRAINEE] - Sup: {sup_nombre}"


class Supervisor(Conductor):
    """
    Supervisor de flota. Cobra base + bono.
    """

    def __init__(self, nombre, licencia, anos_experiencia, categoria, salario_base, bono_supervision):
        super().__init__(nombre, licencia, anos_experiencia, categoria)
        self.__conductores_a_cargo = []
        self.__salario_base = salario_base
        self.__bono_supervision = bono_supervision

    def agregar_conductor_a_cargo(self, conductor):
        if isinstance(conductor, Conductor):
            self.__conductores_a_cargo.append(conductor)

    # POLIMORFISMO
    def calcular_salario_mensual(self):
        # Bono base + pequeño extra por cada conductor a cargo
        extra_por_equipo = len(self.__conductores_a_cargo) * 50
        return self.__salario_base + self.__bono_supervision + extra_por_equipo

    # POLIMORFISMO: Los supervisores suelen poder conducir todo
    def puede_conducir_vehiculo(self, tipo_vehiculo):
        return True

    def __str__(self):
        return super().__str__() + f" [SUPERVISOR] - Equipo: {len(self.__conductores_a_cargo)} personas"