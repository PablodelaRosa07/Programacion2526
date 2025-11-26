matriz = [[1,2,3],[4,5,6],[7,8,9]]

def devuelveDiagonalPrincipal(matriz):
    lista = []
    b = 0
    for i in range (0,len(matriz)):
        for a in range (0,len(matriz)):
            if a == b:
                lista.append(matriz[i][a])
        b = b+1

    return lista

def devuelveDiagonalSecundaria(matriz):
    listaInversa = []
    b = 2
    for i in range (0,len(matriz)):
        for a in range (0,len(matriz)):
            if a == b:
                listaInversa.append(matriz[i][a])
        b = b-1

    return listaInversa


for i in range (len(matriz)):
    assert len(matriz) == len(matriz[i])

diagonalPrincipal = devuelveDiagonalPrincipal(matriz)
diagonalSecundaria = devuelveDiagonalSecundaria(matriz)
print(diagonalPrincipal)
print(diagonalSecundaria)