"""
CONTEXTO:
Eres el encargado de una cadena de tiendas de computadoras con 3 sucursales. Cada sucursal tiene diferentes productos en stock.

TAREAS PARA REALIZAR:

1. Crea tres conjuntos con los inventarios de cada sucursal:

sucursal_norte = {'Laptops Gaming', 'Monitores 4K', 'Teclados Mecánicos',
'Mouse Inalámbrico', 'Memorias RAM', 'Tarjetas Gráficas'}

sucursal_sur = {'Laptops Gaming', 'Discos SSD', 'Teclados Mecánicos',
'Procesadores Intel', 'Memorias RAM', 'Gabinetes RGB'}

sucursal_centro = {'Monitores 4K', 'Mouse Inalámbrico', 'Discos SSD',
'Procesadores AMD', 'Tarjetas Gráficas', 'Audífonos Gamer'}


2. Encuentra los productos que están disponibles en TODAS las sucursales.

3. Encuentra los productos que están en la sucursal Norte o Sur, pero NO en ambas.

4. Encuentra los productos que están SOLO en la sucursal Norte (no están en Sur ni en Centro)

5. La sucursal Norte recibe inventario nuevo de:
'Fuentes de Poder' y 'Procesadores AMD'
Actualiza el conjunto

6. En la sucursal Sur se agotaron: 'Laptops Gaming', 'Gabinetes RGB', 'Webcams HD'
Elimínalos del conjunto sin generar error (nota: 'Webcams HD' no existe)

7. Encuentra qué productos están en exactamente 2 sucursales.
"""

#Se importa os para crear una funcion y limpiar la consola
import os

#Se define la funcion para limpiar la consola
def limpiar_consola():
    #Comando para limpiar la consola en Windows
    os.system('cls')

#Se definen los inventarios iniciales de cada sucursal usando sets
#Sucursal norte
sucursal_norte = {'Laptops Gaming', 'Monitores 4K', 'Teclados Mecánicos',
'Mouse Inalámbrico', 'Memorias RAM', 'Tarjetas Gráficas'}

#Sucursal sur
sucursal_sur = {'Laptops Gaming', 'Discos SSD', 'Teclados Mecánicos',
'Procesadores Intel', 'Memorias RAM', 'Gabinetes RGB'}

#Sucursal centro
sucursal_centro = {'Monitores 4K', 'Mouse Inalámbrico', 'Discos SSD',
'Procesadores AMD', 'Tarjetas Gráficas', 'Audífonos Gamer'}

#Se definen los sets para actualizaciones futuras
#Con este set, se agregaran productos a la sucursal norte
update_sucursal_norte = {'Fuentes de Poder', 'Procesadores AMD'}
#Con este set, se eliminaran productos de la sucursal sur
discard_sucursal_sur = {'Laptops Gaming', 'Gabinetes RGB', 'Webcams HD'}

#Se define la funcion que obtiene todos los productos de todas las sucursales, recibe 3 sets como parametro y retorna un set
def productos_en_todas_sucursales(sucursal_norte:set, sucursal_sur:set, sucursal_centro:set)-> set:
    #Se usa union() para combinar todos los productos unicos de las tres sucursales
    procutos_todas_sucursales = sucursal_norte.union(sucursal_centro).union(sucursal_sur)
    #Retorna el conjunto con todos los productos
    return procutos_todas_sucursales

## Este no estaba incluido en el taller pero lo agregue para practicar con intersection() ya que no se aplicaba en ningun otro punto del taller

#Se define la funcion que busca productos disponibles en las TRES sucursales simultaneamente, recibe 3 sets como parametro
def productos_coinciden_sucursales(sucursal_norte:set, sucursal_sur:set, sucursal_centro:set):
    #Se usa intersection() para encontrar productos comunes en las tres sucursales
    productos_coinciden = sucursal_norte.intersection(sucursal_sur).intersection(sucursal_centro)
    #Valida si no hay productos que coincidan
    if not productos_coinciden:
        #Retorna un mensaje si no existe ninguna coincidencia
        return "No hay productos que coincidan en todas las sucursales"
    #Retorna el conjunto de productos coincidentes
    return productos_coinciden

#Se define la funcion que muestra productos en Norte O Sur, pero NO en ambas, recibe 2 sets como parametro y retorna un set
def productos_norte_o_sur(sucursal_norte:set, sucursal_sur:set)-> set:
    #Se usa symmetric_difference() para encontrar productos exclusivos de cada sucursal
    productos_norte_sur = sucursal_norte.symmetric_difference(sucursal_sur)
    #Retorna el conjunto con las diferencias exclusivas
    return productos_norte_sur

#Se define la funcion que identifica productos EXCLUSIVOS de la sucursal Norte, recibe 3 sets como parametro y retorna un set
def productos_solo_norte(sucursal_norte:set,sucursal_sur:set,sucursal_centro:set):
    #Se usa difference() dos veces para eliminar productos que estan en Sur o Centro
    productos_solo_norte = sucursal_norte.difference(sucursal_sur).difference(sucursal_centro)
    #Valida si no hay productos exclusivos
    if not productos_solo_norte:
        #Retorna un mensaje si no existen productos exclusivos
        return "No hay productos exclusivos en la sucursal Norte"
    #Retorna el conjunto de productos exclusivos
    return productos_solo_norte

#Se define la funcion para agregar nuevos productos al inventario Norte, recibe 2 sets como parametro y retorna un set
def actualizar_inventario_norte(sucursal_norte:set,objetos:set)->set:
    #Se usa update() para agregar los nuevos productos al set original
    sucursal_norte.update(objetos)
    #Imprime mensaje de confirmacion con los productos agregados
    print(f'Sucursal Norte actualizada con los siguientes productos:\n {objetos}')
    #Retorna el conjunto actualizado
    return sucursal_norte

