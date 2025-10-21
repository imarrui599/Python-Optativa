'''Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por
comas.'''

num_entero = int(input(' Introduce un numero entero positivo: '))
n = -1

while n < (num_entero):
    n = n + 2
    print (n, end=', ')


