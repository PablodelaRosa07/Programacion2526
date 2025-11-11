print("A. Introducir árboles")
print("B. Resumen de datos guardados")
print("F. Mostrar datos árbol más alto")
print("E. Salir del programa")
opcion= input("¿Qué desea hacer?:").upper()
arbolesNombre=[]
arbolesTipo=[]
arbolesDiam=[]
arbolesAlt=[]
arbolesEdad=[]
a=0
alturaMax=[]
alturaMin=[]
edadMedia=0
numArboles30=0
while opcion != "E":
    if opcion == "A":
        numArboles = int(input("Introduce la cantidad de árboles que quieres introducir:"))
        for i in range (numArboles+1):
            nombrearbol=int(input("Árbol número:"))
            arbolesNombre.append(nombrearbol)
            tipoArbol= input("¿El árbol es tipo A o tipo B?:").upper()
            arbolesTipo.append(tipoArbol)
            diamArbol= int(input("Introduce el diámetro del árbol en metros:"))
            arbolesDiam.append(arbolesTipo)
            altArbol = int(input("Introduce la altura del árbol en metros:"))
            alturaMax.insert(0, altArbol)
            arbolesAlt.append(altArbol)
            if alturaMax < arbolesAlt[0]:
                alturaMax.insert(0, altArbol)
                alturaMax.pop(-1)
            arbolesAlt.append(altArbol)
            if arbolesAlt >= 30:
                numArboles30=numArboles30+1
            if tipoArbol == "B":
                edadArbol= int(input("Introduce la edad del árbol:"))
                edadMedia.append(edadArbol)
        for i in range (0,len(arbolesEdad)+1):
            edadMedia = edadMedia+arbolesEdad[i]
        edadMedia = edadMedia/len(arbolesEdad)
        print("Mostrando tu colleción de árboles:")
        for i in range (0,numArboles+1):
            if arbolesTipo[i] == "A":
                print(arbolesNombre[i],"| Tipo A:",arbolesTipo[i],"| Diámetro:",arbolesDiam[i],"| Altura:",arbolesAlt[i])
            if arbolesTipo[i] == "B":
                print(arbolesNombre[i],"| Tipo A:",arbolesTipo[i],"| Diámetro:",arbolesDiam[i],"| Altura:",arbolesAlt[i],"| Edad",arbolesEdad[a])
                a=a+1
        print("A. Introducir árboles")
        print("B. Estadísticas principales")
        print("E. Salir del programa")
        opcion= input("¿Qué desea hacer?:").upper()
    if opcion == "B":
        print("La altura máxima es:")
        print("La altura mínima es:")
        print("La media de edad para los árboles de tipo B es",edadMedia,"años")
        print("Existen",numArboles30,"árboles en total de más de 30m")
    if opcion == "F":
        a=0
        for i in arbolesAlt:
            if i == alturaMax:
                print(arbolesNombre[a],"| Tipo A:",arbolesTipo[a],"| Diámetro:",arbolesDiam[a],"| Altura:",arbolesAlt[a])
            a = a+1
    opcion= input("¿Qué desea hacer?:").upper()
    

    


    
        