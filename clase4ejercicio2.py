#Haz un programa que pida tres numeros enteros y muestre si se cumple la expresion: 
#El primer numero es mayor que el segundo y el segundo es menor que el tercero.

num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))
num3 = int(input("ingrese el tercer numero entero: "))

resultado = (num1 > num2) and( num2 < num3)

print(f'¿se cumple la proposicion? {resultado} ')
