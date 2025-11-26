#!/usr/bin/env python3

mi_diccionario={'root':'toor', 'user1':'passw0rd', 'user2':'cGFzc3dvcmQ'}

# Imprimir el diccionario
for i,j in mi_diccionario.items():
    print(f"{i} = {j}")

# Acceder a un valor mediante su clave
for i,j in mi_diccionario.items():
    if i == "user2":
        print(f"La clave {i} tiene un valor de {j}")

# Modificar un valor de una de las claves
for i,j in mi_diccionario.items():
    if i == "root":
        mi_diccionario[i]='746f6f72'

# Añadir un nuevo par clave-valor
mi_diccionario['user3']='hfre6'

# Imprimir el diccionario
print(mi_diccionario)

# Iterar sobre las claves
for i in mi_diccionario.keys():
    print(i)

# Iterar sobre los valores
for i in mi_diccionario.values():
    print(i)

# Iterar sobre ambos
for i,j in mi_diccionario.items():
    print(f"{i} = {j}")

# Imprimir claves
print(mi_diccionario.keys())

# Imprimir valores
print(mi_diccionario.values())

# Imprimir ambos
print(mi_diccionario.items())
