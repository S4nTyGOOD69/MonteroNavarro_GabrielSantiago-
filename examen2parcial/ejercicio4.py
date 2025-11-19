#Haz un programa que pida una palabra y cuenta cuantas vocales tiene la palabra ingresada 
palabra = input("Introduce una palabra: ")
vocales = "aeiouAEIOU" 
contador_vocales = 0 
for letra in palabra: 
    if letra in vocales:
        contador_vocales += 1
print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")

