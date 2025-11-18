"""
1. Escribe una función analizar_estudiantes (estudiantes1, estudiantes2)
que reciba dos conjuntos de nombres de estudiantes. La función deberá retornar un diccionario con la siguiente información:
a. Un conjunto de estudiantes que están en ambos grupos.
b. Un conjunto de estudiantes que están solo en el primer grupo.
c. Un conjunto de estudiantes que están solo en el segundo grupo.
d. Un conjunto de todos los estudiantes.
"""
#se importa os para crear una funcion y limpiar la consola
import os
#se define la funcion para limpiar la consola
def limpiar_consola():
    #comando para limpiar la consola
    os.system('cls')

#Se define la funcion que nos piden inicialmente para operar con conjuntos, la cual recibe 2 sets y retorna un diccionario
def analizar_estudiantes(estudiantes1:set, estudiantes2:set) -> dict:
    #Retorno de datos solicitados
    return {
        # se realiza la operacion & para validar los estudiantes en ambos grupos
        'En ambos grupos': estudiantes1.intersection(estudiantes2),
        #se realiza la diferencia entre estudiante 1 y 2 para ver solo los del grupo 1
        'Solo en grupo 1': estudiantes1.difference(estudiantes2),
        ##se realiza la diferencia entre estudiante 1 y 2 para ver solo los del grupo 2
        'Solo en grupo 2': estudiantes2.difference(estudiantes1),
        #se realiza la operacion | para unir ambos grupos de estudiantes
        'Todos los estudiantes': estudiantes1.union(estudiantes2)
    }

# se define una funcion que solicita el numero del grupo que se va a ingresar que tiene un numero entero como parametro y retorna un set
def solicitar_grupo(numero_grupo: int)-> set:
    #se declara una variable grupo con el tipo de dato set
    grupo = set()
    #Imprime grupo y el numero del grupo que recibe la funcion
    print(f'GRUPO {numero_grupo}')
    #Imprime un mensaje guia para el usuario
    print("Ingrese nombres (presione Enter sin texto para finalizar):")

    # Se crea un ciclo para ingresar una cantidad indeterminada de estudiantes
    while True:
        #se declara el input especificando el grupo al cual le esta ingresando los datos y se utiliza strip para eliminar los espacios
        nombre = input(f'Estudiante del grupo {numero_grupo}: ').strip()
        #se crea una condicion que cuando nombre este vacio rompa el ciclo
        if not nombre:
            #rompe el ciclo
            break
        #si no se cumple la condicion anterior verifica si el nombre ya fue agregado al conjunto para advertir al usuario
        if nombre in grupo:
            print(f'{nombre} ya fue ingresado en el conjunto')
        #Sino entonces el nombre es agregado a el grupo
        else:
            #agrega el nombre al conjunto
            grupo.add(nombre)
            #Imprime el numero de estudiantes agregados al grupo
            print(f'Agregado.\nTotal: {len(grupo)} estudiante(s)')
    #retorna el conjunto
    return grupo

#se define una funcion para mostrar los resultados de manera mas ordenada la cual recibe un diccionario como parametro
def mostrar_resultados(resultados: dict):
    #Se imprime un mensaje informativo
    print("RESULTADOS")
    # se crea un ciclo para aceder a las claves del diccionario y a los valores
    for clave, valores in resultados.items():
        #Se imprime la clave del diccionario
        print(f"\n{clave}:")
        # valida si hay algo en los valores esperando que retorne true o false
        if valores:
            #si retorna true
            #se hace un ciclo que ordena los valores del conjunto temporalmente para facilitar la legibilidad
            for estudiante in sorted(valores):
                #imprime el estudiante
                print(f"{estudiante}")
        #si retorna false
        else:
            #imprime ninguno
            print("(ninguno)")

#Aca se crean 2 variables que van a almacenar los datos de la funcion para luego poder operar los conjuntos
#Se define el grupo 1
grupo1 = solicitar_grupo(1)
#Se define el grupo 2
grupo2 = solicitar_grupo(2)
# Se limpia la consola utilizando la funcion para mas legibilidad
limpiar_consola()

#Valida si no hay nada en grupo 1 Y en grupo2
if not grupo1 and not grupo2:
    print("No se ingresaron estudiantes en ningún grupo")
#Si no se cumple se utiliza la funcion analizar_estudiantes para operar con los conjuntos
else:
    #se define resultado que le pasa los 2 sets que tiene como parametro para luego utilizarla en la funcion que ordena los resultado
    resultados = analizar_estudiantes(grupo1, grupo2)
    #Se utiliza la funcion para mostrar los resultados de manera mas ordenada
    mostrar_resultados(resultados)
