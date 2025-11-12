# union |
# .union()

set_countries = {"Argentina", "Brasil", "Chile"}
set_more_countries = {"Colombia", "Perú", "Argentina"}

# Unión de conjuntos utilizando el metodo union()
# set_countries.union(set_more_countries)
set_union = set_countries | set_more_countries
print(f"Unión de conjuntos: {set_union}")

set_countries.update(set_more_countries)
print(f"Conjunto de conjuntos: {set_countries}")

# Intersección de conjuntos utilizando el metodo intersection() o &

set_countries3 = {"Argentina", "Brasil", "Chile", "Colombia"}
set_more_countries3 = {"Colombia", "Perú", "Argentina"}
set_intersection = set_countries3 & set_more_countries3
print(f"Intersección de conjuntos: {set_intersection}")

# Diferencia de conjuntos utilizando el metodo difference() o -
set_countries4 = {"Argentina", "Brasil", "Chile", "Colombia"}
set_more_countries4 = {"Colombia", "Perú", "Argentina"}
set_difference = set_countries4 - set_more_countries4
set_difference2 = set_more_countries4.difference(set_countries4)
print(f"Diferencia de conjuntos: {set_difference}")
print(f"Diferencia de conjuntos: {set_difference2}")

## Diferencia simétrica utilizando el metodo symmetric_difference() o ^
# Devuelve los elementos que están en uno u otro conjunto, pero no en ambos

set_countries5 = {"Argentina", "Brasil", "Chile", "Colombia"}
set_more_countries5 = {"Colombia", "Perú", "Argentina"}
set_symmetric_difference = set_countries5 ^ set_more_countries5
set_symmetric_difference2 = set_countries5.symmetric_difference(set_more_countries5)

print(f"Diferencia simétrica de conjuntos: {set_symmetric_difference}")
