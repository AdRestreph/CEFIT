"""Desarrolla un programa que calcule el perímetro y el área de un rectángulo. El programa debe solicitar al usuario ingresar la longitud y el ancho del rectángulo."""

def calcular_perimetro(altura, base)->float:
    return 2*(altura + base)

def calcular_area(altura, base)->float:
    return altura * base

altura = float(input("Ingresa la altura (H) del rectangulo: "))
base = float(input("Ingresa la base (B) del rectangulo: "))

print(f'El area del rectangulo es: {calcular_area(altura, base)} \n El perimetro del rectangulo es: {calcular_perimetro(altura, base)}')