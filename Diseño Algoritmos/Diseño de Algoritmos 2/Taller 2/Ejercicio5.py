"""
5. Escribe un programa que:

Genere una lista de automática números del 1 al 40.
Muestre la sumatoria consecutiva de los números (es decir, la sumatoria acumulada).

Además:
-Indique en una lista los numero pares.
-Indique en una lista los numero impares.
-Indique cuántos números pares e impares hay en la secuencia.
"""
# se importa os para crear la funcion de limpiar la consola
import os
# Se define la funcion para limpiar la consola
def limpiar_consola():
    # se utiliza el comando para limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')
# Se define la funcion para generar la lista de numeros del 1 al 40 y calcular la sumatoria acumulada, recibe un parametro rango_final que es int y retorna una tupla con 3 listas
def generar_numeros_y_sumatoria(rango_final:int)->tuple:
    # Se crean tres listas vacias para almacenar los numeros, los pares y los impares
    numeros = []
    numeros_pares = []
    numeros_impares = []
    # Se inicializa la variable sumatoria en 0
    sumatoria = 0
    # Se utiliza un ciclo for para recorrer los numeros del 1 al rango_final
    for numero in range(1, rango_final + 1):
        # Se agrega el numero a la lista de numeros
        numeros.append(numero)
        # Se suma el numero a la sumatoria acumulada
        sumatoria += numero
        # Se crea una condicion para verificar si el numero es par o impar
        if numero % 2 == 0:
            # Si es par se agrega a la lista de numeros pares
            numeros_pares.append(numero)
        else:
            # Si es impar se agrega a la lista de numeros impares
            numeros_impares.append(numero)
    # Se retorna las tres listas y la sumatoria como una tupla
    return numeros, numeros_pares, numeros_impares, sumatoria
# Se limpia la consola antes de mostrar los resultados por si tiene algun contenido previo residual
limpiar_consola()
# Se llama a la funcion generar_numeros_y_sumatoria con rango_final 40 y se desempaquetan las listas y la sumatoria
numeros, numeros_pares, numeros_impares, sumatoria = generar_numeros_y_sumatoria(40)
# Se imprime la lista de numeros generados
print(f'Números del 1 al 40: \n{numeros}')
# Se imprime la sumatoria acumulada de los numeros
print(f'\nSumatoria acumulada de los números del 1 al 40:\n{sumatoria}')
# Se imprime la lista de numeros pares
print(f'\nNúmeros pares:\n{numeros_pares}')
# Se imprime la lista de numeros impares
print(f'\nNúmeros impares:\n{numeros_impares}')
# Se imprime la cantidad de numeros pares e impares
print(f'\nCantidad de números pares: {len(numeros_pares)}\nCantidad de números impares: {len(numeros_impares)}')
