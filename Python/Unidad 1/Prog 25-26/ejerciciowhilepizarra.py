n = 15
resultado = 0
for i in range(n + 1):
    if i % 2 == 0:
        resultado = resultado +2 * i
    else :
        resultado = resultado +2 * i +1
print("El resultado es:",resultado)
