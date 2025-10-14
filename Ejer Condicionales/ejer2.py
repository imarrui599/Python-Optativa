'''Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin
tener en cuenta mayúsculas y minúsculas.'''

contraseña = input("Introduzca la contraseña: ")
contraseña_c = input("Confirme la contraseña: ")
if contraseña.lower() == contraseña_c.lower():
    print('Contraseña correcta')
else:
    print('Contraseña incorrecta')