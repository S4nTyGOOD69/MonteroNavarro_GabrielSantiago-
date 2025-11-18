#Funciones en python

#DEfinicion
def saludar():
    print("¡Holas, bienvenido a la clase de python!")

    #Llamada a la funcion
    saludar()
    saludar()
    saludar()

#Funcion con parametros
def saludar_persona(nombre, apellido, edad):
    print(f"¡Hola, {nombre}! Bienvenido a la clase de python.Tienes {edad} años.")

#Llamada con parametros
saludar_persona("Jorge", "Vasquez", 19)
saludar_persona("Ana", "Lopez", 22 )
saludar_persona()













#sistema de gestion de estiudiante 

#Funcion para moistrar las opciones del menu
def mostrar_menu():
    print("Sistema de gestion de estudiantes")
    print("1. Agregar estudiante")
    print("2. Mostrar lista completa de estudiantes")
    print("3. Buscar estudiante por nombre")
    print("4. Eliminar estudiante")
    print("5. salir")

#Funcion 
def agregar_estudiante(lista_estudiantes)
    nombre = input("Ingrese el nombre del estudiante:")    
    apellido = input("Ingrese el apellido del estudiante:")
    promedio = float(input("Ingrese el promedio del estudiante:"))
    
    lista_estudiantes.append({"nombre": nombre, "apellido": apellido, "promedio": promedio } )
    
    