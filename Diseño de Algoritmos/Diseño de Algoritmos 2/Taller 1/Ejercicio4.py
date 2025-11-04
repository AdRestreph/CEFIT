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