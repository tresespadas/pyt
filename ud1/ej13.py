#!/bin/env python3

num=int(input("Introduce un número: "))

for i in range(1,11):
    print(f"{i} x {num} = ",i*num)
print("----------------------------")
j=1
while j<=10:
    print(f"{j} x {num} = ",j*num)
    j+=1
