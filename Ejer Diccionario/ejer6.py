'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo
electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato
debe imprimirse el contenido del diccionario.'''

persona = {}
while True:
    clave = input("Introduce la clave: ")
    valor = input("Introduce el valor: ")
    persona[clave] = valor
    print(persona)

    continuar = input("¿Quieres continuar? (s/n): ")
    if continuar.lower() == "n":
        break
