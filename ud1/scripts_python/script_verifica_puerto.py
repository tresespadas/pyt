#!/bin/env python3

def puerto_abierto(puerto):
    if puerto % 2 == 0 or puerto % 5 == 0:
        return True

user_port=int(input("Elige un puerto del 1 al 65535: "))
if user_port <= 65535 and user_port >= 1:
    if puerto_abierto(user_port):
        print(f"El puerto {user_port} está abierto")
    else:
        print(f"El puerto {user_port} está cerrado")
else:
    print(f"Puerto inválido")
    exit(1)

