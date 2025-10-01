'''Imagina que acabas de abrir una nueva cuenta de ahorros que
te ofrece el 4% de interés al año. Estos ahorros debido a
intereses, que no se cobran hasta finales de año, se te añaden
al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la
cuenta de ahorros, introducida por el usuario. Después el
programa debe calcular y mostrar por pantalla la cantidad de
ahorros tras el primer, segundo y tercer años. Redondear cada
cantidad a dos decimales.'''

deposito = float(input("Introduzca cuanto dinero va a depositar"))
interes = 0.04 

saldo1 = deposito * (1 + interes)
saldo2 = saldo1 * (1 + interes)
saldo3 = saldo2 * (1 + interes)

saldo1red = round(saldo1, 2)
saldo2red = round(saldo2, 2)
saldo3red = round(saldo3, 2)

print("El saldo tras el primer año es de:", saldo1, "€")
print("El saldo tras el segundo año es de:", saldo2, "€")
print("El sado tras el tercer año es de:", saldo3, "€")
        