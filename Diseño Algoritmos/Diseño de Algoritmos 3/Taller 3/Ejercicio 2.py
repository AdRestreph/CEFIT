"""
Se cuenta con un arreglo unidimensional de tuplas (Lista de Tuplas), donde cada tupla representa el nombre de una ciudad y su temperatura registrada en grados fahrenheit durante el mediodía:
Temp_Fahrenheit= [ ("envigado", 78.8 ), ("Itagüí", 57.2), ("la estrella", 86), ("caldas", 53.6) ]
Se pide:
a) Utilizar la función map() con una función lambda para convertir las temperaturas de cada ciudad de grados Fahrenheit a grados Celsius. La nueva estructura debe mantener el nombre
de la ciudad y su temperatura en Celsius.

Ejemplo de salida esperada (lista de tuplas):
[("Envigado", 32.0), ("Itagüí", 68.0), ...]
b) Mostrar el nuevo arreglo unidimensional con las temperaturas convertidas.
c) Ordenar las ciudades de mayor a menor temperatura en Fahrenheit utilizando sorted() con lambda.
d) Mostrar el resultado final con el siguiente formato:
Temperaturas en Fahrenheit (ordenadas de mayor a menor):
--- Caldas: 212.0 °C
--- La Estrella: 98.6 °C
--- Itagüí: 68.0 °C
--- Envigado: 32.0 °C
"""
# Se importa os para limpiar la consola
import os
# Función para limpiar la consola
def limpiar_consola():
    # Comando para limpiar la consola
    os.system('cls')
# Se limpia la consola al iniciar el programa
limpiar_consola()
# Arreglo unidimensional de tuplas con temperaturas en grados Fahrenheit
Temp_Fahrenheit= [ ("envigado", 78.8 ), ("Itagüí", 57.2), ("la estrella", 86), ("caldas", 53.6) ]
# Definición de la funcion lambda para convertir Fahrenheit a Celsius y formatear el nombre de la ciudad
convertir_celsius = lambda ciudad_temp: (ciudad_temp[0].title(), (ciudad_temp[1] - 32) * 5/9)
# Uso de map para aplicar la funcion de conversion a cada tupla en el arreglo
Temp_Celsius = list(map(convertir_celsius, Temp_Fahrenheit))
# Ordenar las temperaturas en Celsius de mayor a menor usando sorted con lambda
Temp_Celsius = sorted(Temp_Celsius, key=lambda x: x[1], reverse=True)
# Mostrar el resultado en el formato solicitado
print("Temperaturas en Celcius (ordenadas de mayor a menor):")
# Iterar sobre las tuplas de ciudad y temperatura en Celsius
for ciudad, temp in Temp_Celsius:
    # Imprimir cada ciudad con su temperatura en el formato solicitado
    print(f'--- {ciudad}: {temp:.1f} °C')