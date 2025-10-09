opcion = input("Dame una opción (A, B, C):")

match opcion :
    case "A" | "a":
        print("Alta")
    case "B" | "b":
        print("Baja")
    case "C" | "c":
        print("Cambio")
    case _:
        print("No válido")
