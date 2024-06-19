#Escribe un programa que solicite al usuario dos números y determine cuál es mayor o si son iguales.
numero = float(input("Introduce un numero: "))
numero1 = float(input("Introduce el otro numero1: "))
if numero > numero1:
    print(f"El numero {numero} es mayor que el numero {numero1}.")
if numero1 < numero:
    print(f"El numero {numero1} es menor que el numero {numero}.")
else:
   print("Ambos numeros son iguales.")