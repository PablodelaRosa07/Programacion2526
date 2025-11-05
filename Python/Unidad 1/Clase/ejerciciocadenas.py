numero= "1234567"
salida= ""
contador= 0
for i in range (len(numero),0,-3):
    salida= ""+numero[i:i+3]
    contador = contador+3
    print(salida)