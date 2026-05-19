#!/usr/bin/python3

class Alumno:
  def __init__ (self,nombre,nif,nota):
    self.nombre = nombre
    self.nif = nif
    self.nota = nota

  @property
  def nombre(self):
    return self.__nombre

  @property
  def nif(self):
    return self.__nif

  @property
  def nota(self):
    return self.__nota

  @nombre.setter
  def nombre(self, texto):
    if texto == "":
      raise ValueError("El nombre no puede estar vacío")
    else:
      self.__nombre = texto

  @nif.setter
  def nif(self, texto):
    if len(texto) != 9:
      raise ValueError("El nif debe contener 9 caracteres")
    else:
      self.__nif = texto

  @nota.setter
  def nota(self, num):
    if num < 0:
      raise ValueError("La nota no puede ser negativa")
    else:
      self.__nota = num

try:
  alumno1 = Alumno("Pepe","12345678A",5)
  print(alumno1.nombre)
except ValueError as e:
  print(f"No se pudo crear el alumno: {e}")

try:
  alumno2 = Alumno("Luis","123",-1)
  print(alumno2.nombre)
except ValueError as e:
  print(f"No se pudo crear el alumno: {e}")
