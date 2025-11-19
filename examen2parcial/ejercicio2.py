#Pide una palabra y reemplaza todas las vocales por el simbolo *
palabra = input("Introduce una palabra:")
palabra_modificada = palabra.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*").replace("A","*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*") 
print(f"La palabra modificada es: {palabra_modificada}")

