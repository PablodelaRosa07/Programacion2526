historial = float(input("Introduce tu historial crediticio:"))
trabajo = float(input("Introduce el tiempo en años que lleva trabajando:"))
sueldo = float(input("Introduce su salario:"))
prestamo = float(input("Introduce la cantidad que quiere solicitar:"))
if historial < 0 or trabajo < 2 or sueldo*0.01<prestamo :
    print("No es apto para el préstamo")
else :
    print("Es apto para el préstamo")
