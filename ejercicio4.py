# coding=utf-8
__Author__ = "Miroslav Mitev"

import random

def quienGana(jugada1, jugada2):
    if jugada1 == jugada2:
        return 0
    elif (jugada1 == "piedra" and jugada2 == "tijera") or (jugada1 == "tijera" and jugada2 == "papel") or (jugada1 == "papel" and jugada2 == "piedra"):
        return 1
    else:
        return 2

def main():
    print("PIEDRA, PAPEL, ... ¡TIJERA!")

    nombre1 = input("Introduzca el nombre del Jugador 1: ")
    nombre2 = input("Introduzca el nombre del Jugador 2: ")
    numeroTirada = int(input("Introduzca el número de tiradas: "))

    ganadas1 = 0
    ganadas2 = 0

    for _ in range(numeroTirada):
        j1 = random.choice(["piedra", "papel", "tijera"])
        j2 = random.choice(["piedra", "papel", "tijera"])
        
        print(f"Tirada: {nombre1} ha sacado {j1}. {nombre2} ha sacado {j2}.")
        
        ganador = quienGana(j1, j2)
        
        if ganador == 0:
            print("Han empatado.")
        elif ganador == 1:
            print(f"Gana {nombre1}")
            ganadas1 += 1
        else:
            print(f"Gana {nombre2}")
            ganadas2 += 1

    # Resultado final de todas las tiradas
    if ganadas1 > ganadas2:
        print(f"GANA {nombre1}")
    elif ganadas2 > ganadas1:
        print(f"GANA {nombre2}")
    else:
        print("HAN EMPATADO")

if __name__ == "__main__":
    main()
