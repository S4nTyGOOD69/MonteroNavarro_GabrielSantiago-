#Haz un programa que pida una frase y cuenta cuántas letras tiene la frase, sin contar espacios
frase = input("Introduce una frase: ")
frase_sin_espacios = frase.replace(" ", " ")
contador_Letras = len(frase_sin_espacios)
print(f"La frase tiene {contador_Letras} letras (sin contar espacios). ")

