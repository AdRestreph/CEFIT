from abc import ABC , abstractmethod
class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def arrancar(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    @abstractmethod
    def detener(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    @abstractmethod
    def consumo_por_kilometro(self):
        pass

class Carro(Vehiculo):
    def __init__(self, marca, modelo, litros_por_km):
        super().__init__(marca, modelo)
        self.litros_por_km = litros_por_km

    def __str__(self):
        return f"{self.marca}\n{self.modelo}\n{self.litros_por_km}"
    def arrancar(self):
        return f"El coche {self.marca} {self.modelo} ha arrancado."
    def detener(self):
        return f"El coche {self.marca} {self.modelo} se ha detenido."
    def consumo_por_kilometro(self):
        return 0.07

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def __str__(self):
        return f"{self.marca}\n{self.modelo}\n{self.cilindrada}"
    def arrancar(self):
        return f"La moto {self.marca} {self.modelo} ha arrancado."
    def detener(self):
        return f"La moto {self.marca} {self.modelo} se ha detenido."
    def consumo_por_kilometro(self):
        if self.cilindrada<200:
            return 0.03
        else:
            return 0.05


carro1 = Carro("Toyota", "Corolla", 0.07)
moto1 = Moto("Yamaha", "YZF-R3", 150)
moto2 = Moto("Ducati", "Panigale V4", 600)

print(carro1.arrancar())
print(f"Consumo por km del carro: {carro1.consumo_por_kilometro()} litros")
print(carro1.detener())

print(moto1.arrancar())
print(f"Consumo por km de {moto1.marca}: {moto1.consumo_por_kilometro()} litros")
print(moto1.detener())

print(moto2.arrancar())
print(f"Consumo por km de {moto2.marca}: {moto2.consumo_por_kilometro()} litros")
print(moto2.detener())

print(carro1)
print(moto1)
print(moto2)