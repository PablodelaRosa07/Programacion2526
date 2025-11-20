def listaNum():
    lista = []
    lista3 = []
    for i in range (10):
        num = int(input("Introduce un número:"))
        lista.append(num)
    for numero in lista:
        if numero % 10 == 3:
            lista3.append(numero)
    
    return lista3

resultado = listaNum()
print(resultado)