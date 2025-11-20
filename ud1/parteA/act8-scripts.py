#!/usr/bin/env python3

def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

try:
    num1=int(input("Número 1: "))
    num2=int(input("Número 2: "))
    print(f"Suma: {suma(num1,num2)}")
    print(f"Resta: {resta(num1,num2)}")
    print(f"Multiplicación: {mult(num1,num2)}")
    print(f"División: {div(num1,num2)}")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except ValueError:
    print("Debes especificar dos números")
finally:
    print("Fin del programa")
