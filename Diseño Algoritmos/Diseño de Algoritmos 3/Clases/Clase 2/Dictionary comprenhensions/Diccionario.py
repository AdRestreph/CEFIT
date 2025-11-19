# Crear un diccionario

diccionario = {}
for i in range (1,11):
    diccionario[i] = i**2
print(diccionario)

# Usando dictionary comprehension
diccionario2 = {i: i**2 for i in range(1,11)}
print(diccionario2)