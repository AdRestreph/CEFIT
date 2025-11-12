# Ejemplo de uso de conjuntos (sets) en Python
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}
# Crear un conjunto a partir de una cadena de texto y utilizando el contructor set()
conjunto_c = set("hola mundo")

#Para agregar una lista debe ser con update o creando la variable como conjunto desde el inicio
conjunto_a.update([6, 7, 8, 9, 10])

#Al imprimir la cadena de texto, los caracteres repetidos se eliminan y se generan de forma desordenada
print(conjunto_c)
# Al imprimir el conjunto a se le han agregado los elementos de la lista y no se agrega el tipo de dato
print(conjunto_a)

conjunto_d = {(1, 2), (3, 4)}  # Conjunto de tuplas
print(conjunto_d)

lista_numeros = [1, 2, 2, 3, 4, 4, 5]
conjunto_numeros = set(lista_numeros)  # Convertir lista a conjunto
print(conjunto_numeros)  # Imprime {1, 2, 3, 4, 5}, eliminando duplicados

"""
Una de las utilidades principales de los conjuntos es la eliminación de elementos duplicados en una colección de datos.
Lo que facilita este tipo de operacion en lugar de realizar un algoritmo para eliminar duplicados.
"""

lista_sin_duplicados = list(set(lista_numeros))
print(lista_sin_duplicados)  # Imprime [1, 2, 3, 4, 5]
