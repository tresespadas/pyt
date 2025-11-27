#!/usr/bin/env python3

with open("fichero1.txt", "r") as f:
    lineas = f.readlines()

print(f"Antes: {lineas}")
for i in lineas:
    if i == 2:
        lineas[i] = "Línea cambiada\n"
print(f"Después: {lineas}")

with open("fichero1.txt", "w") as f:
    f.writelines(lineas)
