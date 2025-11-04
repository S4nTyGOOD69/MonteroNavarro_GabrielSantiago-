
conteo_divisibles = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        conteo_divisibles += 1
        print(i) 
    print(f'hay {conteo_divisibles} numeros divisibles entre 3 y 5 del 1 al 100.')



