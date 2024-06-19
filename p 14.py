#Escribe un programa que solicite las longitudes de los tres lados de un triángulo y determine si es un triángulo válido (la suma de las longitudes de dos lados debe ser
#mayor que la longitud del tercer lado).

lado1 = float(input("Introduce la longitud del primer lado: "))
lado2 = float(input("Introduce la longitud del segundo lado: "))
lado3 = float(input("Introduce la longitud del tercer lado: "))
if ((lado1 + lado2) > lado3) or ((lado1 + lado3) > lado2) or ((lado2 + lado3) > lado1):
    print("Los lados ingresados forman un triángulo válido.")
else:
    print("Los lados ingresados no forman un triángulo válido.")