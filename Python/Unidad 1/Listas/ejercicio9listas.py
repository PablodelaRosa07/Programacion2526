lista = []
for i in range (15):
    num = int(input("Introduce un número:"))
    lista.append(num)
lista.insert(0, num)
lista.pop(15)
print(lista)