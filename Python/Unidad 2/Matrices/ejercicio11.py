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


def suma(suma,lista,listaInversa):
    suma = 0
    esPrincipal = input("True para la principal y False para la secundaria:").lower()
    if esPrincipal == "true":
        for elemento in lista:
            suma = suma+elemento
    elif esPrincipal == "false":
        for elemento in listaInversa:
            suma = suma+elemento
    
    return suma

diagonalPrincipal = devuelveDiagonalPrincipal(matriz)
diagonalSecundaria = devuelveDiagonalSecundaria(matriz)
sumadeNumeros = suma(matriz,diagonalPrincipal,diagonalSecundaria)
print(diagonalPrincipal)
print(diagonalSecundaria)
print(sumadeNumeros)