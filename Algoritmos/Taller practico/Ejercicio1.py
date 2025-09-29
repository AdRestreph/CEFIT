"""
Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal.
"""

def Identificar_Vocal(letra:str):
    """
    Devuelve un mensaje dependiendo si es vocal o no, o si es otro caracter
    
    Parametros
    -----------------------------
    Entrada: Letra(Str)
    -----------------------------
    """
    
    vocales = {'a','e','i','o','u'}
    if letra.lower() in vocales:
        print("Es una vocal")
    else:
        print("No es una vocal")
        

while True:
    letra = input("Ingrese una letra: ")
    if len(letra) != 1:
        print("Ingrese un solo caracter")
    else:
        Identificar_Vocal(letra)
    

