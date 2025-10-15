#!/bin/env python3

num_mes=int(input("Introduce el número de mes que quieres saber: "))
mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
if num_mes==2:
    print(mes[num_mes-1],"tiene 28 días")
elif num_mes in [4,6,9,11]: 
    print(mes[num_mes-1],"tiene 30 días")
elif num_mes>12:
    print("Sólo hay 12 meses")
    exit(1)
else:
    print(mes[num_mes-1],"tiene 31 días")
