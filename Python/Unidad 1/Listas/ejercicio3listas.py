import random
diassemana =["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

lista_multiplo3=[]
for i in range(3,31,3):
    print(i)
    lista_multiplo3.append(i)
    lista_multiplo3.insert(8)
    if lista_multiplo3 == 8:
        print("8")
print(lista_multiplo3)
