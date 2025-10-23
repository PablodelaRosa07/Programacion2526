meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
temp = []
for i in range(12):
    media = int(input("Dime la temperatura media del mes:"))
    temp.append(media)
print(temp)
for i in range (0,12):
    print(meses[i],temp[i]*"*","(",temp[i],"ºC)")