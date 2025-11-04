#Pide una cantidad de productos y su precio uno por uno, luego muestra el total con IVA del 16%.

cantidad_productos = int(input("Ingrese la cantidad de productos: "))
total_sin_iva = 0.0                                                                                             
for i in range(cantidad_productos):
    precio = float(input("Ingrese el precio del producto {}: ".format(i + 1)))
    total_sin_iva += precio
iva = total_sin_iva * 0.16
total_con_iva = total_sin_iva + iva
print("El total con IVA es:", total_con_iva)

