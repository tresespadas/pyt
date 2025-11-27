#!/usr/bin/env python3

def f1(x,y):
    with open(x,"w") as f:
        f.write(y)
    return

def f2(x):
    with open(x,"r") as f:
        print(f.read())
    return

x = str(input("¿Cómo se va a llamar el fichero?: "))
y = str(input(f"¿Qué frase quieres escribir en {x}: "))
f1(x,y)
f2(x)
