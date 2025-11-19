#ejercicio9

contactos = []
nombre = input("Introduce el nombre del contacto: ")
telefono = input("Introduce el teléfono del contacto: ")
contactos.append((nombre, telefono))
diccionario_contactos = dict(contactos)
print("Diccionario de contactos:", diccionario_contactos)
