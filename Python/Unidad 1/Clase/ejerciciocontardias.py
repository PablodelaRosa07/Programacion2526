dia = int(input("Introduce el día:"))
mes = int(input("Introduce el mes:"))
año = int(input("Introduce el año:"))
diaacumulados = 0
diadelmes = 0
messumado = 0
while messumado <= mes:
    diaacumulados = diaacumulados + diadelmes
    match messumado:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            diadelmes = 31
        case 2:
            diadelmes = 28
        case 4 | 6 | 9 | 11:
            diadelmes = 30
    messumado = messumado+1
print("Los días son:",diaacumulados+dia)