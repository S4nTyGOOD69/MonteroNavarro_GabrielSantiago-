#ejercicio1
numeros_pares = 0
numeros_impares = 0

numero = int(input("Ingrese el un numero entero: "))

for i in range(1, numero + 1):
    if i %2 == 0: 
        numeros_pares += 1
    else:
        numeros_impares +=1
    print(i)
print(f"hay {numeros_pares} numeros pares, {numeros_impares} numeros impares desde 1 hasta {numero}.")


  

