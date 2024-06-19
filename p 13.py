#Escribe un programa que solicite un año al usuario y determine si es el primer año de un siglo (por ejemplo, 1900, 2000, 2100).

año =float(input("Introduce el año: "))
if año % 100 == 0:
    print(f"{año} es el primer año de un siglo")
else:
    print(f"{año} no es el primer año de un siglo")