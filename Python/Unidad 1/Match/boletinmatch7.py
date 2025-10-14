operacion = input("Desea sumar, restar, multiplicar o dividir?:")
x = int(input("Introduce un número:"))
y = float(input("Introduce otro número:"))
resultado = 0
match operacion:
    case "sumar":
        resultado = x+y
        print(x,"+",y,"=",resultado)
    case "restar":
        resultado = x-y
        print(x,"-",y,"=",resultado)
    case "multiplicar":
        resultado = x*y
        print(x,"*",y,"=",resultado)
    case "dividir":
        resultado =x/y
        print(x,"/",y,"=",resultado)