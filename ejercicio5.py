'''Escribir un programa que pregunte al usuario por el número de
horas trabajadas y el coste por hora. Después debe mostrar
por pantalla la paga que le corresponde.'''

horas_trabajadas = float(input("Introduce el numero de horas trabajadas"))
coste_hora = float(input("Introduce el coste por hora"))

paga = horas_trabajadas * coste_hora
print("La paga que le corresponde es:", paga)