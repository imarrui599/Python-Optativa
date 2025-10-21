'''Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.'''

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
n = 0
while n < 10:
    n = n + 1

    multiplicacion = n*numero
    print(multiplicacion)