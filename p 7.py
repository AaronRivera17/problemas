#Calcular el precio con descuento de un producto

prd= float(input("Ingrese el precio del producto "))

if prd >= 100:
    descuento= prd * 0.10 
    des_total= prd - descuento
    print(f"El descuento toal del prodcuto es de: {des_total} ")
    
