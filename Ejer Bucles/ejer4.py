'''Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.'''

num_entero = int(input("Introduce un número entero positivo: "))

if num_entero < 0:
    print("Por favor, introduce un número positivo.")
else:
    n = num_entero
    while n >= 0:
        if n > 0:
            print(n, end=", ")
        else:
            print(n)
        n -= 1






