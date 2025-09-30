'''Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por
pantalla el capital obtenido en la inversión.'''

capital = float(input('El capital es de'))
tiempo = float(input('que tiene un tiempo de'))
interes = int(input('Cuanto interes tiene tu inversion'))

final = (interes / 100 * capital * tiempo)
print('Tu beneficio es de', final)