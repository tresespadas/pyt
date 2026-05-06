#!/usr/bin/python3

class Profesor:
    def __init__(self, nombre, asignaturas):
        self.nombre = nombre
        self.asignaturas = asignaturas

    def __str__(self):
        return f"El profesor se llama {self.nombre} e imparte las asignaturas: {self.asignaturas}."

class Estudiante:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.edad = curso

    def __str__(self):
        return f"El Estudiante se llama {self.nombre} y está en {self.curso} curso."

profe = Profesor("Pepe",["Lengua","Matemáticas"])
print(profe)
