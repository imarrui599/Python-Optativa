import math

'''Escribir un programa que pregunte por una muestra de números, separados por
comas, los guarde en una lista y muestre por pantalla su media y desviación típica'''

entrada = input("Introduce una muestra de números separados por comas: ")
lista_texto = entrada.split(",")

numeros = []
for numero_texto in lista_texto:
    numeros.append(int(numero_texto))

cantidad_numeros = len(numeros)
media = sum(numeros) / cantidad_numeros

suma_cuadrados = 0
for numero in numeros:
    suma_cuadrados += (numero - media) ** 2

varianza = suma_cuadrados / cantidad_numeros
desviacion = math.sqrt(varianza)

print("Media:", media)
print(f"Desviación típica: {desviacion}")
