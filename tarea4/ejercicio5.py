#ejercicio5

entrada = input("Introduce una lista de palabras separadas por comas: ")
palabras = [palabra.strip() for palabra in entrada.split(",")]
palabras_filtradas = list({palabra for palabra in palabras if len(palabra) >= 3})
print(palabras_filtradas)
