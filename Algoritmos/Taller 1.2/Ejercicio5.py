"""Una tienda ofrece un descuento del 15% sobre el total de la compra.
Escribe un programa que solicite al usuario ingresar el monto total de su compra y calcule el monto final a pagar después de aplicar el descuento.
Muestra un mensaje en pantalla indicando el nombre y apellido del cliente, el valor a pagar sin descuento y el valor final a pagar teniendo en cuenta el descuento."""

def calcular_descuento(total:float)->float:
    return total-(total*0.15)

nombre = input("Ingrese el nombre y apellido: ")
compra = float(input("Ingrese el valor total de la compra: "))

print(f'El cliente {nombre} \n Valor a pagar sin descuento:  {compra}$ \n Valor final a pagar: {calcular_descuento(compra)}$')