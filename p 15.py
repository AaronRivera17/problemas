#Escribe un programa que solicite al usuario los años de experiencia y determine la categoría del trabajador

añosexpe = float(input("Introduce los años de experiencia del trabajador: "))
if añosexpe < 2:
    categoria = "Junior"
elif añosexpe >= 2 and añosexpe <= 5:
    categoria = "Semi-Senior"
else:
    categoria = "Senior"
print(f"El trabajador tiene {añosexpe:} años de experiencia y pertenece a la categoría '{categoria:2}'.")