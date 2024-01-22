# coding=utf-8
__Author__ = "Miroslav Mitev"

def fibonacci(n):
    vector = []

    if n < 1:
        return vector
    elif n == 1:
        vector.append(1)
        return vector
    else:
        vector.append(1)
        vector.append(1)
        while len(vector) < n:
            vector.append(vector[-1] + vector[-2])

    return vector

# Programa principal
def main():
    print("SERIE DE FIBONACCI")
    numero = int(input("Introduzca un numero: "))
    print("{0} elementos --> FIBONACCI: {1}.".format(numero, fibonacci(numero)))

if __name__ == "__main__":
    main()
