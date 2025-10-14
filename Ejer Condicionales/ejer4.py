'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es par o impar.'''

num_entero = int(input("Introduzca un numero entero: "))
if num_entero % 2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')