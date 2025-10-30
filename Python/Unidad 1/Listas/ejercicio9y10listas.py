lista = []
for i in range (15):
    num = int(input("Introduce un número:"))
    lista.append(num)
ultimonum = num
num2 = int(input("Veces que se desplaza:"))
for i in range(1,num2+1):
    lista.insert(0,ultimonum)
    lista.pop(15)
    ultimonum = ultimonum-1
print(lista)