'''Escribir un programa que pregunte el nombre el un producto, su precio y un número
de unidades y muestre por pantalla una cadena con el nombre del producto seguido
de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.'''

producto = input(' Indica el producto: ')
precio = float(input(' Indica su precio '))
num_unidades = int(input(' ¿Cuantas unidades hay? '))
total = precio*num_unidades

print(f"{producto}: {precio:08.2f} {num_unidades:03d} {total:010.2f}")