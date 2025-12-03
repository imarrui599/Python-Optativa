'''Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
palíndromo.'''

palabra = input("Introduce una palabra: ")

if palabra.lower() == palabra.lower()[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
