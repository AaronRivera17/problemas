#Escribe un programa que solicite la distancia recorrida en kilómetros y calcule la tarifa del taxi.
distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))

if distancia <= 10:
    tarifa = distancia * 2.50
else:
    tarifa = (10 * 2.50) + ((distancia - 10) * 2.00)

print(f"La tarifa del taxi es: ${tarifa:}")
