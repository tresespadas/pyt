#!/usr/bin/env python3

notas_estudiantes = {'Pepe':2, 'Luis':3, 'María':1}

max_nota = max(notas_estudiantes.values())
for i,j in notas_estudiantes.items():
    if j == max_nota:
        print(f"El estudiante con la nota máxima es {i} con un {j}")
