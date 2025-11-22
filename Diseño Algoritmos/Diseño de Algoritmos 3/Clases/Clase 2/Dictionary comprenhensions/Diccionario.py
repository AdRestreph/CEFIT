import random
# Crear un diccionario
diccionario = {}
for i in range (1,11):
    diccionario[i] = i**2
print(diccionario)

# Usando dictionary comprehension
diccionario2 = {i: i**2 for i in range(1,11)}
print(diccionario2)

# Ejemplo 2

paises = ['Colombia', 'Argentina', 'Brasil', 'Chile']
population = {}

for i in range(len(paises)):
    population[paises[i]] = random.randint(10000000,50000000)
print(population)

# Usando dictionary comprehension
population2 = {pais: random.randint(10000000,50000000) for pais in paises}
print(population2)


poblacion_latam = [45, 38, 213, 19, 23, 42, 32, 35]  # Poblacion en millones
paises_latam = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Paraguay', 'Peru']

paises_latam_20 = {paises_latam: poblacion_latam for paises_latam, poblacion_latam in zip(paises_latam, poblacion_latam) if poblacion_latam < 20}
print(paises_latam_20)

pases_latam_30 = {paises_latam: poblacion_latam for paises_latam, poblacion_latam in zip(paises_latam, poblacion_latam) if poblacion_latam > 30 and poblacion_latam < 50}
print(pases_latam_30)

