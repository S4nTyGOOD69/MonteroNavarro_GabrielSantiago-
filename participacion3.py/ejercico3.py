#Ejercicio3

nombre = input("Ingrese el nombre del estudiante: ")
calificacion = float(input("Ingrese la calificación del estudiante (0-10): "))      
datos_estudiantes = {}
datos_estudiantes[nombre] = calificacion    
promedio = sum(datos_estudiantes.values()) / len(datos_estudiantes)
aprobados = sum(1 for cal in datos_estudiantes.values() if cal >= 6)
reprobados = sum(1 for cal in datos_estudiantes.values() if cal < 6)
print(f"Promedio general: {promedio:.2f}")
print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de reprobados: {reprobados}")
