"""
3. Desarrolle un programa que calcule el factorial de un número entero positivo con validación de entrada asegurándose de que el valor de entrada sea un número válido dentro
del rango permitido, recuerda que los factoriales no están definidos para números negativos y el factorial de cero es 1.
"""

# Se importa os para crear la funcion de limpiar la consola
import os
# Se define la funcion para limpiar la consola
def limpiar_consola():
    # se utiliza el comando para limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')

# Se define la funcion para calcular el factorial, recibe un parametro numero que es int y retorna un int
def calcular_factorial(numero:int)->int:
    # Se inicializa la variable factorial en 1
    factorial = 1
    # Se utiliza un ciclo for para iterar desde 1 hasta el numero incluido
    for i in range(1, numero + 1):
        # Se multiplica el factorial por el valor de i en cada iteracion
        factorial *= i
    # Se retorna el valor del factorial
    return factorial

# Se inicia un ciclo while True para pedir el numero al usuario hasta que ingrese un valor valido
while True:
    # Se crea un bloque try-except para manejar errores en la entrada del usuario
    try:
        # Solicita al usuario que ingrese un numero entero positivo
        numero = int(input('Ingrese un número entero positivo para calcular su factorial: '))
        # Se verifica si el numero es mayor o igual a 0
        if numero >= 0:
            # Si se cumple la condicion se limpia la consola y se imprime el factorial
            limpiar_consola()
            # Se usa la funcion calcular_factorial para obtener el factorial del numero ingresado
            print(f'El factorial de {numero} es: {calcular_factorial(numero)}')
            # Se rompe el ciclo while ya que se ingreso un numero valido
            break
        # Si el numero es negativo se muestra un mensaje de error
        else:
            # Imprime el mensaje de error
            print('Error: El número debe ser un entero positivo o cero. Por favor, intente de nuevo.')
    # Si el usuario ingresa un valor no numerico o un float se captura la excepcion ValueError
    except ValueError:
        # Se muestra un mensaje de error indicando que se debe ingresar un numero valido
        print('Error: Por favor, intente de nuevo con un número entero positivo o cero.')