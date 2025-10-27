# ejercico 1

calificacion1 = float(input("Ingresa la primera calificacion: "))
calificacion2 = float(input("Ingresa la segunda calificacion: "))
calificacion3 = float(input("Ingresa la tercera calificacion: "))

promedio = (calificacion1+calificacion2+calificacion3)/3 

print("El promedio de las notas es: ", round(promedio,1))

print ("----------------------------------------------------------------")

#ejercicio2
import math

print("ingrese el radio del circulo: ")
radio = float(input())
area = math.pi *(radio * radio)
print("El area del circulo es",round(area,2) )

print ("----------------------------------------------------------------")
#Ejercicio 3
 
radio = float(input("Ingresa el radio de tu circunferencia: "))

perimetro = ((radio * 2) * 3.1416)

print(f"El perimetro de tu circunferencia es: {perimetro}")

print ("----------------------------------------------------------------")
#Ejercicio 4 

minutos = int(input("Ingresa los minutos: "))

horas = (minutos / 60)

print(f"Las horas totales son: {horas}")

print ("----------------------------------------------------------------")
#ejercicio 5
precio = float(input("Ingresa el precio: "))

iva = (precio * .16)
precioiva = (precio + iva)

print(f"El precio con iva es: {precioiva}")

print ("----------------------------------------------------------------")
#Ejercicio 6

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

resultado = num1 < num2 < num3

print(f"¿Se cumple la expresión A < B < C? {resultado}")

print ("----------------------------------------------------------------")
#Ejercicio 7

num = float(input("Ingresa un numero: "))

numero = num>=10 and num<=20
print(f"¿El numero esta entre 10 y 20? {numero}")

print ("----------------------------------------------------------------")
#Ejercicio 8

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

resultado = num1 == num2 == num3

print(f"¿Los tres numeros son iguales? {resultado}")

print ("----------------------------------------------------------------")
#Ejercicio 

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

resultado = num1 == num2 == num3

print(f"¿Los tres numeros son iguales? {resultado}")

print ("----------------------------------------------------------------")
#Ejercicio 10

radio = float(input("Ingresa el radio de tu cilindro: "))
altura = float(input("Ingresa la altura de tu cilindro: "))

radiocuadrado = math.pow (radio, 2)
areabase = (radiocuadrado * 3.1416)
volumen = (areabase * altura)

print(f"El volumen del cilindro es: {volumen}")

print ("----------------------------------------------------------------")