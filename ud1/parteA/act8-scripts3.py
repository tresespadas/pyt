#!/usr/bin/env python3

def rango(x):
    return range(1,x+1)

def lista(x):
    return list(x)

def tupla(x):
    return tuple(x)

try:
    x=int(input("Hasta qué número quieres imprimir por pantalla: "))
    print(lista((rango(x))))
    print(tupla((rango(x))))
except ValueError:
    print("Debes insertar un número")
