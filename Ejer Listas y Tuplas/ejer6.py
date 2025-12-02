'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
usuario tiene que repetir.'''

asignaturas = ["Matemicas", "Fisica", "Qumica", "Historia", "Lengua"]
notas = []

for i in asignaturas:
    nota = float(input(f"Introduzca su nota para {i}: "))
    notas.append(nota)

asignaturas_repetir = []

x = 0
while x < len(asignaturas):
    if notas[x] < 5:
            asignaturas_repetir.append(asignaturas[x])
    x += 1
print(f"Las asignaturas que tienes que repetir son:  {asignaturas_repetir}")