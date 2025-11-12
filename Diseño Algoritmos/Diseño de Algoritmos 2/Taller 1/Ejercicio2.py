"""
Crea un programa donde implementes una funcion para contar las vocales
y consonantes de un rexto, palabra o parrafo ingresado, la funcion debe
devolver un mensaje que indique el numero de vocales y numero de consonantes
del texto ingresado
"""
## importo el OS que ayuda a limpir la consola
import os
## Creo una funcion para limpiar la consola
def limpiar_Consola():
    os.system('cls')
## se crea la funcion con un parametro de entrada str y retorno str
def contar_letras(texto:str)->str:
    ## Variables vacias que vna almacenar el contador de vocales y consonantes
    c_vocales = 0
    c_consonantes = 0
## ciclo for para recorrer el texto
    for caracter in texto:
        ## condicion con isalpha para verificar si todos los caracteres son letras del alfabeto
        if caracter.isalpha():
            #condicion, si el caracter esta en el str 'aeiouáéíóú' suma al contador de vocales 1
            if caracter in 'aeiouáéíóú':
                #contador de vocales
                c_vocales +=1
            #si no se cumple la condicion anterior suma a contador de consonantes
            else:
                #contador de consonantes
                c_consonantes += 1
    ## el retorno de la funcion
    return print(f'El texto tiene: {c_vocales} vocales y {c_consonantes} consonantes')

#input para ingresar el texto
texto = input("Ingrese un texto: ")
#funcion para limpiar consola y solo ver el resultado
limpiar_Consola()
#Llamado de funcion para ver el resultado
contar_letras(texto)