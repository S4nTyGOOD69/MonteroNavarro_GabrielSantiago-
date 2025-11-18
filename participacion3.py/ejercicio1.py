#Ejercicio1

nombres = []
while True:
    nombre = input("Ingrese un nombre (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    nombres.append(nombre)
    if len(nombres) == 1:
        primer = nombre
        ultimo =nombre
    else:
        ultimo =nombre
        cantidad = len(nombres)
        print(f"Cantidad de nombres ingresados: {cantidad}")

print(f"El primer nombre ingresado es : {primer}.")
print(f"El ultimo nombre ingresado es: {ultimo}.")


