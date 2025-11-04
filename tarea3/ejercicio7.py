#az un programa que pida un número, y calcule la suma de todos los números, 
# desde el 1 hasta ese número. Por ejemplo, si ingresas 5, deberás sumar 1 + 2 + 3 + 4 +5.

numero = int(input("Ingrese un número: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print("La suma de los números desde 1 hasta", numero, "es:", suma)

