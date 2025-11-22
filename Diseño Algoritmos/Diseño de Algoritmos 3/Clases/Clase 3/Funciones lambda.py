#fUNCIONES LAMBDA

cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Salida: 25

# Función lambda para sumar dos números
suma = lambda a, b: a + b
print(suma(3, 7))  # Salida: 10

# Función lambda para verificar si un número es par
es_par = lambda x: x % 2 == 0
print(es_par(4))  # Salida: True
print(es_par(5))  # Salida: False

# Uso de función lambda con map
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

# otro ejemplo
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [4, 5, 6, 7, 8]
suma_lists = list(map(lambda x, y: x + y, numbers1, numbers2))
print(suma_lists)  # Salida: [5, 7, 9, 11, 13]

