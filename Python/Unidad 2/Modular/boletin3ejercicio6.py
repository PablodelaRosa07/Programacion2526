def estaOrdenadaAscendemente():
    listaNum=[]
    ordenada = True
    meterNum = int(input("Introduce un número:"))
    while meterNum == int:
        listaNum.append(meterNum)
        meterNum = int(input("Introduce un número:"))
    i = 0
    while i < len(listaNum)-1 and ordenada:
            if listaNum[i] > listaNum[i+1]:
                ordenada = False
            i = i+1
    print(ordenada)
    return listaNum

resultado=estaOrdenadaAscendemente()
