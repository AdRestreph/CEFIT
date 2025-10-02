# Importamos el módulo os para poder ejecutar comandos del sistema operativo
import os

"""
Programa de votación.
Permite al usuario elegir un candidato por el cual votar.
Opciones: 
- Candidato Taller 1.2 → Partido rojo
- Candidato B → Partido verde
- Candidato C → Partido azul
Si el usuario ingresa una opción incorrecta, se muestra "Opción errónea".
"""

# Definición de función para limpiar la terminal
def limpiar_terminal():
    os.system('cls') # Ejecuta el comando 'cls' en Windows para limpiar la pantalla

# Definimos una función para registrar el voto según el candidato elegido
def votar(candidato: str) -> str:
    """
    Retorna el mensaje según el candidato elegido.
    
    Parámetros
    ----------
    candidato : str
        Letra del candidato elegido (Taller 1.2, B, C o D)
    
    Retorna
    -------
    str
        Mensaje indicando el partido correspondiente o error si la opción es inválida
    """
    # Convertimos la letra ingresada a mayúscula para evitar errores con minúsculas
    candidato = candidato.upper()

    # Verificamos qué candidato eligió el usuario y retornamos el mensaje correspondiente
    if candidato == "Taller 1.2":
        return "Usted ha votado por el partido rojo"
    elif candidato == "B":
        return "Usted ha votado por el partido verde"
    elif candidato == "C":
        return "Usted ha votado por el partido azul"
    elif candidato == "D":
        return "Usted ha votado en blanco"  # Opción para votar en blanco
    else:
        return "Opción errónea"  # Si el usuario ingresó cualquier otra letra

# Solicitamos al usuario que ingrese la letra del candidato
candidato = input("Ingrese la letra del candidato por el que desea votar (Taller 1.2(Partido rojo), B(Partido verde), C(Partido azul), D(Voto en Blanco)): \n")

# Limpiamos la terminal para mostrar el resultado
limpiar_terminal()
# Mostramos el resultado del voto usando la función votar()
print(votar(candidato), "\n")
# Mensaje final indicando que la aplicación se cerró
print("\nCerrando aplicación\n")
