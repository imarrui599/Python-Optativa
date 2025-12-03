'''Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal.'''

vocales = ["a","e","i","o","u"]
palabra = input("Introduce una palabra: ")

for i in vocales:
    times = 0
    for j in palabra:
        if i == j:
            times += 1
    print("la vocal ", i, "aparece ", times, "veces")



