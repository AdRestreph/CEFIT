"""
Desarrolla un programa en Python que permita realizar operaciones entre matrices (arreglos bidimensionales) de números enteros,
utilizando un menú interactivo, y organizando el código mediante funciones.

MENU DEL PROGRAMA:
1. Llenar la Matriz A manualmente desde el teclado.
2. Llenar la Matriz B manualmente desde el teclado.
3. Calcular la Matriz C como la suma de A + B.
4. Calcular la Matriz D como la resta de B - A.
5. Mostrar una de las matrices (A, B, C o D).
6. Salir del programa.

Tenga en cuenta:
· El tamaño de las matrices (filas y columnas) debe ser definido por el usuario al momento de ingresarlas.
· Los datos deben ser capturados desde el teclado utilizando input () y validando las entradas mediante estructuras como while True y bloques try/except.
· El estudiante debe modularizar su código implementando funciones para:
o Ingresar matrices
o Realizar operaciones entre matrices (suma y resta)
o Mostrar matrices
· El programa debe ejecutarse de forma continua hasta que el usuario seleccione la opción 6 (Salir).
"""
# Se importan las funciones desde el archivo Funciones.py
from Funciones import ingresar_matriz, sumar_matrices, restar_matrices, mostrar_matriz, limpiar_consola
#Se inicializa la matriz A, B, C y D como None para su posterior uso
#Se inicializa la matriz A como none
matriz_A = None
#Se inicializa la matriz B como none
matriz_B = None
#Se inicializa la matriz C como none
matriz_C = None
#Se inicializa la matriz D como none
matriz_D = None
# Bucle principal del programa
while True:

    # Se muestra el menu de opciones
    print("""
MENU DEL PROGRAMA:
1. Llenar la Matriz A manualmente desde el teclado.
2. Llenar la Matriz B manualmente desde el teclado.
3. Calcular la Matriz C como la suma de A + B.
4. Calcular la Matriz D como la resta de B - A.
5. Mostrar una de las matrices (A, B, C o D).
6. Salir del programa.
""")
    # Se solicita al usuario seleccionar una opción
    opcion = input("Seleccione una opción: ")

    # Si la opcion es 1
    if opcion == "1":
        # Se ingresa la matriz A
        matriz_A = ingresar_matriz("A")
    # Si la opcion es 2
    elif opcion == "2":
        # Se ingresa la matriz B
        matriz_B = ingresar_matriz("B")
    # Si la opcion es 3
    elif opcion == "3":
        # Se verifica que las matrices A y B hayan sido ingresadas
        if matriz_A and matriz_B:
            # Se verifica que las matrices A y B tengan el mismo tamaño
            if len(matriz_A) == len(matriz_B) and len(matriz_A[0]) == len(matriz_B[0]):
                # matriz C es la suma de A y B
                matriz_C = sumar_matrices(matriz_A, matriz_B)
                # Imprime mensaje de exito
                print("\nMatriz C calculada correctamente.\n")
            # Sino tienen el mismo tamaño
            else:
                # Imprime mensaje de error
                print("\nERROR: Las matrices A y B deben tener el mismo tamaño.\n")
        # Sino han sido ingresadas las matrices A y B
        else:
            # Imprime mensaje de error
            print("\nDebe ingresar primero las matrices A y B.\n")

    # Si la opcion es 4
    elif opcion == "4":
        # Se verifica que las matrices A y B hayan sido ingresadas
        if matriz_A and matriz_B:
            # Se verifica que las matrices A y B tengan el mismo tamaño
            if len(matriz_A) == len(matriz_B) and len(matriz_A[0]) == len(matriz_B[0]):
                # matriz D es la resta de B y A
                matriz_D = restar_matrices(matriz_B, matriz_A)
                # Imprime mensaje de exito
                print("\nMatriz D calculada correctamente.\n")
            # Sino tienen el mismo tamaño
            else:
                # Imprime mensaje de error
                print("\nERROR: Las matrices A y B deben tener el mismo tamaño.\n")
        # Sino han sido ingresadas las matrices A y B
        else:
            # Imprime mensaje de error
            print("\nDebe ingresar primero las matrices A y B.\n")
    # Si la opcion es 5
    elif opcion == "5":
        # Se solicita al usuario cual matriz desea mostrar
        cual = input("¿Qué matriz desea mostrar? (A, B, C o D): ").upper()
        # Si se selecciona A
        if cual == "A":
            # Se utiliza la funcion para mostrar matriz para A
            mostrar_matriz(matriz_A, "A")
        # Si no si se selecciona B
        elif cual == "B":
            # Se utiliza la funcion para mostrar matriz para B
            mostrar_matriz(matriz_B, "B")
        # Si no si se selecciona C
        elif cual == "C":
            # Se utiliza la funcion para mostrar matriz para C
            mostrar_matriz(matriz_C, "C")
        # Si no si se selecciona D
        elif cual == "D":
            # Se utiliza la funcion para mostrar matriz para D
            mostrar_matriz(matriz_D, "D")
        # Sino se selecciona una opcion valida
        else:
            # Imprime mensaje de opcion invalida
            print("Opción inválida.")
    # Si la opcion es 6
    elif opcion == "6":
        # Se imprime mensaje de finalizacion del programa
        print("\n¡Programa finalizado!\n")
        # Se rompe el bucle para salir del programa
        break
    # Sino se selecciona una opcion valida
    else:
        # Imprime mensaje de opcion invalida
        print("\nOpción inválida. Intente nuevamente.\n")

    # Se limpia la consola al iniciar cada iteración del bucle
    limpiar_consola()