def redondear():
    numero = float((input("Introduce un número:")))
    numeroRedondeado = round(numero, 2)

    return numeroRedondeado

resultado = redondear()
print(resultado)