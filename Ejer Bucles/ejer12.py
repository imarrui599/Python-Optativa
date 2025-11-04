'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase.'''

frase = input("Introduzca una frase: ")
letra = input("Introduzca una letra: ")

print("La letra", letra, "aparece", frase.count(letra), "veces en la frase.")
