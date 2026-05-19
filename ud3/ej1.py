#!/usr/bin/python3

class Calculadora:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def suma(self):
    return f"{self.x} + {self.y} = {self.x + self.y}"

  def resta(self):
    return f"{self.x} - {self.y} = {self.x - self.y}"

  def mult(self):
    return f"{self.x} * {self.y} = {self.x * self.y}"

  def dividir(self):
    return f"{self.x} / {self.y} = {self.x / self.y}"

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))
calc = Calculadora(num1,num2)
print(calc.suma())
print(calc.resta())
print(calc.mult())
print(calc.dividir())
