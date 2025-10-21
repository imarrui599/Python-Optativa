'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión.'''

cantidad = float(input('¿Que cantidad quieres invertir?: '))
interes = float(input('¿Cual es el interes anual en %?:  '))
num_años = int(input('¿Cuantos años piensas invertir?: '))

for año in range(1, num_años + 1):
    cantidad *= (1 + interes / 100)
    print('El capital obtenido en el año', año, 'es de:', round(cantidad, 2))