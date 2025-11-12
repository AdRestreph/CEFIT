# Importamos el módulo os para ejecutar comandos del sistema operativo
import os

"""
Escribir un programa que pida dos palabras y diga si riman o no.
- Si coinciden las 3 últimas letras → riman.
- Si coinciden solo las 2 últimas → riman un poco.
- Si no coinciden → no riman.
"""

# Definición de función para limpiar la terminal
def limpiar_terminal():
    os.system('cls') # Ejecuta el comando 'cls' en Windows para limpiar la pantalla

# Definimos una función que verifica si dos palabras riman
def verificar_rima(palabra_1: str, palabra_2: str) -> str:
    """
    Verifica si dos palabras riman.

    Parámetros
    ----------
    palabra_1 : str
        Primera palabra
    palabra_2 : str
        Segunda palabra

    Retorna
    -------
    str
        Mensaje indicando el tipo de rima
    """
    # Convertimos ambas palabras a minúsculas para evitar errores de comparación
    palabra_1 = palabra_1.lower()
    palabra_2 = palabra_2.lower()

    # Verificamos que ambas palabras tengan al menos 3 letras
    if len(palabra_1) < 3 or len(palabra_2) < 3:
        return "Las palabras deben tener al menos 3 letras"

    # Comparamos las últimas 3 letras de cada palabra
    if palabra_1[-3:] == palabra_2[-3:]:
        return "Las palabras riman"
    # Si no coinciden las últimas 3, verificamos si coinciden las últimas 2
    elif palabra_1[-2:] == palabra_2[-2:]:
        return "Las palabras riman un poco"
    # En cualquier otro caso, no riman
    else:
        return "Las palabras no riman"

# Bucle infinito para mostrar el menú hasta que el usuario decida salir
while True:
    # Mostramos el menú de opciones
    print("Elija una de las opciones: \n 1. Verificar rima \n 2. Para cerrar la aplicación")
    opcion = input("Ingrese una opción: \n")  # Pedimos la opción al usuario

    # Si elige la opción 1, pedimos dos palabras y verificamos la rima
    if opcion == "1":
        palabra1 = input("Ingrese la primera palabra: \n")
        palabra2 = input("Ingrese la segunda palabra: \n")
        limpiar_terminal()  # Limpiamos la terminal
        print(verificar_rima(palabra1, palabra2), "\n")  # Mostramos el resultado

    # Si elige la opción 2, salimos del programa
    elif opcion == "2":
        limpiar_terminal()
        print("\n Cerrando aplicación \n")
        break  # Rompe el bucle y finaliza la ejecución

    # Si ingresa cualquier otra opción, mostramos un mensaje de error
    else:
        limpiar_terminal()
        print("\n Ingrese una de las opciones indicadas \n")