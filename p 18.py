#Escribe un programa que solicite un número al usuario y determine si es divisible por 3,por 5, por ambos o por ninguno.

numero = float(input("Ingrese un número: "))


if numero % 3 == 0 and numero % 5 == 0:
    resultado = "El número es divisible por 3 y por 5."
elif numero % 3 == 0:
    resultado = "El número es divisible por 3."
elif numero % 5 == 0:
    resultado = "El número es divisible por 5."
else:
    resultado = "El número no es divisible ni por 3 ni por 5."


print(")
