'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
<nombre> tiene <edad> años, vive en <dirección> y su número de
teléfono es <teléfono>.'''

personas = {}
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu dirección: ")
telefono = int(input("Introduce tu teléfono: "))

datos = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}

print(f"{datos['nombre']}, tiene {datos['edad']} años, vive en {datos['direccion']} y su número de teléfono es {datos['telefono']}")