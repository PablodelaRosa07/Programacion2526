numeros = []
for i in range(10):
    num = float(input("Introduce el número: "))
    numeros.append(num)

maximo = max(numeros)
minimo = min(numeros)

print("Números introducidos:")
for num in numeros:
    if num == maximo:
        print(num, "(máximo)")
    elif num == minimo:
        print(num ,"(mínimo)")
    else:
        print(num)