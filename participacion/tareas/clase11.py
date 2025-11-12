#ejercicio 3: Pide 6 nombres y muestra la lista numerada (1. Nombre1, 2. Nombre2, etc.)

lista_nombres = []
for i in range(6):
    nombre = input("Introduce un nombre: ")
    lista_nombres.append(nombre)

lista_nombres.sort()

for i, nombre in enumerate(lista_nombres, start=1):
    print(f"{i}. {nombre}")

#Ejercicio4: Pide 8 numeros, elimina las repeticiones y 
# muestra la lista sin duplicados ordenados de menor a mayor.

lista_numeros = []

for i in range(8):
    numero = int(input("Introduce un numero: "))
    lista_numeros.append(numero)

lista_numeros_ordenada = list(set(lista_numeros))
lista_numeros_ordenada.sort()
print(lista_numeros_ordenada)

#ejercicio5: Pide 10 calificaciones entre 0 y 10. si alguna es menor que 6, añade 
# al conteo de reprobados. Al final, muestra cuantos aprobaron y cuantos reprobaron.

lista_aprobados = []
lista_reprobados = []

for i in range(10):
    calificacion = float(input("Introduce una calificacion entre 0 y 10: "))
    while(calificacion < 0 or calificacion > 10):
        calificacion = float(input("Calificacion invalida. Introduce una calificacion entre 0 y 10:"))
    if calificacion < 6:
        lista_reprobados.append(calificacion)
    else: 
        lista_aprobados.append(calificacion)

print(f"Cantidad de aprobados: {len(lista_aprobados)}")
print(f"Cantidad de reprobados: {len(lista_reprobados)}") 

#Diccionario

diccionario = {
    "nombre": "Mario",
    "apellido": "Segovia",
    "edad":29,
    "liceciatura": "Ingeniero en sistemas comaputacionales",
    "isEmpleado": True
}  

print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
print(diccionario["isEmpleado"])
diccionario.pop("edad")
print(diccionario)
print(len(diccionario))

diccionario["edad"] = 29
print(diccionario)

#Recorda un diccionario
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")


#ejercicio1: Crea  un diccionario vacio. Pide nombres y cakificaciones de 5 alumnos y 
# guardalos en ek diccionario. Luego muestra su promedio.
diccionario_alumnos = {}
for i in range(5):
    nombre = input("Introduce el nombre del alumno: ")
    clificacion = float(input(f"Introduce la calificacion de {nombre}: "))
    while(calificacion < 0 or calificacion > 10):
        calificacion = float(input(f"C alificacion invalida. INtroduce la calificacion de {nombre} entre 0 y 10: "))
        diccionario_alumnos[nombre] = calificacion

print(diccionario_alumnos)

for clave, valor in diccionario_alumnos.items():
    print(f"La calificacion de {clave} es: {valor}") 

suma_calificaciones = sum(diccionario_alumnos.values()) 
promedio = suma_calificaciones / len(diccionario_alumnos)
print(f"El promedio de las calificaciones es : {promedio}" )  

#Eejercicio 2: Crea un diccionario con 5 productos y precios, pide un producto y muestra su precio.
diccionario_productos ={
"Cloro": 20,
"detergente": 35,
"jabon": 15,
"papel sanitario": 40,
"limpiador": 60
}
producto_buscado = input("Introduce el nombre del producto: ")
if producto_buscado in diccionario_productos:
    print(f"El precio de {producto_buscado} es ${diccionario_productos[producto_buscado]}.")
else:
    print("El producto no se encuentra en el inventario.")  

#Ejercicio 3: Crea un diccionario con 5 paises y sus capitales. Pide un pais y muestra su capital.

diccionario_paises = {
    "Mexico": "ciudad de Mexico",
    "Beasil": "Brasilia", 
    "Uruguay": "Montevideo",
    "Argentina": "Buenos Aires",
    "Estados Unidos": "Washinton D.C."
    }       
while pais_buscado != "salir":
    if pais_buscado in diccionario_paises:
        printI(f"La capital de {pais_buscado} es: {diccionario_paises[pais_buscado]}.")
        else
