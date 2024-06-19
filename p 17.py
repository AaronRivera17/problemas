#Escribe un programa que solicite la edad del usuario y determine el tipo de licencia de conducir que puede obtener
edad = float(input("Introduce tu edad: "))

if edad >= 16 and edad <= 17:
    tipo_licencia = "Licencia de menor"
elif edad >= 18 and edad <= 65:
    tipo_licencia = "Licencia de adulto"
elif edad > 65:
    tipo_licencia = "Licencia de adulto mayor"
else:
    tipo_licencia = "No eres elegible para tener una licencia de conducir"

print(f"A los {edad} años, fuiste seleccionado para tener '{tipo_licencia}'.")
