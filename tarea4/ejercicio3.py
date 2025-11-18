#Haz un programa que pida al usuario una contraseña. Verifica que: La contraseña tenga al menos 8 caracteres, y que contenga al menos una mayúscula y un número.
frase = input("Introduce una frase: ")
palabras = frase.split()
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
print(contador_palabras)