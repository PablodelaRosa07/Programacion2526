lista = []
for i in range (15):
    num = int(input("Introduce un número:"))
    lista.append(num)
num2 = int(input("Veces que se desplaza:"))
if num2 < len(lista):
    for i in range(num2):
        lista.insert(0, 15)
        lista.pop(15)
print(lista)