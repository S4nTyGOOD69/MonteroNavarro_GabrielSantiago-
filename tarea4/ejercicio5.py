#Pide al usuario una lista de palabras (separadas por comas, por ejemplo Hola, Mario, Python, Programación). Elimina los elementos repetidos y los que sean menores a 3 letras. Muestra la nueva lista e imprímela en pantalla. 
#ejercicio5
entrada = input("Introduce una lista de palabras separadas por comas: ")
palabras = [palabra.strip() for palabra in entrada.split(",")]
palabras_filtradas = list({palabra for palabra in palabras if len(palabra) >= 3})
print(palabras_filtradas)
