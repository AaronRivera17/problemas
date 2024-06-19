#Escribe un programa que solicite un nombre al usuario y determine si el nombre es corto (menos de 5 letras), mediano (5-8 letras) o largo (más de 8 letras).
nombre = float(input("Introduce un nombre: ")

longitud_no = len(nombre)


if longitud_no < 5:
    categoria = "corto"
elif longitud_no >= 5 and longitud_no <= 8:
    categoria = "mediano"
else:
    categoria = "largo"


print(f"El nombre {nombre} tiene {longitud_no} letras y es de longitud {categoria}.")

