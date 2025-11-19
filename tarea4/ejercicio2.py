#ejercicio2

frase = input("Introduce una frase: ")
palabras = frase.split()
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print(contador_palabras)
