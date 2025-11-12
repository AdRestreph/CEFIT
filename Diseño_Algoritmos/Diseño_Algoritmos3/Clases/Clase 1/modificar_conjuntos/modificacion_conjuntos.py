set_countries = {"Argentina", "Brasil", "Chile", "Colombia"}

set_countries.add("Perú")  # Agregar un solo elemento

set_countries.update(["Uruguay", "Paraguay"])  # Agregar múltiples elementos

size = len(set_countries)  # Obtener el tamaño del conjunto

print(f"Conjunto de países: {set_countries}")
print(f"Tamaño del conjunto: {size}")

lista_countries1 = ["Colombia", "Venezuela", "Ecuador"]
list_countries2 = []
for i in lista_countries1:
    list_countries2.append(i.lower())
print(list_countries2)
print(type(list_countries2))
set_countries_lower = set(list_countries2)
print(type(set_countries_lower))
print(set_countries_lower)

