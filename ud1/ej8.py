#!/bin/env python3
import random

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Jugar")
    print("2. Ayuda")
    print("3. Salir")

def jugar():
    secreto = random.randint(1, 10)
    intentos = 0
    print("\n¡Adivina el número del 1 al 10!")

    while True:
        intento = int(input("Tu intento: "))
        intentos += 1
        if intento < secreto:
            print("Demasiado bajo. Intenta otra vez.")
        elif intento > secreto:
            print("Demasiado alto. Intenta otra vez.")
        else:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.\n")
            break

def ayuda():
    print("Este es un juego simple donde debes adivinar un número secreto entre 1 y 10. El juego te dirá si tu intento es demasiado alto o bajo.")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-3): ")

    if opcion == '1':
        jugar()
    elif opcion == '2':
        ayuda()
    elif opcion == '3':
        print("Gracias por jugar. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")


