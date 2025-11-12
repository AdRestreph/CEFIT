import os  # Importa el módulo os para poder ejecutar comandos del sistema operativo, como limpiar la terminal

"""
Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal.
"""

# Función para limpiar la terminal según el sistema operativo
def limpiar_terminal():
        os.system('cls')  # Ejecuta el comando 'cls' para limpiar la terminal

# Función para identificar si una letra es vocal
def Identificar_Vocal(letra: str):
    """
    Devuelve un mensaje dependiendo si es vocal o no, o si es otro caracter
    
    Parametros
    -----------------------------
    Entrada: Letra(Str)
    -----------------------------
    """
    
    vocales = {'a','e','i','o','u'}  # Conjunto de vocales para comparación
    if letra.lower() in vocales:  # Convertimos la letra a minúscula y verificamos si está en el conjunto
        print("Es una vocal \n")  # Si es vocal, imprime mensaje
    else:
        print("No es una vocal \n")  # Si no es vocal, imprime otro mensaje
        

while True:  # Ciclo que se repite mientras a sea distinto de 2
    # Muestra el menú de opciones al usuario
    print("Elija una de las opciones: \n 1. Identificar vocal \n 2. Para cerrar la aplicacion")
    opcion = int(input("Ingrese una opcion: \n"))  # Solicita opción al usuario y la convierte a entero
    
    if opcion == 1:  # Si el usuario elige 1
        letra = input("Ingrese una letra: \n")  # Solicita una letra
        if len(letra) != 1:  # Verifica que el usuario haya ingresado solo un caracter
            limpiar_terminal()  # Limpia la terminal
            print("\n Ingrese un solo caracter \n")  # Muestra mensaje de error
        else:
            limpiar_terminal()  # Limpia la terminal
            Identificar_Vocal(letra)  # Llama a la función para identificar vocal
    elif opcion == 2:  # Si el usuario elige 2
        limpiar_terminal()  # Limpia la terminal
        print("\n Cerrando aplicacion \n")  # Mensaje de salida
        break # Cierra el ciclo
    else:  # Si el usuario ingresa cualquier otro valor
        limpiar_terminal()  # Limpia la terminal
        print("\n Ingrese una de las opciones indicadas \n")  # Mensaje de error
