'''Escribir una función que calcule el total de una factura tras aplicarle el IVA. La
función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el
total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá
aplicar un 21%.'''

def total(sinIva, conIva):
    return ((conIva * sinIva) / 100) + sinIva

sinIva = int(input('Ingrese la cantidad sin IVA: '))
conIva = int(input('Ingrese la cantidad con IVA: '))

print(total(sinIva,conIva))
