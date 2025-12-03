"""
Se cuenta con un arreglo unidimensional ( Lista ) que contiene temperaturas registradas en grados Celsius en siete ciudades durante el mediodía:
temp_celsius = [0, 20, 37, 40,35,27,45]

Se pide:
a) Utilizar la función map () en combinación con una función lambda para convertir todas las temperaturas a grados Fahrenheit. Recuerda la fórmula de conversión:
F = C * 9/5 + 32
b) Mostrar el nuevo arreglo unidimensional con las temperaturas ya convertidas a Fahrenheit.
c) Ordenar las temperaturas de mayor a menor utilizando la función sorted() y mostrar el resultado en el siguiente formato:
Las temperaturas convertidas a grados Fahrenheit son:
--- T1
--- T2
--- T3
--- T4
"""
# Se importa la libreria os para limpiar la consola
import os
# Función para limpiar la consola
def limpiar_consola():
    # Comando para limpiar la consola
    os.system('cls')
# Se limpia la consola al iniciar el programa
limpiar_consola()
# Arreglo unidimensional con temperaturas en grados Celsius
temp_celsius = [0, 20, 37, 40,35,27,45]
# se define la función lambda para convertir Celsius a Fahrenheit
convertir_fahrenheit = lambda c: c * 9/5 + 32
# Se utiliza map para aplicar la función de conversión a cada elemento del arreglo
temp_fahrenheit = list(map(convertir_fahrenheit, temp_celsius))
# Se ordenan las temperaturas en Fahrenheit de mayor a menor usando sorted
temp_fahrenheit = sorted(temp_fahrenheit, reverse=True)
# Se muestra el resultado en el formato solicitado
print("Las temperaturas convertidas a grados Fahrenheit son:")
# Se itera sobre las temperaturas convertidas
for temp in temp_fahrenheit:
    #Se imprime cada temperatura con el formato solicitado
    print(f'--- {temp:.1f} °F')