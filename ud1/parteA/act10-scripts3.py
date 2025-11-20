#!/usr/bin/env python3

def crear():
    try:
        x=str(input("Inserta una cadena: "))
    except ValueError:
        print("Inserta un dato convertible a cadena")

    return x

def tamano(x):
    return len(x)

def buscar(x,y):
    lista = list()
    for pos, letra in enumerate(x):
        if letra == y:
            lista.append(pos)
    return lista

def mayus(x):
    return x.upper()

while True:
    print("a. Crear una cadena")
    print("b. Indicar el tamaño de la cadena")
    print("c. Buscar un carácter que se reciba por parámetros")
    print("d. Convertir en mayúsculas")
    print("e. Salir")

    try:
        opt=str(input("Opción: "))
    except ValueError:
        print("Inserta una opción válida")

    match opt:
        case "a":
                cadena = crear()
                print(f"Se ha creado la cadena {cadena}")
        case "b": 
            try: 
                print(f"El tamaño de la cadena '{cadena}' es {tamano(cadena)}")
            except NameError:
               print("Cadena no definida") 
        case "c":
            try:
                letra=str(input("Letra a buscar: "))
            except NameError:
               print("Cadena no definida") 
            except ValueError:
                print("Inserta un tipo de dato válido")

            try:
                buscar(cadena,letra)
                print(f"Hay un caracter '{letra}' en la(s) posición(es) {buscar(cadena,letra)} de la cadena '{cadena}'")
            except NameError:
               print("Cadena no definida") 
            except ValueError:
                print(f"No hay caracter '{letra}' en la cadena '{cadena}'")
        case "d":
            try:
                print(mayus(cadena))
            except NameError:
               print("Cadena no definida") 
        case "e":
            exit()
