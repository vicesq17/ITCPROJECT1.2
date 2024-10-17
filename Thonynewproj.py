"""
PROYECTO PYTHON
Simulador de compras en un supermercado
El usuario pondrá los objetos que compro y el programa le dira el total de
su compra y su historial de compra

"""

"""
=================== Listas ===================================

"""

# Lista de productos
productos = [
    [1, "Medicina", 570, "Farmacia"],
    [2, "Vendaje", 440, "Farmacia"],
    [3, "Vacuna", 735, "Farmacia"],
    [4, "Suero", 420, "Farmacia"],
    [5, "Cuidado personal", 377, "Farmacia"],
    [6, "Microondas", 2300, "Electrodomésticos"],
    [7, "Televisores", 1400, "Electrodomésticos"],
    [8, "Refrigeradores", 3400, "Electrodomésticos"],
    [9, "Computadoras", 5700, "Electrodomésticos"],
    [10, "Artículos de baño", 3700, "Insumos"],
    [11, "Artículos de limpieza", 3100, "Insumos"],
    [12, "Alimentos", 5500, "Insumos"],
    [13, "Artículos de oficina", 2500, "Insumos"]
]

# Lista de compras
lista_de_compras = {"Farmacia": [], "Electrodomésticos": [], "Insumos": []}

"""

====================== Funciones de apoyo ========================

"""

def mostrar_menu(categoria):
    
    """
        (uso de ciclos for, condicionales, listas)
        Recibe: La categoría escogida (string)por el usuario del producto 
        que compro
        Imprime la lista de productos por categoría y crea una lista con los 
        numeros de los productos que pertenecen a dicha categoria
        Devuelve: Lista con los números por categoría
    """
    
    print("\nProductos en", categoria, ":")
    productos_categoria = []
    for prod in productos:
        if prod[3] == categoria:
            print(prod[0], "-", prod[1], ": $", prod[2])
            productos_categoria.append(prod[0])  # Almacenar los ids(números)
    return productos_categoria

# Función para obtener el valor del producto
def obtener_valor_producto(producto_id):
    
    """
        (uso de condicionales y listas)
        Recibe: Número correspondiente al producto en la lista principal
        Compara el número o ID del producto en la lista, si lo encuentra, 
        devuelve su precio, si no, devuelve un 0
        devuelve: Precio del producto de la lista
    """
    
    for prod in productos:
        if prod[0] == producto_id:
            lista_de_compras[prod[3]].append(prod[1])  # Agregar el producto 
            return prod[2]  # Devolver el valor del producto
    return 0  # Si no se encuentra, devolver 0

# Función para validar entrada
def validar_entrada(mensaje, opciones):
    
    """
        (uso de ciclos, operadores y variables)
        Recibe: El mensaje para saber que numero debe introducir el usuario y 
        la lista de numeros validos para poner en esa entrada
        Valida que los numeros introducidos por el usuario correspondan
        a dicha entrada y no se conbinen los productos con las categorias
        Devuelve: El valor numérico que introdujo el usuario
    """
   
    entrada = input(mensaje)  # Solicitar entrada
    while not (entrada.isnumeric() and int(entrada) in opciones):  
        print("Inválido. Escoge entre", min(opciones),"y", max(opciones), ".")
        entrada = input(mensaje)  # Pedir nueva entrada si no es válida
    return int(entrada)

"""

======================== Funciones principales =========================

"""

# Función que contiene el ciclo de compras
def realizar_compras():
    
    """
        (uso de ciclos y condicionales anidados)
        Recibe: No recibe parámetros
        La función inicia el ciclo de compras del usuario, este irá poniendo
        los valores que se adecúen a sus compras, dependiendo de la categoría
        y el producto. De igual forma, cabe mencionar que aquí se hacen las 
        llamadas a las funciones anteriores
        Devuelve: El total de compra del usuario
    """

    total_compra = 0
    seguir_comprando = True

    while seguir_comprando:
        print("\nCategorías:\n1 -Farmacia\n2 -Electrodomésticos\n3 - Insumos")
        opcion_categoria = validar_entrada("Elige entre (1-3): ", range(1, 4))

        if opcion_categoria == 1:
            productos_validos = mostrar_menu("Farmacia")
        elif opcion_categoria == 2:
            productos_validos = mostrar_menu("Electrodomésticos")
        elif opcion_categoria == 3:
            productos_validos = mostrar_menu("Insumos")

        # Selección del producto y cálculo del total
        escogido = validar_entrada("Producto comprado: ", productos_validos)
        valor = obtener_valor_producto(escogido)

        if valor > 0:
            total_compra += valor
            print("Agregaste un producto de $", valor)
            print("Total acumulado: $", total_compra)
        else:
            print("Producto no válido.")

        # Preguntar si quiere seguir comprando
        decision = validar_entrada("¿Seguir comprando? (1-SI,2-NO): ", [1, 2])
        if decision == 2:
            seguir_comprando = False

    return total_compra

def programa_principal():
    
    """
        (uso de ciclos for)
        Recibe: No recibe parámetros
        Aquí se ejecuta el programa principal, se manda a llamar a la función 
        anterior para que este haga los llamados pertinenetes para obtener
        todos los resultados
        No tiene regresos
    """
    
    print("Bienvenido, vamos a ver cuánto gastaste este mes:")
    total = realizar_compras()

    # Mostrar el resumen de la compra
    print("\nEl total de tu gasto este mes fue: $", total)
    print("Resumen de tu compra:")
    for categoria, items in lista_de_compras.items():
        if items:
            print(categoria, ":", ", ".join(items))

# Ejecutar el programa principal
programa_principal()
