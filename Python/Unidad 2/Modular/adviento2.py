matriz =   [['A', 'B', 'C', 'D'],    
    ['E', 'F', 'G', 'H'],    
    ['I', 'J', 'K', 'L'],    
    ['M', 'N', 'Ñ', 'O'],    
    ['P', 'Q', 'R', 'S'],    
    ['T', 'U', 'V', 'W'],    
    ['X', 'Y', 'Z', '_']]

numDescifrar = "21,34,74,21,71,31,61,44,74,34,34,21,23,11,74,13,44,42,74,61,53,11,12,11,32,44,74,72,74,51,21,53,54,31,54,61,21,42,13,31,11"
cadena = "NO_SOLO_HAY_QUE_CONFIAR_EN_EL_PROCESO_HAY_QUE_SEGUIRLO"


def descifrar(matriz,numDescifrar):
    listaPalabras = []
    listaCifrada = numDescifrar.split(",")

    for par in listaCifrada:
        fila = int(par[0])-1
        columna = int(par[1])-1
        listaPalabras.append(matriz[fila][columna])

    return listaPalabras

def cifrar(matriz,cadena):
    listaNumeros = []
    listaCifrada = numDescifrar.split("")
    fila = 0
    for i in range (0,len(matriz)):
        if listaCifrada[i] in matriz[i]:
            fila = i
            for i in range(0,len(matriz[i])):
                if i == listaCifrada[i]:
                    columna = i
        listaNumeros.append(f"{fila}{columna},")
    return listaNumeros

resultado = descifrar(matriz,numDescifrar)
resultado2 = cifrar(matriz,cadena)
print(resultado)
print(resultado2)