#!/bin/env python3

var='animal'
print(f"La variable var vale { var }")
del var
try:
    print(f"La variable var vale { var }")
except NameError:
    print('La variable que quieres imprimir se borró')

x=1
print(f"\nLa variable x vale { x }")
print(f"eval('x+1') es igual a { eval('x+1') }")
print(f"El tipo de x vale { type(x) }")
print(f"El tipo de eval('x+1') vale { type(eval('x+1')) }")

variable='3'
print(f"\nLa variable 'variable' vale { variable }")
print(f"\nEl tipo de la variable 'variable' vale { type(variable) }")
variable=3
print(f"\nLa variable 'variable' vale { variable }")
print(f"\nEl tipo de la variable 'variable' vale { type(variable) }")

for i in range(1,5):
    print("Estoy en un bucle for")

for i in range(1,10):
    if i==2:
        continue
    elif i==3:
        pass
    elif i==7:
        break
    else:
        print(i)
