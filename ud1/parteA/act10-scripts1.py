#!/usr/bin/env python3

def palindromo(x):
    if x[::-1] == x:
        return True

try:
    cad=str(input("Inserta un palabra: "))
    if palindromo(cad):
        print(f"{cad} es un palíndromo")
    else:
        print(f"{cad} no es un palíndromo")
except ValueError:
    print("Error: Tipo de dato incorrecto")
finally:
    print("Fin del programa")

