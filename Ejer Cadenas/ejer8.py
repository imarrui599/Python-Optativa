'''Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido.'''

precio = input("Introduce el precio con dos decimales: ")
div = precio.split('.')

print(div[0], ' euros y ' , div[1], ' centimos ')