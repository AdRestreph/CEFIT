"""
Un estudiante ha obtenido tres notas en sus exámenes parciales. Escribe un programa que
solicite al usuario ingresar las tres notas y calcule el promedio.
Luego, muestra en pantalla un mensaje indicando el nombre y apellido del estudiante, asignatura y promedio obtenido.
"""

def promedio(notas: list) -> float:
    return sum(notas) / len(notas)

materias = {}
notas = []

nombres = input("Ingrese nombres y apellidos: ")
materia = input("Ingrese el nombre de la materia: ")

for i in range(3):
    nota = float(input(f"Ingrese la nota del parcial {i + 1}: "))
    notas.append(nota)

materias[materia] = notas

print(materias)
print(f'El estudiante {nombres} tiene un promedio de {promedio(notas)} en la materia {next(iter(materias))}')