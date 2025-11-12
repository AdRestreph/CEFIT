"""
1. Desarrolla un programa en Python que solicite al usuario ingresar su nombre y apellido, y luego le pida cinco calificaciones numéricas entre 0 y 10
(Ingrese la calificación #1:, luego Ingrese la calificación #2: y así sucesivamente hasta Ingrese la calificación # 5:).

El programa debe validar cada entrada, asegurándose de que el valor sea un número válido dentro del rango permitido. Si el usuario ingresa un dato incorrecto
(por ejemplo, un número fuera del rango o una entrada no numérica), debe mostrarse un mensaje de error y volver a solicitar esa calificación hasta que se ingrese correctamente.

Al finalizar, el programa debe calcular el promedio de las cinco calificaciones y mostrar un mensaje personalizado con el nombre completo del estudiante,
 su promedio (redondeado a dos decimales), y un nivel de rendimiento según esta escala:

· "Excelente" si el promedio es mayor o igual a 9,
· "Bueno" si es mayor o igual a 7,
· "Regular" si es mayor o igual a 5,
· "Insuficiente" si es menor a 5.
Asegúrate de que el programa tenga una salida clara, ordenada y fácil de entender.
"""

# Se importa os para crear la funcion de limpiar la consola
import os
# Se define la funcion para limpiar la consola
def limpiar_consola():
    # se utiliza el comando para limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')
# Se define la funcion del rendimiento del estudiante con un atributo promedio que seria float y con una salida str que indicaria el nivel de desempeño del estudiante
def nivel_rendimiento(promedio:float)->str:
    #Se crea una condicion donde si el promedio es menor que 5 el rendimiento del estudiante seria insuficiente
    if promedio < 5:
        # Retorna el str con el rendimiento del estudiante
        return 'Insuficiente'
    # Se define un elif en donde evalua 2 rangos que sea mayor o igual a 5 y menor que 7
    elif promedio >= 5 and promedio < 7:
        #Si se cumple con la regla anterior entonces el estudiante es regular
        return 'Regular'
    # Se define otro elif donde evalua nuevamente 2 rangos, que sea mayor o igual a 7 y menor que 9
    elif promedio >= 7 and promedio < 9:
        # Si cumple con la condicion anterior el estudiante tiene un rendimiento bueno
        return 'Bueno'
    # Se define el ultimo condicional en base a que sea mayor o igual a 9
    elif promedio >= 9:
        # Si se cumple la condicion retorna rendimiento excelente
        return 'Excelente'

# Se define la funcion para calcular el promedio de las calificaciones de los estudiantes, se pasa un parametro de lista y retorna un float
def calcular_promedio(salida_calificaciones:list)->float:
    # Aca retorna el float, en base a la suma de los numeros que tiene la lista usando la funcion sum() y se divide en el tamaño de la lista utilizando len y se redondea a 2 decimales
    return round(sum(salida_calificaciones) / len(salida_calificaciones), 2)

# Se pide al usuario que ingrese su nombre y apellido
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')

# Se crea una lista vacia para almacenar las notas
notas = []
i = 1

# Se utiliza un ciclo while para pedir las 5 notas al usuario poniendole una condicion de que la longitud de la lista notas sea menor a 5
while len(notas) < 5:
    # Se crea un bloque try-except para manejar errores en la entrada del usuario, en caso de que ingrese un valor no numerico o un float no valido
    try:
        #Solicita la nota al usuario en base al numero i que inicia en 1 y va aumentando hasta 5
        nota = float(input(f'Ingrese la nota #{i}: '))
        # Se crea una condicion para validar que la nota este entre 0 y 10
        if 0 <= nota <= 10:
            # Si la nota es valida se agrega a la lista notas
            notas.append(nota)
            # Se incrementa el contador i en 1
            i += 1
        # Si la nota no es valida se muestra un mensaje de error y se vuelve a solicitar la nota
        else:
            print('La nota no es válida. Por favor ingrese una nota entre 0 y 10.')
    # Si el usuario ingresa un valor no numerico o un float con coma en lugar de punto se captura la excepcion ValueError
    except ValueError:
        # Se muestra un mensaje de error indicando que se debe ingresar un numero valido
        print("Ingrese un número válido (por ejemplo, 7.5).")
        # Continua el ciclo hasta que se ingresen las 5 notas validas

# Se limpia la consola antes de mostrar el resultado final
limpiar_consola()

# Se muestra el resultado final con el nombre completo del estudiante, su promedio y su nivel de rendimiento
print(f'\nEl estudiante {nombre} {apellido} tiene un promedio de {calcular_promedio(notas):.2f} '
      f'y su rendimiento es {nivel_rendimiento(calcular_promedio(notas))}.')

