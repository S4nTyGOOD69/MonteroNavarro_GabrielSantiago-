#Haz un programa que pida 5 nombres y luego pregunte uno; si está en la lista, muestra “Encontrado”.
nombres = []
for _ in range(5):
    nombre = input("Introduce un nombre: ")
    nombres.append(nombre)
nombre_buscar = input("Introduce un nombre para buscar: ")
if nombre_buscar in nombres:
    print("Encontrado")
else:
    print("No encontrado")

    