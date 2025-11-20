#!/usr/bin/env python3

def rellenar(x):
    while True:
        y=input("Introduce un valor para insertar en la lista: ")
        if y != "xx":
            x.append(y)
        else:
            break
    return x

def insertar(x,index):
    y=input("Introduce un valor para insertar en la lista: ")
    x.insert(index,y)
    return x

def crear_tupla():
    t=tuple()
    while True:
        y=int(input("Introduce un entero para la tupla: "))
        if y != 0:
            try:
                t.append(y)
            except AttributeError:
                print("Las tuplas son inmutables")
        else:
            break
    return t
        
def operaciones(x):
    try:
        print(f"Máximo: {max(x)}")
        print(f"Mínimo: {min(x)}")
        print(f"Longitud: {len(x)}")
    except ValueError:
        print("La tupla está vacia")
    finally:
        return

while True:
    print("a. Rellenar lista")
    print("b. Insertar un elemento en la lista")
    print("c. Crear tupla")
    print("d. Operaciones con tuplas")
    print("x. Imprimir lista")
    print("e. Salir")

    opt=str(input("Elige una opción: "))

    match opt:
        case "a":
            lista=list()
            rellenar(lista)
        case "b":
            pos=int(input("Posición para insertar: "))
            insertar(lista,pos)
        case "c":
            tupla = crear_tupla()
        case "d":
            operaciones(tupla)
        case "e":
            exit()
        case "x":
            try:
                print(lista)
            except NameError:
                print("Debes crear primero la lista\n")
        case "_":
            print("Opción inválida")
            
