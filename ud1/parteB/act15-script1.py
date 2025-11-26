#!/usr/bin/env python3

def f():
    i = 0
    l = list()
    while i < 6:
        x = input("Ingresa un valor para el set/frozenset: ")
        l.append(x)
        i += 1
    return l

lista = f()
s = set(lista)
lista = f()
fs = frozenset(lista)

print(s)
print(fs)
