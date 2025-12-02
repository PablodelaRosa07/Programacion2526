ventas = [
    ["Portátil", 150, 799.99, 4.5],
    ["Smartphone", 250, 599.99, 4.3],
    ["Auriculares", 400, 49.99, 4.0],
    ["Tablet", 120, 299.99, 3.9],
    ["Monitor", 180, 199.99, 4.2],
    ["Smartwatch", 220, 149.99, 4.1],
    ["Teclado mecánico", 300, 89.99, 4.4],
    ["Ratón gaming", 350, 59.99, 4.0],
    ["Cámara digital", 90, 999.99, 4.6],
    ["Consola", 200, 399.99, 4.7],
    ]

def getProducto(ventas):
    detalle=input("Introduce el nombre del producto para buscarlo:").capitalize()
    posicion = 0
    encontrado = []
    while posicion < len(ventas) and not encontrado:
        if ventas[posicion][0] == detalle:
            encontrado = ventas[posicion]
        posicion = posicion+1

    return encontrado

def calcularIngresos(encontrado):
    ingreso = 0
    ingreso = encontrado[1]*encontrado[2]
    
    return ingreso

def productoDestacado(ventas):
    listaDestacados = []
    for elemento in ventas:
        if elemento[3] >= 4.2:
            listaDestacados.append(elemento[0])
            
    return listaDestacados

def tieneMayorIngreso(encontrado):
    for i in range(0,2):
        llamada = calcularIngresos()
    assert encontrado[0] > encontrado[1]


resultadoProducto = getProducto(ventas)
print(resultadoProducto)

resultadoIngresos = calcularIngresos(resultadoProducto)
print(f"Ingresos del producto: {resultadoIngresos}")

resultadoDestacado = productoDestacado(ventas)
print(f"Productos destacados: {resultadoDestacado}")