#Escribe un programa que solicite al usuario su salario bruto y calcule el salario netodespués de aplicar un impuesto del 20% si el salario bruto es mayor a $2000.

salarioB = float(input("Introduce tu salario bruto: "))
if salarioB > 2000:
    impuesto = salarioB * 0.20
    salarioN = salario - impuesto
else:
    salarioN = salarioB
print(f"Tu salario neto es {salarioN:}")
