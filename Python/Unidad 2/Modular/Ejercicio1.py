num= input("Introduce una cadena de más de 4 caracteres:")
lista= list(num)
salida=""
while len(lista) <=3:
    num= input("Introduce una cadena de más de 4 caracteres:")
    lista= list(num)
numint=int(num)
if numint % 2 == 0:
    salida= num[2]+num[4]
    print(salida)
if numint % 3 == 0:
    salida= num[1]+num[2]
    print(salida)
if numint % 7 == 0:
    salida= num[0]+num[3]
    print(salida)