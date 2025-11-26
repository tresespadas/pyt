#!/usr/bin/env python3

f = open("prueba.txt","w")
f.writelines(["Línea 1\n","Línea 2\n", "Línea 3\n"])
f.close()

f = open("prueba.txt","r")
print(f.readlines())
f.close()

with open("nuevo.txt","w") as f:
    for i in range(4):
        x = input("Escribe una línea de texto: ")
        f.write(x + "\n")

#with open("acabello_datos.txt","w+") as f:
#    for linea in f:
#        f.write("Línea cambiada")

with open("datos.txt","r") as f:
    print(f"El fichero {f.name} tiene {len(f.read())} caracteres")

with open("registro.log","r") as registro:
    errores = open("errores.log","w")

    for i in registro:
        if "Error" in i:
            errores.write(i)
    errores.close()
