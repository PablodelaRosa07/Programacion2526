import random
matriz = []

def getListaSinColumna(matriz):
    columna = int(input("¿Qué columna quieres recibir?(0-4):"))
    lista = []
    for i in range(0,5):
        lista.append(matriz[i][0])

    return lista

def generaCarton(matriz):
    a = 1
    b = 15
    for i in range (0,5):
        lista = []
        while len(lista) < 5:
            if i == 2 and len(lista) == 2:
                lista.append("--")
            else:
                num = random.randint(a,b)
                if num not in lista:
                    lista.append(num)
        matriz.append(lista)
        a = a+15
        b = b+15
    
    return matriz




resultado = generaCarton(matriz)
devuelveColumna = getListaSinColumna(matriz)
print(devuelveColumna)

for i in range(0,5):
    assert len(matriz) == 5
    assert len(matriz[i]) == 5
assert matriz[2][2] == "--"