# coding=utf-8
__Author__="Miroslav Mitev"

def fibonacci(n):
    vector = []

    if n < 1:
        return vector
    elif n == 1:
        vector.append(1)
    else:
        vector.append(1)
        vector.append(1)
        for i in range(2, n):
            vector.append(vector[i-1] + vector[i-2])

    return vector

# Programa principal
def main():
    print("SERIE DE FIBONACCI")
    numero = int(input("Introduzca un numero: "))
    resultado = fibonacci(numero)
    print(f"{numero} elementos --> FIBONACCI: {resultado}")

if __name__ == "__main__":
    main()
