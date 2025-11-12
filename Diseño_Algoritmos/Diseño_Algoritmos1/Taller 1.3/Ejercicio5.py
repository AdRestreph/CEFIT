nombre = input('Ingresa tu nombre: ') #1: Int no se usa para una cadena de texto en un input

if nombre == "Maria":#2: Python es case sensitive, necesita que la variable nombre sea igual a como se define
                        #3: El operador de comparacion es ==
    print('Hola Maria')

elif nombre == "Carlos":#4: elif debe ser bien escrito para funcionar
                        #5: la variable nombre nuevamente mal escrita
    print("Hola Carlos")

elif nombre == 'Juan':
    print("Hola Juan")  #6: imprimia un mensaje incorrecto

else:#7: else no lleva condición
    print("No te tengo en mis registros")#8: Las triplecomillas sobraban
