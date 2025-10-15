#!/bin/env python3

entrada=input("Introduce un carácter en mayúscula o minúscula: ")
if entrada.isupper():
    print(f"{entrada} es una letra mayúscula")
else:
    print(f"{entrada} es una letra minúscula")
