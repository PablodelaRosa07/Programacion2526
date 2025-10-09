numero = int(input("Dame un número:"))
div= 1
while numero != 0:
    div = div*10
    numero = numero //div
    resultadoResto = numero % div
    print(resultadoResto)