#!/usr/bin/python3

class Persona:
  def __init__(self,nombre="",edad=0,dni=""):
    self.nombre = nombre
    self.edad = edad
    self.dni = dni

  @property 
  def nombre(self):
    return self._nombre

  @nombre.setter
  def nombre(self, texto):
    if texto == "":
      raise ValueError("El nombre de la persona no puede estar vacio")
    else:
      self._nombre = texto

  @property 
  def edad(self):
    return self._edad

  @edad.setter
  def edad(self, numero):
    if numero < 0:
      raise ValueError("La edad no puede ser negativa")
    else:
      self._edad = numero

  @property 
  def dni(self):
    return self._dni

  @dni.setter
  def dni(self, numero):
    if len(numero) != 9:
      raise ValueError("El dni debe constar de 9 caracteres")
    else:
      self._dni = numero

  def mostrar(self):
    return f"Los datos de la persona son: {self.nombre} , {self.edad} , {self.dni}"

  def esMayorDeEdad(self):
    if self.edad > 18:
      print("Es mayor de edad")
    else:
      print("No es mayor de edad")

p1 = Persona("Álvaro",31,"32098038C")

print(p1.mostrar())

p1.esMayorDeEdad()
