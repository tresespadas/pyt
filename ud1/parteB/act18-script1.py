#!/usr/bin/env python3

notas_estudiantes = dict()

i = 1
while i <= 3:
    alumno = str(input(f"Nombre del alumno {i}: "))
    nota = int(input(f"Nota del alumno {i}: "))
    notas_estudiantes[alumno]=nota
    i += 1

print(notas_estudiantes)
