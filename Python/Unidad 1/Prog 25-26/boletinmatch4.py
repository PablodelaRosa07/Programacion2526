dia = float(input("Introduce el día:"))
mes = float(input("Introduce el mes:"))
hemis = float(input("Introduce en que Hemisferio estás, norte o sur (norte es 1 y sur 2):"))
if hemis == 1:
    match mes :
        case 1 | 2:
            print("Estás en invierno")
        case 12:
            if dia <= 20 and dia >= 1:
                print("Estás en otoño")
            elif dia >= 21 and dia <= 31:
                print("Estás en invierno")
        case 3:
            if dia <= 20 and dia >= 1:
                print("Estás en invierno")
            elif dia >= 21 and dia <= 31:
                print("Estás en primavera")
        case 4 | 5:
            print("Estás en primavera")
        case 6:
            if dia <= 20 and dia >= 1:
                print("Estás en primavera")
            elif dia >= 21 and dia <= 30:
                print("Estás en verano")
        case 7 | 8:
            print("Estás en verano")
        case 9:
            if dia <= 20 and dia >= 1:
                print("Estás en verano")
            elif dia >= 21 and dia <= 30:
                print("Estás en otoño")
        case 10 | 11:
            print("Estás en otoño")
    
elif hemis == 2:
    match mes:
        case 1 | 2:
            print("Estás en verano")
        case 12:
            if dia <= 20 and dia >= 1:
                print("Estás en primavera")
            elif dia >= 21 and dia <= 31:
                print("Estás en verano")
        case 3:
            if dia <= 20 and dia >= 1:
                print("Estás en verano")
            elif dia >= 21 and dia <= 31:
                print("Estás en otoño")
        case 4 | 5:
            print("Estás en otoño")
        case 6:
            if dia <= 20 and dia >= 1:
                print("Estás en otoño")
            elif dia >= 21 and dia <= 30:
                print("Estás en invierno")
        case 7 | 8:
            print("Estás en invierno")
        case 9:
            if dia <= 20 and dia >= 1:
                print("Estás en invierno")
            elif dia >= 21 and dia <= 30:
                print("Estás en primavera")
        case 10 | 11:
            print("Estás en primavera")
else :
        print("Los datos no son válidos")


