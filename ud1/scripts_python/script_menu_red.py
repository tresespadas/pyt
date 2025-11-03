#!/bin/env python3

def ver_ip():
    print("La IP del servidor es la 192.168.121.200")
    return

def conexion(ip):
    print(f"Haciendo PING a {ip}")
    print(f"Paquete recibido")
    print(f"Paquete recibido")
    print(f"Paquete recibido")
    print(f"Paquete recibido")
    print(f"Total de paquetes enviados: 4")
    print(f"Total de paquetes recibidos: 4")
    print(f"Hay conexión con la ip {ip}")
    return

while True:
    print("\n1.- Ver IP del servidor")
    print("2.- Comprobar conexión")
    print("3.- Salir")

    opcion=int(input("Elige una opción: "))

    match opcion:
        case 1:
            ver_ip()
        case 2:
            user_ip=str(input("¿A qué IP le quieres hacer PING?: "))
            conexion(user_ip)
        case 3:
            print("Saliendo...")
            exit(0)
        case _:
            print("Opción inválida")


            
