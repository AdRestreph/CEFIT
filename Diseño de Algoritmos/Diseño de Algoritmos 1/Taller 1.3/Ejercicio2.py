import os   # Importa el módulo os

"""
Escribir un programa que, dado un número entero, muestre su valor absoluto. 
Nota: para los positivos su valor absoluto es igual al número, 
y para los negativos es el número multiplicado por -1.
"""

# Definición de función para limpiar la terminal
def limpiar_terminal():
        os.system('cls') # Ejecuta el comando 'cls' en Windows para limpiar la pantalla

# Definición de la función para calcular el valor absoluto
def valor_abs(numero: int) -> int:
    """
    Calcula y devuelve el valor absoluto de un número entero.
    
    Parámetros
    ----------
    numero : int
        Número de entrada
    
    Retorna
    -------
    int
        Valor absoluto del número
    """  # Docstring que documenta lo que hace la función y sus parámetros
    
    if numero < 0:       # Si el número es negativo...
        return -numero   # Retorna el número multiplicado por -1 (su valor absoluto)
    return numero        # Si el número es positivo o 0, lo retorna directamente

# Bucle principal del programa
while True:   # Se ejecuta indefinidamente hasta que se use 'break'
    print("Elija una de las opciones: \n 1. Valor absoluto \n 2. Para cerrar la aplicacion")
    opcion = input("Ingrese una opcion: \n")   # Solicita al usuario que ingrese una opción
    
    if opcion == "1":   # Si la opción es "1", se calcula el valor absoluto
        numero = int(input("Ingrese un numero: \n"))   # Pide un número entero al usuario
        limpiar_terminal()   # Limpia la terminal antes de mostrar el resultado
        print(f"El valor absoluto de {numero} es {valor_abs(numero)} \n")  # Muestra el resultado
        
    elif opcion == "2":   # Si la opción es "2", cierra la aplicación
        limpiar_terminal()   # Limpia la terminal antes de salir
        print("\n Cerrando aplicacion \n")   # Mensaje de salida
        break   # Rompe el bucle 'while' y finaliza el programa
        
    else:   # Si la opción no es válida
        limpiar_terminal()   # Limpia la terminal
        print("\n Ingrese una de las opciones indicadas \n")   # Muestra un mensaje de error
