def jilguero():
    meter = input("¿Deseas registrar datos de un jilguero?:").lower()
    return meter

def validar(meter):
    if meter == "si":
        matriz = []
        validacion = False
        listaNota = []
        cantidad = int(input("¿Cuántos jilgueros quieres registrar?:"))
        for i in range (cantidad):
            listaNota = []
            nota = int(input("Introduce una nota del 1 al 5:"))
            while nota > 0 and len(listaNota) < 6:
                if nota in listaNota:
                    print("Esa nota está repetida")
                else:
                    listaNota.append(nota)
                nota = int(input("Introduce una nota del 1 al 5:"))
            matriz.append(listaNota)
            if len(listaNota) == 5:
                validacion = True
    return listaNota,validacion,matriz


def calcularPunt(listaNotas,validacion,matriz):
    minimo = min(listaNotas)
    maximo = min(listaNotas)
    print(f"El máximo es:{maximo}")
    print(f"El mínimo es:{minimo}")
    puntuacionMax = 0
    for lista in matriz:
        if len(lista) > puntuacionMax:
            puntuacionMax = lista
    print(f"El ganador es:{lista}")


meterJilguero = jilguero()
puntuaciones = validar(meterJilguero)
calcularPunt(puntuaciones[0],puntuaciones[1],puntuaciones[2])
