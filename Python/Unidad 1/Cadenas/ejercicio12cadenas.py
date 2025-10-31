num = input("Introduce un número:")
salida = ""
num = list(num)
a = 0
for i in range (0,len(num)+1,len(num)):
    num.pop(a)
    a = -1
for valor in num:
    salida = salida+valor
print(salida)