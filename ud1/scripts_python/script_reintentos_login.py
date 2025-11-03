#!/bin/env python3

CUENTA="admin"
PASS="admin"

def verifica_login(usuario,clave):
    if usuario == CUENTA and clave == PASS:
        return True
    else:
        return False

intentos=0
while intentos < 4:
    usuario_input=input("Usuario: ")
    pass_input=input("Contraseña: ")
    
    if verifica_login(usuario_input,pass_input):
        print("Acceso permitido")
        exit(0)
    else:
        print("Credenciales erroneas")
        intentos +=1
print("Cuenta bloqueada")


