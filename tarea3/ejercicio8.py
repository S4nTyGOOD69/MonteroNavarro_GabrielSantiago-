num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2: 
    num1, num2 = num2, num1 

print("Los numeros multiplos de 7 entre", num1, "y", num2, "son los siguentes: ")

for i in range(num1, num2 +1):
    if i % 7 == 0:
         print(i)   