#Se define la funcion para eliminar productos agotados del inventario Sur, recibe 2 sets como parametro y retorna un set
def eliminar_productos_agotados_sur(sucursal_sur: set, objetos: set) -> set:
    #Se crea un ciclo para iterar sobre cada producto a eliminar
    for producto in objetos:
        """Valida si el producto existe en el inventario y aunque se puede usar directamente discard() para elementos que
        no existan lo hago asi para imprimir mensajes y mostrar informacion al usuario que esta intentando eliminar algo que no esta
        """
        if producto in sucursal_sur:
            #Se usa discard() para eliminar sin generar error si no existe
            sucursal_sur.discard(producto)
            #Imprime mensaje de confirmacion
            print(f'Se ha eliminado: {producto}')
        #Si el producto no existe
        else:
            #Imprime mensaje informativo
            print(f'No se encontró el producto: {producto}')
    #Retorna el conjunto actualizado
    return sucursal_sur

#Se define la funcion que encuentra productos en EXACTAMENTE 2 sucursales, recibe 3 sets como parametro y retorna un set
def productos_en_dos_sucursales(sucursal_norte:set, sucursal_sur:set, sucursal_centro:set)-> set:
    #Se calcula la union de tres operaciones:
    #1. (Norte | Sur) - Centro: productos en Norte y Sur, pero no en Centro
    #2. (Norte | Centro) - Sur: productos en Norte y Centro, pero no en Sur
    #3. (Sur | Centro) - Norte: productos en Sur y Centro, pero no en Norte
    productos_dos_sucursales = (
        (sucursal_norte.intersection(sucursal_sur)).difference(sucursal_centro).union((sucursal_norte.intersection(sucursal_centro)).difference(sucursal_sur)).union(
        (sucursal_sur.intersection(sucursal_centro)).difference(sucursal_norte)
        )
    )
    #Retorna el conjunto de productos en exactamente 2 sucursales
    return productos_dos_sucursales

#Se crea un bucle infinito para el menu principal
while True:
    #Se usa try para manejar posibles excepciones
    try:
        #Se solicita al usuario que seleccione una opcion del menu
        opcion = int(input(
            "\nSeleccione una opción:\n"
            "1. Productos en todas las sucursales\n"
            "2. Productos que coinciden en todas las sucursales\n"
            "3. Productos en Norte o Sur, pero no en ambas\n"
            "4. Productos solo en Norte\n"
            "5. Actualizar inventario Norte\n"
            "6. Eliminar productos agotados en Sur\n"
            "7. Productos en exactamente 2 sucursales\n"
            "8. Salir\n"
            "Opción: "
        ))
        # Se limpia la consola para mejor legibilidad
        limpiar_consola()

        # Si la opcion esta fuera del rango permitido (1 a 8) se lanza un ValueError
        if opcion < 1 or opcion > 8:
            raise ValueError

        #Valida si la opcion es 1
        if opcion == 1:
            #Imprime el resultado de la funcion productos_en_todas_sucursales
            print(f'PRODUCTOS DE TODAS LAS SURCURSALES:\n{productos_en_todas_sucursales(sucursal_norte, sucursal_sur, sucursal_centro)}')
        #Valida si la opcion es 2
        elif opcion == 2:
            #Imprime el resultado de la funcion productos_coinciden_sucursales
            print(f'PRODUCTOS QUE COINCIDEN EN TODAS LAS SUCURSALES:\n{productos_coinciden_sucursales(sucursal_norte, sucursal_sur, sucursal_centro)}')
        #Valida si la opcion es 3
        elif opcion == 3:
            #Imprime el resultado de la funcion productos_norte_o_sur
            print(f'PRODUCTOS EN NORTE O SUR (pero no ambas):\n{productos_norte_o_sur(sucursal_norte,sucursal_sur)}')
        #Valida si la opcion es 4
        elif opcion == 4:
            #Imprime el resultado de la funcion productos_solo_norte
            print(f'PRODUCTOS SOLO EN NORTE:\n{productos_solo_norte(sucursal_norte,sucursal_sur,sucursal_centro)}')
        #Valida si la opcion es 5
        elif opcion == 5:
            #Imprime el resultado de la funcion actualizar_inventario_norte
            print(f'ACTUALIZAR INVENTARIO EN NORTE:\n{actualizar_inventario_norte(sucursal_norte,update_sucursal_norte)}')
        #Valida si la opcion es 6
        elif opcion == 6:
            #Imprime el resultado de la funcion eliminar_productos_agotados_sur
            print(f'ELIMINAR PRODUCTOS AGOTADOS EN SUR:\n{eliminar_productos_agotados_sur(sucursal_sur,discard_sucursal_sur)}')
        #Valida si la opcion es 7
        elif opcion == 7:
            #Imprime el resultado de la funcion productos_en_dos_sucursales
            print(f'PRODUCTOS EXACTAMENTE EN 2 SUCURSALES:\n{productos_en_dos_sucursales(sucursal_norte,sucursal_sur,sucursal_centro)}')
        #Valida si la opcion es 8
        elif opcion == 8:
            #Imprime mensaje para salir del programa
            print("Saliendo del programa...")
            #Rompe el ciclo while
            break
    #Captura excepciones de tipo ValueError
    except ValueError:
        #Imprime mensaje de error
        print("Opción inválida. Por favor, intente de nuevo.")