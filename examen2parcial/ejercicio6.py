#pide al usuario ingresar 10 productos y almacenalos en una lista. luego muestra la lista ordenada alfabeticamente
#Ejercicio6
productos = []
for i in range(10):
    producto = input(f"Introduce el nombre del producto {i+1}: ")
    productos.append(producto)
    productos_ordenados = sorted(productos)
    print("Lista de productos ordenados alfabeticamente: ")
    for prod in productos_ordenados:
        print(prod)

