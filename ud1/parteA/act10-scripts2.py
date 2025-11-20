#!/usr/bin/env python3

def contar(p,v):
    return p.count(v)

try:
    palabra=str(input("Inserta una palabra: "))
    vocal=str(input("Inserta una palabra: "))

    if len(vocal) > 1 or palabra.count(" ") > 0:
        print("Especifica una palabra y una vocal")
        exit() 

    print(f"La vocal '{vocal}' aparece {contar(palabra,vocal)} veces en la palabra '{palabra}'")
except ValueError:
    print("Especifica una palabra y una vocal")
finally:
    print("Fin del programa")
