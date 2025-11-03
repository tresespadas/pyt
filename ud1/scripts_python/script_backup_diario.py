#!/bin/env python3

def crear_copia(fichero):
    print(f"Creando la copia de seguridad del fichero {fichero}")
    return

def restaurar_copia(fichero):
    print(f"Restaurando la copia de seguridad del fichero {fichero}")
    return

while True:
    print("1.- Crear copia")
    print("2.- Restaurar copia")
    print("3.- Salir")

    opcion=int(input("Elige una opción: "))

    match opcion:
        case 1:
            fichero=input("¿Sobre qué fichero quieres crear la copia?")
            crear_copia(fichero)
        case 2:
            fichero=input("¿Sobre qué fichero quieres restaurar la copia?")
            restaurar_copia(fichero)
        case 3:
            print("Saliendo...")
            exit(0)
        case _:
            print("Opción inválida")


            
