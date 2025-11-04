'''Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
que el usuario escriba “salir” que terminará.'''

eco = ""

while eco.lower() != "salir":
    eco = input("Introduce una frase y escribe salir para acabar: ")
    if eco.lower() != "salir":
        print(eco)

        
