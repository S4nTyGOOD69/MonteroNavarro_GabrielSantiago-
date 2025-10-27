#Sintaxis condicionales 

numero = float(input("ingrese un numero:"))

if numero > 0:
    print("Bloque if ejecutado.")
    print("El numero es positivo.")
elif numero < 0: 
    print("Bloque elif ejecutado.")
    print("El numero es negativo.")
else:
    print("Bloque else ejecutado.")  
    print("el numero es cero.") 

print("---------------------------------------")

#if 
#ejercio2: programa que pida dos numero y muestre cual es mayor o si son iguales 

num1 = float(input("Ingrese el primer numero:"))
num2 = float(input("ingrese el segundo numero:"))

if num1 > num2:
    print ("El primer numero es mayor.")
elif num1 < num2: #num2 > num1
    print("El segundo numero es mayor.")
else:
    print("Ambos numeros son iguales.")

print("------------------------------------------------")        


#ejercicio3:Haz un programa que pida una calificacion del 0 al 10 y 
# muestre si esta aprobado o reprobado. Toma en cuenta una calificacion mayor o igual a 6 como aprobatoria 

nombreAlumno = input("Ingrese el nombre completo:")
calificacion = float(input("Ingrese la calificacion del alumno (0 - 10): "))

if calificacion >= 6:
    print(f"El alumno {nombreAlumno} esta aprobado. ")
else:
    print(f"El alumno {nombreAlumno} esta reprobado. ")

print("-----------------------------------------") 

#ejercicio4: Haz un programa que pida la edad de una persona y muestre si puede votar (mayor o igual a 18 años) o no

nombre = input("Ingrese el nombre de la persona:")
edadPersona = int(input("Ingrese su edad: ") )
