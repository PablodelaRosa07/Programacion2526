matriz = [8, 1, 6,3, 5, 7,4, 9, 2]

def listaPares():
    lista = []
    for i in range (0,len(matriz)):
        if matriz[i] % 2 == 0:
            lista.append(i)
        
    return lista

resultado = listaPares()
print(resultado)