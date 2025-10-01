'''Una panadería vende barras de pan a 3.49€ cada una. El pan
que no es el día tiene un descuento del 60%. Escribir un
programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el
precio habitual de una barra de pan, el descuento que se le
hace por no ser fresca y el coste final total.'''

pan = 3.49
descuento = (60 * 100 / 3.49)
pan_vendidoNo = int(input("Cuantas barras que no son del dia se han vendido:"))
pan_vendidoDia  = int(input("Cuantas barras de pan del dia se han vendido:"))

print("Se han vendido", pan_vendidoNo, "que normalmente valen 3.49 € pero al no ser del dia tienen un descuento de 60%")
print("Se han vendido en total", pan_vendidoDia + pan_vendidoNo, "barras de pan, que es en total", pan_vendidoDia * pan + pan_vendidoNo * pan)

