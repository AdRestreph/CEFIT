"""
Calculadora de propinas.
Escribe un programa que calcule el total a pagar en un restaurante
incluyendo una propina.
Para ello, crea una funcion llamada calcular_propina
que reciba dos parametros: El monto de la cuenta (un numero decimal)
y el porcentaje de la cuenta (un numero decimal) y devuelva el valor
de la propina.
Luego, diseña otra funcion llamada total_con_propina, que utilice
la funcion anterior para sumar el monto de la cuenta y la propina,
devolviendo el total a pagar.

Finalmente, crea una funcion mostrar_total que reciba el monto de la cuenta
y el porcentaje de propina, y que imprima el subtotal, el valor de la propina
y el total a pagar, todos con formato de 2 decimales
"""
#Se importa el OS para crear la funcion de limpiar la consola
import os
#Se crea la funcion de limpiar la consola
def limpiar_Consola():
    #Comando solo para windows
    os.system('cls')
#Se crea la funcion calcular propina con 2 parametros, monto y porcentaje
def calcular_propina(monto:float,porcentaje:float)->float:
    #Retorna directamente la operacion requerida sin almacenar una variable en memoria
    return monto * porcentaje /100
#Se crea funcion para sumar el monto de la cuenta mas la propina con 2 parametros de entrada y se usa la funcion anterior para calcularlo
def total_con_propina(monto:float,porcentaje:float)->float:
    # Se suma el monto y la funcion para calcular el total con propina
    return monto + calcular_propina(monto,porcentaje)
#Se crea la tercera funcion, que reune las 2 funciones anteriores para dar un resultado total de la cuenta de forma detalla
def mostrar_total(monto:float,porcentaje:float)->str:
    #se utiliza el f{} para dar un solo print y establecer el formato de 2 decimales
    return print(f'Porcentaje de propina: {porcentaje:.2f}%\nSubtotal: {monto:.2f}\nValor de propina:{calcular_propina(monto,porcentaje):.2f} \nTotal: {total_con_propina(monto,porcentaje):.2f}')

#se solicita el valor de la cuenta con un input
monto = float(input("Ingrese el monto a pagar: "))
#se solcita el valor del procentaje en propina con respecto a la cuenta que va a pagar
porcentaje = float(input("Ingrese el porcentaja de propina: "))
#Se usa la tercera funcion que contiene todos los resultados anteriores
mostrar_total(monto,porcentaje)
