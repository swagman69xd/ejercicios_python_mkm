# coding=utf-8
__Author__ = "Miroslav Mitev"

def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplica(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

# Función que crea el menú de la aplicación.
def menuApp():
    print("MENU CALCULADORA")
    opcion = -1

    while opcion != 0:
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("0. Salir")

        opcion = int(input("Introduzca opción: "))

        if opcion == 1:
            s1 = int(input("Introduzca el primer sumando: "))
            s2 = int(input("Introduzca el segundo sumando: "))
            print("La suma de {0} + {1} = {2}.".format(s1, s2, suma(s1, s2)))
        elif opcion == 2:
            minuendo = int(input("Introduzca el minuendo: "))
            sustraendo = int(input("Introduzca el sustraendo: "))
            print("La resta de {0} - {1} = {2}.".format(minuendo, sustraendo, resta(minuendo, sustraendo)))
        elif opcion == 3:
            factor1 = int(input("Introduzca el primer factor: "))
            factor2 = int(input("Introduzca el segundo factor: "))
            print("La multiplicación de {0} * {1} = {2}.".format(factor1, factor2, multiplica(factor1, factor2)))
        elif opcion == 4:
            dividendo = int(input("Introduzca el dividendo: "))
            divisor = int(input("Introduzca el divisor: "))
            resultado = divide(dividendo, divisor)
            print("La división de {0} / {1} = {2}.".format(dividendo, divisor, resultado))
        elif opcion != 0:
            print("Error: Opción incorrecta, introduzca una nueva opción.")

# Programa principal
def main():
    menuApp()

if __name__ == "__main__":
    main()
