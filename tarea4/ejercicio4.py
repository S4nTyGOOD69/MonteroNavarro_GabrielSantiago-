#ejercicio4
texto = input("Introduce un texto: ")
palabra = input("Introduce una palabra: ")
contador = texto.count(palabra)
if contador > 0:
    print(f"La palabra '{palabra}' aparece {contador} veces.")
else:
    print(f"La palabra '{palabra}' no está en el texto.")

