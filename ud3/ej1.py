#!/usr/bin/python3

class Mascota:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"La mascota se llama {self.name} y tiene {self.age} edad."

perro = Mascota("Leo",17)
print(perro)
