diassemana =["Lunes","Martes","Miércoles","Jueves","Viernes"]
findesemana =["Sábado","Domingo"]
diassemana.append("Jueves") #Agrego al final
diassemana.insert(2, "Miércoles") #Agrego en la posición 2
print(diassemana[2]) #Lectura por posición
diassemana = diassemana+findesemana #Concateno 2 listas
diassemana.pop(6) #Borrado por posición
diassemana.remove("Martes") #Borrado por valor
print(len(diassemana)) #Tamaño de la lista
if "Martes2" in diassemana:
    print("Está")
    diassemana.index #Devuelve en qué posición está
else:
    print("No está")
