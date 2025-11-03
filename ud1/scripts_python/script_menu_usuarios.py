#!/bin/env python3

def anadir_usuario():
	mensaje="Estás en la funcion anadir_usuario"
	print(mensaje)

def eliminar_usuario():
	mensaje="Estás en la funcion eliminar_usuario"
	print(mensaje)

def listar_usuarios():
	mensaje="Estás en la funcion listar_usuarios"
	print(mensaje)

def salir():
	print("Saliendo del programa...")
	exit();

while True:
	print("1.- Añadir usuario al sistema")
	print("2.- Eliminar usuario del sistema")
	print("3.- Listar usuarios del sistema")
	print("4.- Salir")
	user_input=int(input("Elige una opción: "))
	
	match user_input:
		case 1:
			anadir_usuario()
		case 2:
			eliminar_usuario()
		case 3:
			listar_usuarios()
		case 4:
			salir()
		case _:
			print("Opción inválida")

