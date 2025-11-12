#!/bin/env python3

# 5.Lista alfabética
lista1=["a","h","n","e","d","f","t","u","i","k","l","c","m"]
print(lista1)

lista1.sort()
print(lista1)

lista1.reverse()
print(lista1)

# 6.Comprobar si un elemento está en la lista
for i in lista1:
    if i=="l":
        print(f"La letra {i} se encuentra en la lista")
        break


