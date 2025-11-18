#Ejercio5

numero = int(input("Ingrese un número: "))
lista = []
for _ in range(numero):
    elemento = input("Ingrese un elemento: ")
    if elemento not in lista:
        lista.append(elemento)
print("Lista sin duplicados:", lista)       
