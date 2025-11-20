#!/usr/bin/env python3

def pos(x):
    if x >= 0:
        return True

lista=list()
while True:
    x=int(input("Número : "))
    if pos(x):
        lista.append(x)
    else:
        break

print(f"Lista original: {lista}")
lista.sort(); print(f"Lista ordenada: {lista}")
lista.sort(reverse=True); print(f"Lista inversamente ordenada: {lista}")
print(f"Máximo: {max(lista)}")
print(f"Mínimo: {min(lista)}")
