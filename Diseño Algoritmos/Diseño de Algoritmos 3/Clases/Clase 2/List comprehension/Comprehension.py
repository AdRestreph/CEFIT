# Tradicionalmente

lista1 = []
for i in range(10):
    lista1.append(i)
print(lista1)

# Usando list comprehension
lista2 = [i for i in range(10)]
print(lista2)
# lista = [elemento for elemento in iterable]

# Condicional en list comprehension
lista3 = [i for i in range(1,11) if i % 2 == 0]
print(lista3)

km = [10, 20, 30, 40, 50]
metros = [i*1000 for i in km]
print(f'Metros: {metros}')

