"""
Escribe una función Analizar (estudiantes1, estudiantes2) que reciba dos conjuntos de nombres de estudiantes. La función deberá retornar un diccionario con la siguiente información:
a) Un conjunto de estudiantes que estén en ambos grupos
b) Un conjunto de estudiantes que solo están en el primer grupo
c) Un conjunto de estudiantes que solo están en el segundo grupo
d) Un conjunto de todos los estudiantes.

REQUISITOS
a) Los nombres de los estudiantes deben ser ignorados en cuanto a mayúsculas/minúsculas (Juan/JUAN) deben ser considerados el mismo nombre.
b) Debes tener una segunda función para el ingreso y validación de datos de los estudiantes:

Validaciones:
a) El nombre no debe estar vacío. Inténtelo de nuevo.
b) El nombre no puede contener números. Inténtelo de nuevo.
c) Al ingresar un estudiante, debe aparecer un mensaje en pantalla: ingrese el nombre del estudiante número 1 o fin para terminar.
Mostrar ordenado y adecuadamente los resultados obtenidos, NO MOSTRARLOS EN FORMA DE CONJUNTO (HACER UN RECORRIDO DEL ITERABLE Y PRESENTAR LA INFORMACIÓN).
"""
# se importa os para limpiar la consola
import os
# Se define la funcion limpiar consola
def limpiar_consola():
    # Se usa el comando apra limpiar la consola
    os.system('cls')
# Se define la funcion analizar
def analizar(estudiantes1:set,estudiantes2:set)->dict:
    # Intersección: Estudiantes en ambos grupos
    ambos = estudiantes1.intersection(estudiantes2)
    # Diferencia: Solo en el primer grupo
    solo_primero = estudiantes1.difference(estudiantes2)
    # Diferencia: Solo en el segundo grupo
    solo_segundo = estudiantes2.difference(estudiantes1)
    # Union: Todos los estudiantes
    todos = estudiantes1.union(estudiantes2)
    # Retornamos el diccionario
    return {
        # Retorna la interseccion
        "ambos": ambos,
        # Retorna solo el primer grupo
        "solo_primero": solo_primero,
        # Retorna solo el segundo grupo
        "solo_segundo": solo_segundo,
        # Retorna ambos grupos
        "todos": todos
    }
# se define la funcion mostrar lista, que recibe un titulo y un conjunto
def mostrar_lista(titulo, conjunto):
    # imprime el titulo
    print(f"\n{titulo}:")
    # condicional Si no hay conjunto
    if not conjunto:
        #Imprime ninguno
        print("  (Ninguno)")
    # sino sucede lo anterior
    else:
        # Itera nombre ordenando son sorted sobre conjunto
        for nombre in sorted(conjunto):
            #imprime el nombre
            print(f"  - {nombre}")

# se define la funcion para ingresar los estudiantes a cada grupo
def ingresar_estudiantes(numero_grupo):
    # Se define estudiantes como set
    estudiantes = set()
    # se define un contador
    contador = 1
    # se imprime el grupo que se esta solicitando
    print(f"\n--- Ingreso de estudiantes para el GRUPO {numero_grupo} ---")
    # se crea un ciclo
    while True:
        # se define entrada y almacena el input temporalmente
        entrada = input(f"Ingrese el nombre del estudiante número {contador} o 'fin' para terminar: ").strip()
        # Condición de salida si se escribe fin
        if entrada.lower() == 'fin':
            #rompe el ciclo
            break
        # Validacion a: No estar vacio
        if not entrada:
            #Imprime un mensaje de error
            print("Error: El nombre no debe estar vacío. Inténtelo de nuevo.")
            continue

        # Validación b: No contener números
        # Usamos any() con isdigit() para detectar si hay algún número en la cadena
        if any(char.isdigit() for char in entrada):
            print("Error: El nombre no puede contener números. Inténtelo de nuevo.")
            continue

        # Requisito de mayusculas/minusculas:
        # Guardamos el nombre en formato title
        # y que el set elimine duplicados automaticamente ignorando el case original.
        estudiantes.add(entrada.title())
        # aumenta el contador
        contador += 1
    #retorna el conjunto estudiantes
    return estudiantes

# se establece el grupo 1
grupo1 = ingresar_estudiantes(1)
# Se establece el grupo 2
grupo2 = ingresar_estudiantes(2)

# Análisis de los datos
resultados = analizar(grupo1, grupo2)
# Se limpia la consola para imprimir los resultados
limpiar_consola()
# se crea un "baner" para la presentacion de resultados (Recorrido del iterable)
print("\n" + "=" * 40)
print("RESULTADOS DEL ANÁLISIS")
print("=" * 40)
#Se utiliza la funcion mostrar lista para imprimir de manera ordenada
mostrar_lista("a) Estudiantes que están en AMBOS grupos", resultados["ambos"])
#Se utiliza la funcion mostrar lista para imprimir de manera ordenada
mostrar_lista("b) Estudiantes que SOLO están en el grupo 1", resultados["solo_primero"])
#Se utiliza la funcion mostrar lista para imprimir de manera ordenada
mostrar_lista("c) Estudiantes que SOLO están en el grupo 2", resultados["solo_segundo"])
#Se utiliza la funcion mostrar lista para imprimir de manera ordenada
mostrar_lista("d) TODOS los estudiantes (lista general)", resultados["todos"])