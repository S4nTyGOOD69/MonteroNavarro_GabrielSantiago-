#ejercio6

nombres = []
calificaciones = [] 
for _ in range(5):
    nombre = input("Ingrese el nombre del estudiante: ")
    calificacion = float(input("Ingrese la calificación del estudiante (0-10): "))
    nombres.append(nombre)
    calificaciones.append(calificacion)
promedio = sum(calificaciones) / len(calificaciones)
calificacion_mayor = max(calificaciones)
calificacion_menor = min(calificaciones)
indice_mejor_alumno = calificaciones.index(calificacion_mayor)  
mejor_alumno = nombres[indice_mejor_alumno]
print(f"Promedio general: {promedio:.2f}")
print(f"Calificación mayor: {calificacion_mayor}")
print(f"Calificación menor: {calificacion_menor}")
print(f"Mejor alumno: {mejor_alumno}")      
