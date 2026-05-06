#!/usr/bin/python3

class Mascota:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"La mascota se llama {self.name} y tiene {self.age} edad."
    
    def cambiarEdad(self, age):
        self.age = age

class Perro(Mascota):
    def __init__(self, name, age, race):
        super().__init__(name, age)
        self.race = race

    def __str__(self):
        return f"El perro se llama {self.name}, tiene {self.age} años y es de raza {self.race}."

perro1 = Perro("Leo", 14, "Labrador")
print(perro1)
