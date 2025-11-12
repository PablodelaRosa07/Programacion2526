print("Pulse T para generar un nuevo tablero")
print("Pulse J para jugar")
print("Pulse E para salir del juego")
opcion = input("¿Qué desea hacer?:").upper()
while opcion != "T" and opcion != "J" and opcion != "E":
    print("La opción es incorrecta")
    print("Pulse T para generar un nuevo tablero")
    print("Pulse J para jugar")
    print("Pulse E para salir del juego")
    opcion = input("¿Qué desea hacer?:").upper()

import random
listaTablero = []
listaMinas = []
numMinas=0
puntos = 0
MinasRestantes = numMinas
MinasEncontradas = 0
while opcion == "T" or opcion == "J":
    if opcion == "T":
        print("Generando tablero")
        for i in range(8):
            num = random.randint(0,1)
            if num == 0:
                listaTablero.append("")
            elif num == 1:
                listaTablero.append("X")
                numMinas=numMinas+1
        print(f"¡Tablero generado! Se han escondido {numMinas} minas. Tablero:{listaTablero}")
        MinasRestantes = numMinas
    elif opcion == "J":
        while len(listaTablero) <= 7:
            print("Debes generar el tablero antes.")
        print("Jugando")
        print(f"Tienes que encontrar {numMinas} minas")
        while MinasEncontradas < numMinas:
            posicion = int(input("Introduce una posición de la lista, (0-7):"))
            while posicion in listaMinas:
                posicion = int(input("Ya habías encontrado esta mian. Introduce una posición de la lista, (0-7):"))
            listaMinas.append(posicion)       
            while posicion >= 8:
                posicion = int(input("Error en la posición. Introduce una posición de la lista, (0-7):"))
            if listaTablero[posicion] == "X":
                puntos = puntos+1
                MinasRestantes = MinasRestantes-1
                MinasEncontradas = MinasEncontradas+1
                print(f"¡MINA! +1 punto. [Puntuación: {puntos} | Minas Restantes: {MinasRestantes}]")
            elif listaTablero[posicion] == "":
                puntos = puntos-1
                print(f"¡AGUA! +1 punto. [Puntuación: {puntos} | Minas Restantes: {MinasRestantes}]")
        print(f"Has encontrado todas las minas. La puntuación final es {puntos} puntos")
        print("---FIN DEL JUEGO---")
    print("Pulse T para generar un nuevo tablero")
    print("Pulse J para jugar")
    print("Pulse E para salir del juego")
    opcion = input("¿Qué desea hacer?:").upper()

print("Saliendo")

