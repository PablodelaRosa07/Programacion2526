dia = float(input("Introduce el día:"))
mes = float(input("Introduce el mes:"))
hemis = float(input("Introduce en qué Hemisferio estás, norte (1), o sur (2):"))
match hemis:
    case 1:
        match mes :
            case 1 | 2:
                print("Estás en invierno")
            case 12:
                if dia <= 20 and dia >= 1:
                    print("Estás en otoño")
                elif dia >= 21 and dia <= 31:
                    print("Estás en invierno")
            case 4 | 5:
                print("Estás en primavera")
            case 3:
                if dia <= 20 and dia >= 1:
                    print("Estás en invierno")
                elif dia >= 21 and dia <= 31:
                    print("Estás en primavera")
            case 7 | 8:
                print("Estás en verano")
            case 6:
                if dia <= 20 and dia >= 1:
                    print("Estás en primavera")
                elif dia >= 21 and dia <= 30:
                    print("Estás en verano")
            case 10 | 11:
                print("Estás en otoño")
            case 9:
                if dia <= 20 and dia >= 1:
                    print("Estás en verano")
                elif dia >= 21 and dia <= 30:
                    print("Estás en otoño")
            case _:
                print("Los datos no son válidos")
    
match hemis:
    case 2:
        match mes:
            case 1 | 2:
                print("Estás en verano")
            case 12:
                if dia <= 20 and dia >= 1:
                    print("Estás en primavera")
                elif dia >= 21 and dia <= 31:
                    print("Estás en verano")
            case 4 | 5:
                print("Estás en otoño")
            case 3:
                if dia <= 20 and dia >= 1:
                    print("Estás en verano")
                elif dia >= 21 and dia <= 31:
                    print("Estás en otoño")
            case 7 | 8:
                print("Estás en invierno")
            case 6:
                if dia <= 20 and dia >= 1:
                    print("Estás en otoño")
                elif dia >= 21 and dia <= 30:
                    print("Estás en invierno")
            case 10 | 11:
                print("Estás en primavera")
            case 9:
                if dia <= 20 and dia >= 1:
                    print("Estás en invierno")
                elif dia >= 21 and dia <= 30:
                    print("Estás en primavera")
            case _:
                print("Los datos no son válidos")