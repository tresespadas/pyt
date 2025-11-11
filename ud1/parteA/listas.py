#!/usr/bin/env python3

# Creación de una lista
lista1=[1,2,3]
print(lista1)

# Añadiendo un elemento
lista1.append(4)
print(lista1)

# Eliminando un elemento (por posición)
del lista1[0]
print(lista1)

# Copia de lista
lista2=[1,2,3,4,5,6,7,8,9]
lista3=lista2[2:6]
print(lista3)

# Listas multidimensionales
matriz=[[1,2,3],[3,2,7],[1,2,1]]
print(matriz)
print(matriz[1][2])

# Metodos
lista=[1,5,6,-9,10]
print(lista)
# Método para ordenar
lista.sort()
print(lista)

# Función map
lista=[1,2,3,4,5,6]
def potencia(num):
    return num ** num
lista_potencia=list(map(potencia,lista))
print(lista_potencia)
