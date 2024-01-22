# coding=utf-8
__Author__ = "Miroslav Mitev"

# Función que determina si un número es primo.
def esPrimo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

# Programa principal
def main():
    print("ES PRIMO")
    n = int(input("Introduzca un numero: "))
    resultado = "primo" if esPrimo(n) else "no primo"
    print("{0} es {1}.".format(n, resultado))

if __name__ == "__main__":
    main()