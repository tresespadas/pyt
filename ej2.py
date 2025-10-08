#!/bin/env python3

num1=int(input("Número 1: "))
num2=int(input("Número 2: "))

print(num1+num2)
print(num1-num2)
print(num1*num2)
if num2==0:
    print("No se puede dividir entre cero")
    exit
else:
    print(num1/num2)
