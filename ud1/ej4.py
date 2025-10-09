#!/bin/env python3

cant=int(input("Introduce la cantidad en MB: "))
unid=input("¿A qué unidades lo quieres convertir?[GB/TB]: ")

if unid=='GB':
    cant=cant/1024
    print("El disco duro tiene",cant,"GB")
elif unid=='TB':
    cant=cant/1024/1024
    print("El disco duro tiene",cant,"TB")
else:
    print("Unidad no especificada correctamente: [GB/TB]")

