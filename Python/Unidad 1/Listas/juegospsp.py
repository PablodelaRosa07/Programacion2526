print("R. Registrar juegos")
print("E. Mostrar estadísticas")
print("P. Juego con mayor puntuación")
print("D. Detalles del juego")
print("G. Búsqueda por géneros")
print("S. Salir del programa")
nombre = []
puntuacion=[]
genero=[]
numjuegos = 0
opcion=""
while opcion != "S":
    opcion = input("¿Qué desea hacer?:").upper()
    match opcion:
        case "R":
            print("Registrando...")
            veces=int(input("¿Cuántos juegos quieres añadir?:"))
            for i in range (0,veces):
                nom= (input("Introduce el nombre del juego:"))
                nombre.append(nom)
                punt= int(input("Introduce tu puntuación (1-10):"))
                puntuacion.append(punt)
                gen= input("Introduce el género del juego:")
                genero.append(gen)
                numjuegos = numjuegos+1
        case "E":
            print("Mostrando tu colleción de juegos:")
            for i in range (numjuegos):
                print(nombre[i],"| Puntuación:",puntuacion[i],"| Género:",genero[i])
        case "P":
            max=puntuacion[0]
            for i in puntuacion:
                if i > max:
                    max = i
            posicion=puntuacion.index(max)
            print(nombre[posicion],"| Puntuación:",puntuacion[posicion],"| Género:",genero[posicion])
        case "D":
            detalle=input("Introduce el nombre del juego para buscarlo:")
            if detalle in nombre:
                posicion=nombre.index(detalle)
                print(nombre[posicion],"| Puntuación:",puntuacion[posicion],"| Género:",genero[posicion])
            else:
                print("Ese juego no está en la lista")
        case "G":
            buscargenero=input("Introduce el género del juego:")
            for buscargenero in genero:
                if (genero==buscargenero) in nombre:
                    generojuego=genero.index(buscargenero)
                    print(nombre[generojuego],"| Puntuación:",puntuacion[generojuego],"| Género:",genero[generojuego])
                else:
                    print("Ese género no está en la lista")
        case "S":
            print("Saliendo del programa")