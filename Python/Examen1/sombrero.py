import random
print("=======================")
print("SOMBRERO SELLECCIONADOR")
print("=======================")
print("1. Seleccionar casa para alumno")
print("2. Mostrar estadísticas")
print("Elige una opción. Si quieres salir del programa, escribe (1) y el nombre del personaje innombrable")
nombre = ""
totalalumnos = 0
casa1 = 0
casa2 = 0
casa3 = 0
casa4 = 0
opcion1 = int(input("Elige una opción, (1 o 2):"))
while nombre!="voldemort":
    if opcion1 == 1:
        print("Ejecutando y seleccionando casa") 
    elif opcion1 == 2:
        print("Ejecutando y mostrar estadísticas")
        print("Total de alumnos:",totalalumnos)
        print("Gryffindor",casa1)
        print("Slytherin",casa2)
        print("Hufflepuff",casa3)
        print("Ravenclaw",casa4) 
    num = random.randint(1,4)
    nombre = input("Introduce tu nombre:")
    if nombre != "voldemort":
        if num == 1:
            casa = "Gryffindor"
            casa1 = casa1+1
        elif num == 2:
            casa = "Slytherin"
            casa2 = casa2+1
        elif num == 3:
            casa = "Hufflepuff"
            casa3 = casa3+1
        elif num == 4:
            casa = "Ravenclaw"
            casa4 = casa4+1
        print("El Sombrero dice que",nombre,"pertenece a",casa)
        totalalumnos = totalalumnos+1
        opcion1 = int(input("Elige una opción, (1 o 2):"))
print("Apparition, transpórtame a otro sitio")












