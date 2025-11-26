#!/usr/bin/env python3

def f(l):
    s = set(l)
    return s

lista = [1,2,3,4,1,2,5,6,7,2,1,2,4,2,2,3,5,6,7,8,9,0]
print(f"Lista inicial: {lista}")
lista2 = list(f(lista))
print(f"Lista final: {lista2}")
