"""Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit."""

def conversion_temperatura(celcius: float) -> float:
    return celcius * 9 / 5 + 32

celsius = float(input("Ingresa una temperatura en grados Celsius: "))

print(f'{celsius}°C son {conversion_temperatura(celsius)} °F')
