# Haz un programa que pida una edad, y dependiendo del rango, muestre una categoría: - 
# - Menor de 13 años -> "Niño"  - 13 a 17 años -> "Adolescente" - 18 a 64 años -> "Adulto"  - 65 o más -> "Adulto mayor"
edadpersona = int(input("ingrese su edad: "))
if edadpersona < 13:
     print("niño")
elif 13 <= edadpersona <= 17:
     print("adolecente")
elif 18 <= edadpersona <= 64:
     print("adulto")
else:
     print("adulto mayor")

