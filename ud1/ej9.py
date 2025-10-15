#!/bin/env python3

num=int(input("Introduce un número: "))
res=1
for i in range(num,0,-1):
    res*=i
print(res)
