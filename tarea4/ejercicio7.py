#ejercicio7

respuestas = {}
while True:
    nombre = input("Introduce el nombre de la persona (o 'Fin' para terminar): ")
    if nombre == "Fin":
        break
    respuesta = input("Introduce la respuesta ('Si' o 'No'): ")
    respuestas[nombre] = respuesta

contador_si = sum(1 for r in respuestas.values() if r.lower() == "si")
contador_no = sum(1 for r in respuestas.values() if r.lower() == "no")

print(f"Personas que respondieron 'Si': {contador_si}")
print(f"Personas que respondieron 'No': {contador_no}")



