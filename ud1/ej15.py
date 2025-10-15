#!/bin/env python3

entrada=int(input("Número primo?: "))

if entrada<=1:
    print("No es primo")
    exit(0)

for i in range(2,entrada):
    if entrada%i==0:
        print("No es primo")
        exit(0)
print("Es primo")

