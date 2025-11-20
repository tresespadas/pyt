#!/usr/bin/env python3

def es_par(x):
    if x % 2 == 0:
        return True

suma=0
for i in range(1,17):
    if es_par(i):
        suma+=i

print(suma)
