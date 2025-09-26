cuenta = float(input("Introduce la cantidad existente en tu cuenta:"))
num1 = float(input("Introduce la cantidad que desee retirar:"))
if num1 > cuenta :
    print("No es posible hacer la operación")
else: 
    print("Se ha retirado", num1, "de la cuenta")
    print("Queda", cuenta-num1, "en la cuenta")
