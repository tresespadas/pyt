#!/bin/env python3

def bisiesto(num):
    if num%400==0:
        print("Es bisiesto")
    elif num%100!=0 and num%4==0:
        print("Es bisiesto")
    else:
        print("No es bisiesto")

entrada=int(input("Año: "))
bisiesto(entrada)
