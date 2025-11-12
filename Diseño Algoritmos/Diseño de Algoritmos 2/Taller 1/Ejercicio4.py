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
# importa la libreria os para limpiar la consola
import os
# Funcion para limpiar la consola
def limpiar_consola():
    os.system('cls')

#Se define la funcion obtener_grupo_etiario que recibe un entero edad y devuelve un string
def obtener_grupo_etiario(edad:int)->str:
    # Verifica que la edad sea mayor a 0 y menor o igual a 12
    if edad > 0 and edad <= 12:
        return 'Niño' #retorna Niño si tiene el rango de edad
    # Verifica que la edad sea mayor o igual a 13 y menor o igual a 17
    elif edad >= 13 and edad <= 17:
        return 'Adolecente' #retorna Adolecente si tiene el rango de edad
    # Verifica que la edad sea mayor o igual a 18 y menor o igual a 64
    elif edad >= 18 and edad <= 64:
        return 'Adulto' #retorna Adulto si tiene el rango de edad
    # Verifica que la edad sea mayor o igual a 65
    elif edad >= 65:
        return 'Adulto mayor' #retorna Adulto mayor si tiene el rango de edad

#Se define la funcion mostrar_clasificacion que recibe un string nombre y un entero edad y devuelve un string
def mostrar_clasificacion(nombre:str,edad:int)->str:
    # Verifica que la edad no sea negativa u+y
    if edad < 0:
        #Imprime Edad no valida si la edad es negativa
        return print('Edad no valida')
    #Si no es negativa
    else:
        #Imprime el nombre, edad y la clasificacion obtenida de la funcion obtener_grupo_etiario
        return print(f'Nombre: {nombre}, edad: {edad} y clasificacion: {obtener_grupo_etiario(edad)}')

# Solicita al usuario ingresar la edad y el nombre
edad = int(input('Edad: '))
nombre = input('Nombre: ')
#Llama a la funcion limpiar_consola para limpiar la consola
limpiar_consola()
#Llama a la funcion mostrar_clasificacion con los parametros nombre y edad
mostrar_clasificacion(nombre,edad)