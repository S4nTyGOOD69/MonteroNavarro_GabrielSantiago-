palabra = "Palabra ejemplo"

for letra in palabra:
    print(letra)

#Ejercicio 3: Haz un programa que pida nombre y apellido. muestra en pantalla en formato Apellido,
# nombre con cada palabra iniciando en mayuscula.
nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")    

print(f"{apellido.capitalize()}, {nombre.capitalize()}")

#Ejercicio 4: pide una fase y una letra. Muestra cuantas veces aparece esa letra en la frase sin
#sin dsitinguir entre mayusculas y minusculas.
frase = input("Escribe una frase: ")
letra = input("Ecribe una letra que dese buscar: ")

frase_formateada = frase.strip().lower() 
letra_formateada = letra.strip().lower()

conteo_letra = frase_formateada.count(letra_formateada)

#ejercicio 5: pide una frase y reemplaza todas las vocales 'a' por '@' y muestra el resultado.
frase = input("Escribe una frase: ")
frase_formateada = frase.strip().lower()
frase_modificada = frase_formateada.replace("a", "@")
print("Frase modificada:", frase_modificada)

#ejercicio 6: pide un texto y extrae los primeros 10 caracteres. 
# si el texto tiene menos de 10 caracteres, muestra el texto completo.
texto = input("Escribe un texto o frase: ")
if len(texto) <=10:
    print(f"El texto completo es: '{texto}'")
else:
    texto_diez_caracteres = texto[:10]
    print(f"Los primeros 10 caracteres son: '{texto_diez_caracteres}'")

#################################################################
#                       LISTAS EN PYTHON
#################################################################
#las listas son indexables y mutables 
lista1 = [10,30,20,50,5,15] # lista
lista2 = ["manzana", "banana", "fresa", "pera", "naranja", 4 , 6.6, True]

print(lista1)
pringt(lista2)

for elemento in lista1:
    print(elemento)

for elemento in lista2:
    print(elemento)

#llenado de listas vacias 
lista3 = [] # lista vacia
#llenar la lista con datos ingresados por el usuario
for i in range(11):
    numero = int(input("Ingresa un numero entero: "))
    lista.append(numero) #agregar el numero ingresado a la lista 
                        # (append agrega un elemento al final de la lista)
print("Lista llena:", lista3)   
print(len(lista3))
print(sum(lista3))
lista3.reverse() #Invierte el orden de los elementos en la lista
print("Lista invertida:", lista3) 
lista3.sort() #Ordena los elementos de la lista en orden ascendente
print("Lista ordenada:", lista3)                         




