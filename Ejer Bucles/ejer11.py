'''Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la última.'''

palabra = str(input("Introduce una palabra: "))
invertida = palabra[::1]

for letra in invertida:
    print(letra)
