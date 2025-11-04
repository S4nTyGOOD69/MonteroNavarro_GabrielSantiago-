 
numero = int(input("Ingrese un numero entero: "))
if numero % 2 == 0 and numero % 3 == 0:
    print(f"El numero {numero} es divisible entre 2 y 3.")
elif numero % 2 == 0:
    print(f"El numero {numero} es divisible entre 2.") 
elif numero % 3 == 0:
    print(f"El numero {numero} es divisible entre 3.")
else:
    print(f"El numero {numero} no es divisibles entre 2 y 3.")

