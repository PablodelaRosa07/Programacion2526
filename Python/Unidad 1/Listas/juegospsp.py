print("R. Registrar juegos")
print("E. Mostrar estadísticas")
print("S. Salir del programa")
nombre = []
puntuacion=[]
genero=[]
numjuegos = 0
opcion = input("¿Qué desea hacer?:")
while opcion == "r" or opcion == "e":
    if opcion == "r":
        print("Registrando...")
        nom= (input("Introduce el nombre del juego:"))
        punt= int(input("Introduce tu puntuación (1-10):"))
        gen= input("Introduce el género del juego:")
        nombre.append[nom]
        puntuacion.append[punt]
        genero.append[gen]
        numjuegos = numjuegos+1
    if opcion == "e":
        for i in range (numjuegos):
            print("Mostrando tu colleción de juegos:")
            print(nombre[i],"| Puntuación:",puntuacion[i],"| Género:",genero[i])
while opcion != "r" and opcion != "e" and opcion != "s":
    opcion = input("¿Qué desea hacer?:")
print("Saliendo del programa")