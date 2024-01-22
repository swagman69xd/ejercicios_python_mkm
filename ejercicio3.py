# coding=utf-8
__Author__ = "Miroslav Mitev"

def obtenerCalificaion(nota):
    if 0 <= nota < 3:
        calificacion = "Muy deficiente"
    elif 3 <= nota < 5:
        calificacion = "Insuficiente"
    elif 5 <= nota < 6:
        calificacion = "Suficiente"
    elif 6 <= nota < 7:
        calificacion = "Bien"
    elif 7 <= nota < 9:
        calificacion = "Notable"
    elif 9 <= nota <= 10:
        calificacion = "Sobresaliente"
    else:
        calificacion = "Incorrecta"
    return calificacion

def main():
    n = int(input("Introduzca la nota: "))
    print('Calificación: ' + obtenerCalificaion(n))

if __name__ == "__main__":
    main()