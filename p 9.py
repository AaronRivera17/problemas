#Escribe un programa que solicite un carácter al usuario y determine si es una letra (a-z, A-Z) o un dígito (0-9).
X = input("Escribe un caracter: ")

if X.isdigit():
    print("Es un dígito")

if X.isalpha():
    print("Es una letra")