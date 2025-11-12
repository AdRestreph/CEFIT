"""
2. Escribe un programa en Python que solicite al usuario ingresar un número entero positivo. Si el usuario ingresa un valor inválido (como un número cero, negativo o no entero),
el programa debe mostrar un mensaje de error adecuado y volver a pedir el número hasta que se ingrese un valor correcto. Una vez ingresado un número válido, el programa debe mostrar
la tabla de multiplicar del 1 al 10 de ese número. Asegúrate de utilizar validación de datos y mostrar la salida de forma clara y ordenada.
"""
# Se importa os para crear la funcion de limpiar la consola
import os
# Se define la funcion para limpiar la consola
def limpiar_consola():
    # se utiliza el comando para limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')
# Se define la funcion para generar la tabla de multiplicar, recibe un parametro numero que es int y retorna un str
def tabla_multiplicar(numero:int)->str:
    # Se crea una variable resultado que almacena el str inicial de la tabla de multiplicar
    resultado = f'Tabla de multiplicar del {numero}:\n'
    # Se utiliza un ciclo for para iterar del 1 al 10
    for i in range(1, 11):
        # Se concatena a la variable resultado cada linea de la tabla de multiplicar
        resultado += f'{numero} x {i} = {numero * i}\n'
    # Se retorna la variable resultado
    return resultado
# Se inicia un ciclo while True para pedir el numero al usuario hasta que ingrese un valor valido
while True:
    # Se crea un bloque try-except para manejar errores en la entrada del usuario
    try:
        # Solicita al usuario que ingrese un numero entero positivo
        numero = int(input('Ingrese un número entero positivo: '))
        # Se verifica si el numero es mayor a 0
        if numero > 0:
            # Si se cumple la condicion se limpia la consola y se imprime la tabla de multiplicar
            limpiar_consola()
            # Se usa la funcion talba_multiplicar para imprimir la tabla de multiplicar del numero ingresado
            print(tabla_multiplicar(numero))
            # Se rompe el ciclo while ya que se ingreso un numero valido
            break
        # Si el numero no es mayor a 0 se muestra un mensaje de error
        else:
            # Imprime el mensaje de error
            print('Error: El número debe ser mayor a cero. Por favor, intente de nuevo.')
    # Si el usuario ingresa un valor no numerico o un float se captura la excepcion ValueError
    except ValueError:
        # Se muestra un mensaje de error indicando que se debe ingresar un numero valido
        print('Error: Por favor, intente de nuevo con un numero mayor a cero que no sea decimal.')
