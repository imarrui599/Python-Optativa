'''Escribir un programa que lea un entero positivo, , introducido
por el usuario y después muestre en pantalla la suma de todos
los enteros desde 1 hasta . La suma de los primeros enteros
positivos puede ser calculada de la siguiente forma:'''

numero_entero = int(input("Introduce un numero entero positivo:"))

if numero_entero > 0:
    suma = numero_entero * (numero_entero + 1) // 2
    print(f"La suma del entero del 1 al {numero_entero} es: {suma}")
else:
    print("Introduce un numero entero positivo")
