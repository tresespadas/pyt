#!/bin/env python

import os

# Imprime el directorio de trabajo
print(f"La ruta actual es {os.getcwd()}")

# Lista el contenido del directorio de trabajo
print(f"El contenido del directorio de trabajo es {os.listdir(os.getcwd())}")

# Crea un nuevo directorio en el directorio de trabajo
nombre_dir=str(input("\nInserta un nombre para un nuevo directorio: "))
try:
    os.mkdir(nombre_dir)
except(FileExistsError):
    print("Ya existe un directorio con ese nombre")
finally:
    print(f"Listando de nuevo el contenidoo del directorio de trabajo: {os.listdir(os.getcwd())}")
