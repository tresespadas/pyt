#!/usr/bin/env python3

lista=list()
while True:
    x=str(input("¿Quieres insertar un número en la lista?(s/n): "))
    if x == "s" or x == "S":
        y=int(input("Número: "))
        lista.append(y)
    else:
        break

lista2 = lista.copy()
lista2.sort()
if lista == lista2:
    print(f"La lista está ordenada")
    print(lista2)
else:
    print(f"La lista no está ordenada\nSe procede a ordenarla")
    print(lista2)
