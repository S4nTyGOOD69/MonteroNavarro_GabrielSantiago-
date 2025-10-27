# Haz un programa que pida dos numeros y muestre si el primero es mayor, menor o igual al segundo 
# ( utiliza solo operadores de comparacion y logicos)

num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))

resultado1 = (num1 > num2)
resultado = (num1 <= num2) 

print(f'¿se cumple la proposicion si es mayor el primer numero? {resultado1} ')
print(f'¿se cumple la proposicion menor o igual al segundo ? {resultado} ')

