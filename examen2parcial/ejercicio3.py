#Haz un  programa que pida un numero entero N, y calcula la suma de todos los numeros del 1 al N
numero = int(input("Introduce un numero entero N: "))
summa = 0
for i in range(1, numero + 1):
    summa += i
    print(f"La suma de los numeros del 1 al {numero} es: {summa}")
    