#ejercicio2
numeros_pares = []
numeros_impares = []
while True:
    numero = int(input("Ingres un numero (0 para terminar): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero) 
        cantidad_impares = len(numeros_impares)
        cantidad_pares = len(numeros_pares)
        print(f"Cantidad de numeros pares: {cantidad_pares}" )
        print(f"Cantidad de numeros impares: {cantidad_impares}")
        numeros_pares.sort()
        numeros_impares.sort()
        print("Numeros pares en orden ")
        for num in numeros_pares:
            print(num)
            print("Numeros impares en orden ")
            for num in numeros_impares:
                print(num)


        
