"""
1. Crea una lista con todos los países de Latinoamérica y otra lista con sus respectivas poblaciones, con base a esto vas a generar:
a) un listado de países con las poblaciones mayores a 20 millones de habitantes.
b) un listado de países con las poblaciones mayores a 20 millones de habitantes.
nota: presenta de manera detallada y bien organizada cada una de las listas generadas, utilizado dict comprehension. VALOR (25%)
"""
#se importa os para limpiar la consola
import os
# se hace una funcion para ordenar los diccionarios de mayor a menor
def imprimir_orden_mayor_menor(diccionario: dict):
    # Se itera con enumerate para obtener un contador "i" junto con la clave y el valor del diccionario ordenado
    # Se usa la funcion sorted y key lambda para ordenar el diccionario por el valor (poblacion)
    for i, (clave, valor) in enumerate(sorted(diccionario.items(), key=lambda x: x[1], reverse = True)):
        #en cada recorrido imprime de mayor a menor la clave y el valor del dict
        print(f'--- [{i+1}] {clave} : {valor}')
# se define una funcion para limpiar la consola
def limpiar_consola():
    # comando para limpiar la consola
    os.system('cls')
# se define una lista de paises
paises_latam = [
    "Brasil", "México", "Colombia", "Argentina", "Perú", "Venezuela",
    "Chile", "Guatemala", "Ecuador", "Bolivia", "Haití",
    "República Dominicana", "Cuba", "Honduras", "Paraguay",
    "Nicaragua", "El Salvador", "Costa Rica", "Panamá", "Uruguay",
    "Jamaica", "Trinidad y Tobago", "Guyana", "Surinam", "Belice",
    "Bahamas", "Barbados", "Santa Lucía", "Granada",
    "San Vicente y las Granadinas", "Antigua y Barbuda",
    "Dominica", "San Cristóbal y Nieves"
]
# se define una lista de poblaciones que corresponden a cada pais
poblaciones = [
    212_812_405, 131_946_900, 53_425_635, 45_851_378, 34_576_665,
    28_516_896, 19_859_921, 18_687_881, 18_135_478, 12_413_315,
    11_772_557, 11_427_557, 10_979_783, 10_825_703, 6_929_153,
    6_916_140, 6_338_193, 5_129_910, 4_515_577, 3_386_588,
    2_839_175, 1_507_782, 831_087, 634_431, 417_072,
    401_283, 282_467, 180_149, 117_303,
    99_924, 94_209, 65_871, 46_922
]
# Utilizando comprenhentions se relaciona una lista de poblaciones y paises
# Se itera para agregar a este dict si es menor a 20 millones
paises_poblaciones_menores_20 = {paises_latam: poblaciones for paises_latam, poblaciones in zip(paises_latam, poblaciones) if poblaciones < 20_000_000}
## Se itera para agregar a este dict si es mayor o igual a 20 millones
paises_poblaciones_mayores_20 = {paises_latam: poblaciones for paises_latam, poblaciones in zip(paises_latam, poblaciones) if poblaciones >= 20_000_000}
# Se limpia la consola antes de mostrar los resultados
limpiar_consola()
# Se imprime un mensaje indicativo de los paises con poblacion menor
print("\nPAISES CON POBLACION MENOR A 20 MILLONES\n")
#Se usa la funcion para imprimir cada elemento
imprimir_orden_mayor_menor(paises_poblaciones_menores_20)
# Se imprime un mensaje indicativo de los paises con poblacion mayor
print("\nPAISES CON POBLACION MAYOR A 20 MILLONES\n")
#Se usa la funcion para imprimir cada elemento
imprimir_orden_mayor_menor(paises_poblaciones_mayores_20)


