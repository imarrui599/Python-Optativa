'''Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta.'''

contraseña = "jethoven"
entrada = ""

while entrada != contraseña:
    entrada = input("Cual es la contraseña: ")

print("contraseña correcta")