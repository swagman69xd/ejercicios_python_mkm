def esMayorEdad(edad):
    return edad >= 18

def main():
    nombre = input("Por favor, introduce tu nombre: ")
    edad = int(input("Por favor, introduce tu edad: "))

    if esMayorEdad(edad):
        print(f"{nombre}, ya puedes conducir.")
    else:
        print(f"{nombre}, todavía no puedes conducir.")

if __name__ == "__main__":
    main()
