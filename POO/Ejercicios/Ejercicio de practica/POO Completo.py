import abc
class Personaje:
    def __init__(self, nombre, salud, fuerza, inteligencia):
        self.nombre = nombre
        self.salud = salud
        self.fuerza = fuerza
        self.inteligencia = inteligencia

    def __str__(self):
        return f" Personaje: {self.nombre}\n Salud: {self.salud}\n Fuerza: {self.fuerza}\n Inteligencia: {self.inteligencia}"

    def atacar(self, otro_personaje):
        damage = self.fuerza
        otro_personaje.salud -= damage
        print(f"{self.nombre} ataca a {otro_personaje.nombre} causando {damage} de daño.")

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, salud=150, fuerza=20, inteligencia=5)

    def atacar(self, otro_personaje):
        damage = self.fuerza * 1.5
        otro_personaje.salud -= damage
        print(f"{self.nombre} realiza un ataque poderoso a {otro_personaje.nombre} causando {damage} de daño.")