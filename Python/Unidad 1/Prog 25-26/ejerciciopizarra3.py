opcion = input("¿Qué día de la semana es?(L, M, X, J, V, S o D):")

match opcion :
    case "L" | "l" | "M" | "m" | "X" | "x" | "J" | "j" | "V" | "v" :
        print("Instituto")
    case "S" | "s" | "D" | "d":
        print("Casa")