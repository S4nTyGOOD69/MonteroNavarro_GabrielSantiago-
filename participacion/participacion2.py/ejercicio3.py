#ejercicio3

#ejercicio3

numero = int(input("Introduce un numero: "))
print(f"tabla de multiplicar del {numero}: ")
for i in range(0, 21, 2):
    resultado= numero * i
    print(f'{numero} x {i} = {resultado}')