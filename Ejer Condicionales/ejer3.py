'''Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.'''

num1 = float(input("Introduzca el numero1: "))
num2 = float(input("Introduzca el numero2: "))
if num1 == 0 or num2 == 0:
    print('Error en la division')
else:
    print(f'El resultadod de la division es: {num1/num2}')

