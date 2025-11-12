set_countries = {"Uruguay", "Paraguay", "Bolivia", "Ecuador"}
set_countries.remove("Paraguay")  # Remover un solo elemento

print(set_countries)

set_countries.discard("Chile")  # Remover un elemento que no existe (no genera error)
print(set_countries)

removed_country = set_countries.pop()  # Remover y obtener un elemento arbitrario
print(f"País removido: {removed_country}")
print(set_countries)

set_countries.clear()
print(set_countries)    