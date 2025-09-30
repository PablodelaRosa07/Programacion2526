opcion = (input("Introduce día de la semana:"))
opcion = opcion.upper()
print(opcion)
match opcion:
    case "LUNES":
        print("El horario es:")
        print("================")
        print("LUNES")
        print("================")
        print("8-9 FOL")
        print("9-10 EDE")
        print("10-11 PROG")
        print("11-11:30 Recreo")
        print("11:30-12 PROG")
        print("12-14 BBDD")
    case "Domingo" | "domingo" | "DOMINGO" | "SABADO" | "SÁBADO" | "sabado" | "sábado" | "Sabado" | "Sábado":
        print("Día de estudio y reflexión")
    case "MARTES":
        print("El horario es:" \
            "==============" \
            "MARTES" \
            "==============" \
            "8-10 PROG" \
            "10-11 LDM" \
            "11-11:30 LDM" \
            "11:30-13:30 LDM" \
            "13:30-14:30 ITPE")
    case _:
        print("Valor incorrecto")