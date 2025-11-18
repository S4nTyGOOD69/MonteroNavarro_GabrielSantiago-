#Ejercicio4

frase = input("Ingrese una frase: ")
vocales = "aeiouAEIOU"
contador_vocales = sum(1 for char in frase if char in vocales)
print(f"La frase contiene {contador_vocales} vocales.")
