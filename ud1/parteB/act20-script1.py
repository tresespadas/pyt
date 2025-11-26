#!/usr/bin/env python3

nombre_fichero = str(input("¿Cómo se llama el fichero que quieres crear?: "))

try:
    f = open(nombre_fichero,"w")
    f.writelines(["Línea 1\n","Línea 2\n","Línea 3\n"])
    f.close()

    f = open(nombre_fichero,"r")
    print(f.readlines())
    f.close()
except:
    print(f"No se pudo crear el fichero {nombre_fichero}")
