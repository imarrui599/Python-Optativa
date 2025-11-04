'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.'''

num_ent = int(input("Introduzca un numero entero: "))
if num_ent > 1:
    for e in range (2, num_ent):
        if num_ent % e == 0:
            print("No es un numero primo")
    else:
        print("Es un numero primo")
else:
    print("Es un numero primo")