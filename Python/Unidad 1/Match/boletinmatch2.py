mes = input("Introduce el número de mes:")
match mes:
    case "1" | "2" |"3":
        print("Estamos en invierno")
    case "4"|"5"|"6":
        print("Estamos en primavera")
    case "7"|"8"|"9":
        print("Estamos en verano")
    case "10"|"11"|"12":
        print("Estamos en otoño")
    case _:
        print("Ese número no es ningún mes")