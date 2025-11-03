#!/bin/env python3

def verifica_usuario(nombre):
	if nombre == 'admin':
		return True
	else:
		return False


user_input=input("Escribe un nombre de usuario: ")
if verifica_usuario(user_input):
	print(f"El usuario {user_input} se encuentra en el sistema")
else: 
	print(f"El usuario {user_input} NO se encuentra en el sistema")
