numero = input("Dime un número:")
listadigitos = []
numveces = 0
for i in range(len(numero)-1,-1,-1):
    listadigitos.append(numero[i])
    numveces = numveces+1
print(numveces)