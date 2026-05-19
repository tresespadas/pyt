#!/usr/bin/python3

class Cuenta:
  def __init__(self,titular,cantidad=0):
    self.titular = titular
    self.cantidad = cantidad

  @property
  def titular(self):
    return self._titular

  @titular.setter
  def titular(self, texto):
    if not isinstance(texto, str):
      raise ValueError("Ingresa un cadena de texto")
    elif len(texto) == 0:
      raise ValueError("Ingresa un titular no vacío")
    else:
      self._titular = texto

  @property
  def cantidad(self):
    return self._cantidad

  @cantidad.setter
  def cantidad(self, numero):
    if numero < 0:
      raise ValueError("No se puede establecer una cantidad negativa")
    else:
      self._cantidad = numero

  def mostrar(self):
    print(f"La cuenta del titular {self.titular} posee una cantidad de {self.cantidad}€")

  def ingresar(self, numero):
    if numero < 0:
      raise ValueError("No se puede ingresar una cantidad negativa")
    else:
      self.cantidad += numero

  def retirar(self, numero):
    if numero < 0:
      raise ValueError("No se puede retirar una cantidad negativa")
    elif self.cantidad < numero:
      raise ValueError("La cuenta no dispone de tanta cantidad")
    else:
      self.cantidad -= numero

c1 = Cuenta("PepeLuis")
      
c1.mostrar()

c1.ingresar(400)
c1.mostrar()

try:
  c1.retirar(1000)
except ValueError as e:
  print(f"Error: {e}")
  
c1.mostrar()

