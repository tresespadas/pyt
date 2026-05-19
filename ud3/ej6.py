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

class CuentaJoven(Cuenta):
  def __init__(self,titular,bonificacion,cantidad=0):
    super().__init__(titular,cantidad)
    self.bonificacion = bonificacion

  @property
  def bonificacion(self):
    return self._bonificacion

  @bonificacion.setter
  def bonificacion(self, porcentaje):
    if porcentaje < 0 or porcentaje > 100:
      raise ValueError("El porcentaje debe estar entre 0 y 100")
    else:
      self._bonificacion = porcentaje

  def esTitularValido(self, edad):
    if edad > 18 and edad < 25:
      return True
    else:
      return False

  def mostrar(self):
    print(f"Cuenta Joven con bonificacion de {self.bonificacion}%")


c1 = CuentaJoven("Álvaro",15,200)
c1.mostrar()
#print("¿Titular válido?", c1.esTitularValido(22))

c1.ingresar(200)
print(c1.cantidad)
