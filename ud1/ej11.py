#!/bin/env python3

str_mes=str(input("Introduce las tres primeras letras del mes que quieres saber: "))
mes_dict={"ene":"Enero","feb":"Febrero","mar":"Marzo","abr":"Abril","may":"Mayo","jun":"Junio","jul":"Julio","ago":"Agosto","sep":"Septiembre","oct":"Octubre","nov":"Noviembre","dic":"Diciembre"}
for i, (letras, mes) in enumerate(mes_dict.items()):
    if str_mes==letras:
        if i+1==2:
            print(mes,"tiene 28 días")
        elif (i+1) in [4,6,9,11]: 
            print(mes,"tiene 30 días")
        else:
            print(mes,"tiene 31 días")
