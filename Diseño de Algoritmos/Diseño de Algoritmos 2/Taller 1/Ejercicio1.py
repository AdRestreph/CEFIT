"""
Crea un programa donde implementes una funcion para calcular
las principales operaciones aritmeticas de dos numeros, la funcion tendra
tres parametros (operacion, num1, num2) y debe devolver el resultado de
la operacion aritmetica indicada en el argumento.
Deberas tener en cuenta la division por cero (error, division por cero).
"""
## Se importa el OS
import os
## Funcion para limpiar consola
def limpiar_Consola():
    ## metodo para limpiar consola en windows
    os.system('cls')
## Se define la funcion con 3 parametros y sus respectivos tipos de datos y el retorno esperado
def calcular(operacion:str, num1:float, num2:float):
    ## Primera condicion (suma), si operacion es 1 suma los 2 numeros
    if operacion == '+':
        resultado = num1 + num2
    ## Segunda condicion (resta), si operacion es 2 resta los 2 numeros
    elif operacion == '-':
        resultado = num1 - num2
    ## Tercera condicion (multiplicacion), si operacion es 3 multiplica los 2 numeros
    elif operacion == '*':
        resultado = num1 * num2
    ## Cuarta condicion (division), si operacion es 4 divide los 2 numeros siempre y cuando pase la validacion de que el num2 no sea 0
    elif operacion == '/':
        if num2 != 0:
            resultado = num1 / num2
        ## En caso de num2, muestra un error correspondiente
        else:
            return '(Error) Indeterminacion'
    ## Si no se cumple ninguna de las condiciones anteriores se asume que es un error de digitacion
    else:
        return '(Error) Seleccione una opcion valida.'
    return resultado

## Se hace un input donde se da un indice para cada operacion (Tambien se podria hacer con un indice correspondiente para cada operacion)
operador = input(" -> (+) Suma\n -> (-) Resta\n -> (*) Multiplicacion\n -> (/) Division\n Ingrese el indice del operador que desea calcular: ")
## Se hacen 2 input, para num1 y num2 para realizar la operacion
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
## Se limpia la consola con la funcion para que sea mas visible el resultado
limpiar_Consola()
## Se imprime el resultado
print(f'Resultado: {num1} {operador} {num2} = {calcular(operador, num1, num2)}')
