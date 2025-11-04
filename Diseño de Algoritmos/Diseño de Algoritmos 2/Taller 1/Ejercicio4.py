"""
Desarrolla un programa que determine el grupo etario de una persona
según su edad. Crea una función llamada obtener_grupo_etario que
reciba un número entero correspondiente a la edad y devuelva una cadena
que indique si la persona es: "Niño" (0–12 años), "Adolescente" (13–17
años), "Adulto" (18–64 años) o "Adulto mayor" (65 años o más).
La función debe verificar que la edad no sea negativa; si lo es, debe
devolver un mensaje de error como "Edad no válida". Luego, implementa
una función mostrar_clasificacion que reciba el nombre (cadena de texto)
y la edad (entero) de una persona, y muestre un mensaje en pantalla
indicando a qué grupo etario pertenece, por ejemplo: "Lucía es un(a)
Adulto"
"""

import os

def limpiar_consola():
    os.system('cls')

def obtener_grupo_etiario(edad:int)->str:
    if edad > 0 and edad <= 12:
        return 'Niño'
    elif edad >= 13 and edad <= 17:
        return 'Adolecente'
    elif edad >= 18 and edad <= 64:
        return 'Adulto'
    elif edad >= 65:
        return 'Adulto mayor'


def mostrar_clasificacion(nombre:str,edad:int)->str:
    if edad < 0:
        return print('Edad no valida')
    else:
        return print(f'Nombre: {nombre}, edad: {edad} y clasificacion: {obtener_grupo_etiario(edad)}')

edad = int(input('Edad: '))
nombre = input('Nombre: ')
limpiar_consola()
mostrar_clasificacion(nombre,edad)