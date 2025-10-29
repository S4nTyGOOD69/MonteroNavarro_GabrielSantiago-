#Ejercicio3: Haz un programa en python que pida un numero entero y muestre cuantos numero pares 
# hay desde 1 hasta ese numero (incluyendo si es par)

conteo_pares = 0
#solicitar al usuario que ingrese un numero entero
numero = int(input("Ingrese un numero entero: "))

for i in range(1, numero + 1):
    if i %2 == 0: 
        conteo_pares += 1
        print(1)

print(f"hay {conteo_pares} numeros pares desde 1 hasta {numero}.")
         
print("----------------------------------------------------") 

        #ejercicio4: Haz un programa en python que pida un numero y 
        # calcule el factorial de ese numero utilizando in ciclo for.
numero = int(input("Ingrese un numero para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es {factorial}.")

print("---------------------------------------------------------------------------")

#ejercicio1: Haz un programa que pida al usuario ingresar una contraseña 
# correcta hasta que ingrese la correcta, y que tenga 5 inentos 
contraseña_correcta = "Credinalga"
intentos = 0
max_intentos = 5
contraseña = input("Ingrese la contraseña: ")

while (intentos < max_intentos) and (contraseña != contraseña_correcta):
    print("Cotraseña incorrecta. Intenta de nuevo.")
    intentos +=1 
    contraseña = input("Ingrese la contraseña: ")

if intentos ==max_intentos:
    print("Has excedido el numero maximo de intentos. Acceso denegado.")
else:
    print(f"Contraseña correcta. Acceso concedido. Intentos realizados {intentos}.") 
           
print("-------------------------------------------------------------------------")

#ejercicio2: Haz un programa que pida al usuario ungresar numero positivos y 
# que se detenga hasta que ingrese un numero negativo 

numero = float(input("Ingrese un numero positivo(o un numero negativo para salir): "))

while numero >= 0:
    numero = float(input("Ingrese un numero positivo (o un numero negativo para salir): "))

print("Numero negativo ingresado. Programa terminado.")

print("------------------------------------------------------------")

#Ejercicio 3: haz un programa que sume todos los numeros que ingrese el usuario hasta qie 
# ingrese un 0
suma = 0 
numero = float(input("Ingrese un numero para sumar (o 0 para salir): "))

while numero != 0:
    suma += numero
    numero = float(input("Ingrese un numero para sumar (o 0 para salir): "))

print(f"La suma total de los numeros ingresados es: {suma}.")
