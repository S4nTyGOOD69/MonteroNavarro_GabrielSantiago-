#ejercicio1

frase = input("Introduce una frase: ")
palabras = frase.split()
palabras_mas_de_cinco = [palabra for palabra in palabras if len(palabra) > 5]
print(palabras_mas_de_cinco)
