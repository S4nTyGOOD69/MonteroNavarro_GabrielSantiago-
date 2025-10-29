#ejercicio4

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))
num4 = int(input("Ingresa el cuarto numero: "))
num5 = int(input("Ingresa el quinto numero: "))

contador_mayor_10 = 0

if num1 > 10:
    contador_mayor_10 += 1 
if num2 > 10:
    contador_mayor_10 += 1 
if num3 > 10:
    contador_mayor_10 += 1 
if num4 > 10:
    contador_mayor_10 += 1 
if num5 > 10:
    contador_mayor_10 += 1     

print(f"De los 5 numeros ingresados, {contador_mayor_10}, son maypores que 10")
