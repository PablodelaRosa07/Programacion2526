matriz = []

def lista():
    for i in range (3):
        lista = []
        for i in range(3):
            numeroMeter = int(input("Introduce un número:"))
            lista.append(numeroMeter)
        matriz.append(lista)
    return matriz

def columna(matriz):
    columnas = int(input("¿Qué columna quieres sumar?(0,1,2):"))
    while columnas > 2:
        columnas = int(input("¿Qué columna quieres sumar?(0,1,2):"))
    suma = 0
    for elemento in matriz:
        suma = suma + elemento[columnas]
    return suma

listas = lista()
suma = columna(listas)
print(f"La suma de las columnas es: {suma}")
