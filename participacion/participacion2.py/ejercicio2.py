#ejercicio2

nombre = input("Ingrese nombre completo: ")
edadPersona = int(input("Ingresa su edad: "))

añosfaltantes = 18-(edadPersona)

if edadPersona >= 18: 
    print(f"{nombre} tiene {edadPersona} años y puede votar.")
else:
    print(f"{nombre} tiene {edadPersona} y no puede votar")
    print(f"Te faltan {añosfaltantes} años para poder votar")