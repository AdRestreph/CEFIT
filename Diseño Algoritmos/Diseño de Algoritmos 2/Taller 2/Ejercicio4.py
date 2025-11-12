"""
4. Escribe un programa en Python que haga lo siguiente:

Recorra los números del 1 al 100 utilizando un ciclo for.
Identifique cuáles de estos números son múltiplos de 2 y cuáles no.
Guarde los múltiplos de 2 en una lista llamada lista1.
Guarde los números que no son múltiplos de 2 en otra lista llamada lista2.
Al finalizar el ciclo, muestre en pantalla el contenido de ambas listas con un mensaje descriptivo.

"""
# se importa os para crear la funcion de limpiar la consola
import os
# Se define la funcion para limpiar la consola
def limpiar_consola():
    # se utiliza el comando para limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')

# Se define la funcion para clasificar los numeros en multiplos de 2 y no multiplos de 2, no recibe parametros y retorna dos listas
def clasificar_numeros()->tuple:
    # Se crean dos listas vacias para almacenar los multiplos de 2 y los no multiplos de 2
    lista1 = []
    lista2 = []
    # Se utiliza un ciclo for para recorrer los numeros del 1 al 100
    for numero in range(1, 101):
        # Se crea una condicion para verificar si el numero es multiplo de 2
        if numero % 2 == 0:
            # Si es multiplo de 2 se agrega a la lista1
            lista1.append(numero)
        else:
            # Si no es multiplo de 2 se agrega a la lista2
            lista2.append(numero)
    # Se retorna ambas listas como una tupla
    return lista1, lista2

# Se limpia la consola antes de mostrar los resultados por si tiene algun contenido previo residual
limpiar_consola()
# Se llama a la funcion clasificar_numeros y se desempaquetan las listas
multiplos_de_2, no_multiplos_de_2 = clasificar_numeros()
# Se imprime el contenido de ambas listas con un mensaje descriptivo
print('Números múltiplos de 2 (lista1):')
# Se imprime la lista de multiplos de 2
print(multiplos_de_2)
# Se imprime un salto de linea para separar las dos listas
print('\nNúmeros que no son múltiplos de 2 (lista2):')
# Se imprime la lista de no multiplos de 2
print(no_multiplos_de_2)