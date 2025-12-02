'''Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
a mayor.'''

numeros_ganadores = [33224, 54896, 36471, 25803]
for i in range(6):
    numero = int(input(" Pon los numeros ganadores de la loteria: "))

    numeros_ganadores.sort()
    print('Los mumeros ganadores son ' + str(numero))


