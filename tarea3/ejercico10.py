opcion = 0

while opcion != 5:
    print("calculadora")
    print("1- suma")
    print("2- resta")
    print("3- multiplicacion")
    print("4- division")
    print("5- salir")

    opcion = int(input("Elija una opcion"))

    if opcion >= 1 and opcion <= 4: 
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))

        if opcion == 1:
            print("resultado:", num1 + num2)
        elif opcion == 2:
            print("resultado", num1 - num2)
        elif opcion == 3:
            print("resultado", num1 * num2) 
        elif opcion == 4:
            if num2 != 0:
             print("resultado", num1 / num2)       
            else :
                print("Error: no se puede dividir entre cero.")
    elif opcion == 5:
        print("saliendo de la calculadora")
    else: 
        print("opcion no valida, intente de nuevo")
                    