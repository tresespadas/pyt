#!/bin/env python

import os, platform

# Ejercicio 0 (módulo os)
#print(os.name)

# Ejercicio 0 (módulo platform)
print(f"El nombre del sistema operativo es {platform.platform()}")

# Ejercicio 1
user_path = str(input("Ingresa una ruta absoluta: "))
try:
    dir = os.listdir(user_path)
    print(f"{user_path} se trata de un directorio")
except(NotADirectoryError):
    print(f"{user_path} se trata de un archivo")
except(FileNotFoundError):
    print(f"{user_path} no se encuentra en el sistema")

# Ejercicio 1 (otra forma de hacerlo)
#user_path = str(input("Ingresa una ruta absoluta: "))
#
#if not os.path.exists(user_path):
#    print(f"{user_path} no se encuentra en el sistema")
#elif os.path.isdir(user_path):
#    print(f"{user_path} se trata de un directorio")
#elif os.path.isfile(user_path):
#    print(f"{user_path} se trata de un archivo")

# Ejericio 2
file_path = str(input("Ingresa la ruta absoluta de un archivo: "))

if not os.path.exists(file_path):
    print(f"{file_path} no se encuentra en el sistema")
elif os.path.isdir(file_path):
    print(f"{file_path} se trata de un directorio")
elif os.path.isfile(file_path):
    #print(f"{file_path} se trata de un archivo")
    print(os.stat(file_path))

# Ejericio 3
