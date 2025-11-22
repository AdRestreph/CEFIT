"""
Convierta una lista de temperaturas dadas en grados celsius a grados fahrenhteit
utilizando la funcion map y una funcion lambda
La formula de conversion es F = C * 9/5 + 32
"""
celsius = [0, 10, 20, 30, 40, 50]
fahrenheit_tradicional = []

# tradicional

for i in range(len(celsius)):
    fahrenheit = celsius[i] * 9/5 + 32
    print(f'{celsius[i]}°C = {fahrenheit}°F')
    fahrenheit_tradicional.append(fahrenheit)

for i in range(len(fahrenheit_tradicional)):
    print(fahrenheit_tradicional[i])

# Usando map y lambda

fahrenheit_lamda = list(map(lambda c: c * 9/5 + 32, celsius))
for i in range(len(fahrenheit_lamda)):
    print(f'{celsius[i]}°C = {fahrenheit_lamda[i]}°F')

for i in range(len(fahrenheit_lamda)):
    print(fahrenheit_lamda[i])

print(fahrenheit_lamda)