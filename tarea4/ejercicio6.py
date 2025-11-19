#ejercicio6

productos_precios = []
num_productos = int(input("¿Cuántos productos quieres agregar al diccionario? "))
for _ in range(num_productos):
    producto = input("Introduce el nombre del producto: ")
    precio = float(input(f"Introduce el precio de {producto}: "))
    productos_precios.append((producto, precio))
diccionario_productos = dict(productos_precios)
productos_comprados = input("Introduce una lista de productos comprados separados por comas: ").split(",")
total_compra = 0.0
for producto in productos_comprados:
    producto = producto.strip()
    if producto in diccionario_productos:
        total_compra += diccionario_productos[producto]
    else:
        print(f"Advertencia: El producto '{producto}' no existe en el diccionario.")
print(f"Total de la compra: {total_compra}")

