listaProductos = []
listaPrecios = []

#listaProductos
def listaProducto():
    dinero = 0
    total = 0
    dineroMax = float(int(input("Introduce el dinero máximo en € que quieres gastar en la compra:")))
    while dinero < dineroMax:
        productos = input("Introduce el nombre del producto:").lower()
        precios = float(int(input("Introduce el precio del producto:")))
        dinero = dinero+precios
        if dinero < dineroMax:
            listaProductos.append(productos)
            listaPrecios.append(precios)
    for i in range (0, len(listaPrecios)):
        total = total+listaPrecios[i]
    return total,dineroMax,listaProductos,listaPrecios

#menu
def menu(resultado,productos,precios,totalcuenta):
    print(f"Importe máximo a gastar: {resultado}")
    print(f"Productos: {productos}")
    print(f"Precios: {precios}")
    print(f"El coste total es de {totalcuenta}€")

    print("Pulse S para calcular dinero restante.")
    print("Pulse R para eliminar un producto y su precio de la lista.")
    print("Pulse C para devolver la lista de productos cuyo precio es más alto que un importe.")
    return resultado,totalcuenta

#opciones
def opciones(dineroMaximo,totalCuenta):
    opcion = input("¿Qué desea hacer?:").upper()
    while opcion == "S" or opcion == "R" or opcion == "C":
        if opcion == "S":
            print(f"Dinero sobrante: {dineroMaximo-totalCuenta}")

        elif opcion == "R":
            a = 0
            producto = input("Introduce el nombre del producto:").lower()
            print(listaProductos, listaPrecios)
            seguro = input(f"Se va a eliminar {producto} de la lista. ¿Estás seguro? (S/N):").upper()
            if seguro == "S":
                for i in listaProductos:
                    if i == producto:
                        listaProductos.remove[a]
                    a = a+1
            elif seguro == "N":
                print("No se ha eliminado.")
            print(listaProductos, listaPrecios)

        elif opcion == "C":
            a = 0
            listaMayor = []
            importe = float(int(input("Introduce un importe:")))
            for precio in listaPrecios:
                if precio > importe:
                    listaMayor.append(listaProductos[a])
                a = a+1
            print(f"La lista de precios con precio mayor al importe: {listaMayor}")
        opcion = input("¿Qué desea hacer?:").upper()
    print("Saliendo del programa")
    return opcion,

resultado=listaProducto()
preciosMenu=menu()
menu(resultado[1],resultado[2],resultado[3],resultado[0])

opcionesDinero=opciones()
opciones(preciosMenu[0],preciosMenu[1])
