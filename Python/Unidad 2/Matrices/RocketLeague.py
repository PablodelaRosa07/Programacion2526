def opciones():
    print("R. Registrar puntuaciones de equipo")
    print("L. Listar equipos y su puntuación por fase")
    print("C. Clasificados por fase")
    print("S. Salir")
    opcion = input("¿Qué desea hacer?:").upper()
    while opcion != "R" and opcion != "L" and opcion != "C" and opcion != "S":
        print("Opción incorrecta")
        opcion = input("¿Qué desea hacer?:").upper()

    return opcion

def opcionElegir(opcion):
    listaNombre = []
    listaPuntuacion = []
    if opcion == "R":
        fase = input("¿En qué fase quieres meter la puntuación?:").lower()
        while fase != "final" and fase != "semifinal" and fase != "inicial":
            fase = input("¿En qué fase quieres meter la puntuación?:").lower()
        if fase == "inicial":
            for i in range (0,8):
                nombreEquipo = input("Introduce nombre del equipo:")
                puntuacionEquipo = int(input("Introduce su puntuación:"))
                listaNombre.append(nombreEquipo)
                listaPuntuacion.append(puntuacionEquipo)
        elif fase == "semifinal":
            for i in range (0,4):
                nombreEquipo = input("Introduce nombre del equipo:")
                puntuacionEquipo = int(input("Introduce su puntuación:"))
                listaNombre.append(nombreEquipo)
                listaPuntuacion.append(puntuacionEquipo)
        elif fase == "final":
            for i in range (0,2):
                nombreEquipo = input("Introduce nombre del equipo:")
                puntuacionEquipo = int(input("Introduce su puntuación:"))
                listaNombre.append(nombreEquipo)
                listaPuntuacion.append(puntuacionEquipo)
        print("========================")
        print("Registrado corractamente")
        print("========================")

    elif opcion == "L":
        for i in range (0,len(listaNombre)):
            print(f"El equipo {listaNombre[i]} ha obtenido {listaPuntuacion[i]}")

    elif opcion == "C":
        print("")
    
    return opcion
    


resultado = opciones()
resultado2 = opcionElegir(resultado)