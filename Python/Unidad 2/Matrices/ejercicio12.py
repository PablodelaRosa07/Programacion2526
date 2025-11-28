

def sumaDiagonal():
    matriz = []
    for i in range (0,4):
        fila = []
        for j in range (0,5):
            elemento = i+j
            fila.append(elemento)
        matriz.append(fila)

    return matriz

resultado = sumaDiagonal()
print(resultado)