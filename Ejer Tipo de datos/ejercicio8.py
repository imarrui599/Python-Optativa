'''Escribir un programa que pida al usuario dos números enteros
y muestre por pantalla la <n> entre <m> da un cociente <c>
y un resto <r> donde <n> y <m> son los números introducidos
por el usuario, y <c> y <r> son el cociente y el resto de la
división entera respectivamente.'''

num1_entero = int(input("Introduzca un numero entero"))
num2_emtero = int(input("Introduzca otro numero entero"))
cociente = num1_entero / num2_emtero
resto = num1_entero % num2_emtero

print("El resultado es:", cociente ,"y el resto es:", resto)