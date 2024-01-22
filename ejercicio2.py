def main():
    nombre = input("Introduzca su nombre: ")
    try:
        edad = int(input(f"Introduzca su edad, {nombre}: "))
    except ValueError:
        print("Por favor, introduzca una edad válida (número entero).")
        return

    # Comprobamos si es mayor de edad - Estructura condicional if - else
    if edad >= 18:
        print(f"{nombre}, ya puede conducir.")
    else:
        print(f"{nombre}, todavía eres menor de edad.")

if __name__ == "__main__":
    main()