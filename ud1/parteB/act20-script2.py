#!/usr/bin/env python3

nombre_fichero = str(input("¿Cómo se llama el fichero que quieres crear?: "))

try:
    f = open(nombre_fichero,"w")
    frase = str(input(f"Escribe un frase para el fichero {f.name}: "))
    f.write(frase)
    f.close()
    
    f = open(nombre_fichero,"r")
    print(f.read())
    f.close()
except:
    print(f"No se pudo crear el fichero {nombre_fichero}")
