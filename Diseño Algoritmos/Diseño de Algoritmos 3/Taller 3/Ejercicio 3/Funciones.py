"""Funciones para manejo de matrices: ingreso, suma, resta y visualización."""
# Se importa la libreria os para limpiar la consola
import os
# Funcion para limpiar la consola
def limpiar_consola():
    # Comando para limpiar la consola
    os.system('cls')
    # Se limpia la consola al iniciar el programa
limpiar_consola()
# Se define la funcion ingresar matriz desde teclado
def ingresar_matriz(nombre):
    """Solicita al usuario el tamaño y los valores de una matriz."""
    # Encabezado de ingreso de datos
    print(f"\n--- Ingresar datos para la Matriz {nombre} ---")
    # Ciclo para ingresar filas con validacion
    while True:
        # Intenta obtener una entrada valida para filas
        try:
            # Se define filas para almacenar el numero de filas
            filas = int(input("Ingrese el número de filas: "))
            # Verifica que filas sea mayor que 0
            if filas > 0:
                # Si es valido, sale del ciclo
                break
            # Sino es valido, muestra mensaje y continua el ciclo
            print("El número debe ser mayor que 0.")
        # Captura error de valor no entero
        except ValueError:
            # Muestra mensaje de error
            print("Entrada inválida. Ingrese un número entero.")
    # Ciclo para ingresar filas con validacion
    while True:
        # Intenta obtener una entrada valida para columnas
        try:
            # Se define columnas para almacenar el numero de columnas
            columnas = int(input("Ingrese el número de columnas: "))
            # Verifica que columnas sea mayor que 0
            if columnas > 0:
                # Si es valido, sale del ciclo
                break
            # Sino es valido, muestra mensaje y continua el ciclo
            print("El número debe ser mayor que 0.")
        # Captura error de valor no entero
        except ValueError:
            # Muestra mensaje de error
            print("Entrada inválida. Ingrese un número entero.")
    # Crear matriz vacía
    matriz = []
    # Ciclo para ingresar los valores de la matriz
    for f in range(filas):
        # Lista para almacenar la fila actual
        fila = []
        # Ciclo para ingresar los valores de cada columna
        for c in range(columnas):
            # Ciclo para validar la entrada de cada valor
            while True:
                # Intenta obtener una entrada valida para el valor de la matriz
                try:
                    # Solicita el valor para la posición [fila][columna]
                    valor = int(input(f"Valor en posición [{f}][{c}]: "))
                    # Agrega el valor a la fila actual
                    fila.append(valor)
                    # Sale del ciclo de validación
                    break
                # Captura error de valor no entero
                except ValueError:
                    # Muestra mensaje de error
                    print("Entrada inválida. Ingrese un número entero.")
        # Agrega la fila completa a la matriz
        matriz.append(fila)
    # Imprime mensaje de confirmación
    print(f"\nMatriz {nombre} ingresada correctamente.\n")
    # Retorna la matriz ingresada
    return matriz

# Funcion para sumar dos matrices
def sumar_matrices(A, B):
    """Retorna la matriz suma A + B."""
    # Obtiene el numero de filas
    filas = len(A)
    # Obtiene el numero de columnas
    columnas = len(A[0])
    # Se define C para almacenar la matriz suma
    C = []
    # Ciclo para sumar las matrices
    for f in range(filas):
        # Lista para almacenar la fila actual
        fila = []
        # Ciclo para sumar cada columna
        for c in range(columnas):
            # Agrega la suma de los elementos correspondientes a la fila actual
            fila.append(A[f][c] + B[f][c])
        # Agrega la fila completa a la matriz suma
        C.append(fila)
    # Retorna la matriz suma
    return C

# Funcion para restar dos matrices
def restar_matrices(B, A):
    """Retorna la matriz resta B - A."""
    # Obtiene el numero de filas
    filas = len(A)
    # Obtiene el numero de columnas
    columnas = len(A[0])
    # Se define D para almacenar la matriz resta
    D = []
    # Ciclo para restar las matrices
    for f in range(filas):
        # Lista para almacenar la fila actual
        fila = []
        # Ciclo para restar cada columna
        for c in range(columnas):
            # Agrega la resta de los elementos correspondientes a la fila actual
            fila.append(B[f][c] - A[f][c])
        # Agrega la fila completa a la matriz resta
        D.append(fila)
    # Retorna la matriz resta
    return D

# Se define la funcion para mostrar una matriz
def mostrar_matriz(Matriz, nombre):
    """Muestra una matriz con formato claro."""
    # Verifica si la matriz ha sido creada
    if Matriz is None:
        # Si no ha sido creada, muestra mensaje y retorna
        print(f"\nLa matriz {nombre} no ha sido creada aún.\n")
        return
    #  Imprime el encabezado de la matriz
    print(f"\n--- Matriz {nombre} ---")
    # Ciclo para imprimir cada fila de la matriz
    for fila in Matriz:
        # Imprime los elementos de la fila separados por espacios
        print(" ".join([str(x) for x in fila]))
