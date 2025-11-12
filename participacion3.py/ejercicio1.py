#Pide nombres hasta que el usuario escriba la palabra "Fin". Al final muestra cuantos nombres ingresó, y cuál es el primero y el último.
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



