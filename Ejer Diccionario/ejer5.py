asignatura = {'Matematicas': 6, 'Fisica': 4, 'Quimica': 5}
total = 0

for i in asignatura:
    print(f"La asignatura {i}, tiene {asignatura[i]} creditos")
    total += asignatura[i]
    
print(f"El total de creditos es {total}")