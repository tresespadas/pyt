#!/usr/bin/python3

class Producto:
  def __init__ (self,codigo,nombre,precio,descripcion):
    self.__codigo = codigo
    self.__nombre = nombre
    self.__precio = precio
    self.__descripcion = descripcion

  @property
  def nombre(self):
    return self.__nombre
  
  @property
  def precio(self):
    return self.__precio

  @property
  def descripcion(self):
    return self.__descripcion

class Libro(Producto):
  def __init__(self,codigo,nombre,precio,descripcion,isbn,autor):
    super().__init__(codigo,nombre,precio,descripcion)
    self.isbn = isbn
    self.autor = autor

  def __str__(self):
    return f"El libro {self.nombre} es del autor {self.autor}"

class Juguete(Producto):
  def __init__(self,codigo,nombre,precio,descripcion,edad_recomendada):
    super().__init__(codigo,nombre,precio,descripcion)
    self.edad_recomendada = edad_recomendada

class Articulo(Producto):
  def __init__(self,codigo,nombre,precio,descripcion,categoria):
    super().__init__(codigo,nombre,precio,descripcion)
    self.categoria = categoria


l1 = Libro("123","El Quijote",13,"No tenéis lengua para escribir un Quijote","123asd123asd","Miguel de Cervantes")

print(l1.autor)
print(l1)
