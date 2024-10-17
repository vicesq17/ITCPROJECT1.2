
#PROYECTO PYTHON
"""
PROYECTO PYTHON
Simulador de compras en un supermercado
El usuario pondrá los objetos que compro y el programa le dira el total de
su compra y su historial de compra.

"""


"""
================== Funciones auxiliares =================
"""

#(uso de funciones y parámetros)
def menus(opcion):
    """
    La función recibe el parámetro "opción", el cual es un integer; luego define
    con una serie de condiciones la categoría a la que corresponde el número ingresado
    y devuelve la lista de artículos correspondiente a esa categoría.
    
    """
    if opcion == 1:
        for i in menu_farmacia:
            print (i) 
    elif opcion == 2:
        for i in menu_electrodomesticos:
            print(i)
    elif opcion == 3:
        for i in menu_insumos:
            print(i)
 #(uso de estructuras de decisión y listas)   
def valor_pruducto_1(producto):
    """
    La función recibe una variable que se llama "producto",siendo un número entero y es
    usado para agregar a la variable lista de compras, la categoría correspondiente al
    número elegido y devuelve el precio del producto elegido.
    
    """
    if producto == 1:
        lista_de_compras[0].append("Medicina")
        return 570
    elif producto == 2:
        lista_de_compras[0].append("Medicina")
        return  440
    elif producto == 3:
        lista_de_compras[0].append("Medicina")
        return  735
    elif producto == 4:
        lista_de_compras[0].append("Medicina")
        return  420
    elif producto == 5:
        lista_de_compras[0].append("Medicina")
        return  377
    elif producto == 6:
        lista_de_compras[1].append("Electrodomesticos")
        return  2300
    elif producto == 7:
        lista_de_compras[1].append("Electrodomesticos")
        return  1400
    elif producto == 8:
        lista_de_compras[1].append("Electrodomesticos")
        return  3400
    elif producto == 9:
        lista_de_compras[1].append("Electrodomesticos")
        return  5700
    elif producto == 10:
        lista_de_compras[2].append("Insumos")
        return  3700
    elif producto == 11:
        lista_de_compras[2].append("Insumos")
        return  3100
    elif producto == 12:
        lista_de_compras[2].append("Insumos")
        return  5500
    elif producto == 13:
        lista_de_compras[2].append("Insumos")
        return  2500
    else:
        return 0
    
"""
================================ Programa principal =========================
Crea la lista de compras y maneja los pasos correspondientes a mostrar al usuario
las categorías y productos de su elección, posteriormente pidiendo al usuario que eliga
los productos disponibles, mandando a llamar las funciones auxiliares con los datos que
proporciona el usuario para realizar el procesamiento de datos en base a cada opción;
finalmente calcula el precio total correspondiente de los productos elegidos y finalmente
muestra al usuario ese total en conjunto con las categorías previamente seleccionadas.

"""

lista_de_compras = [[],[],[]]
menu_farmacia = ["1-Medicina $570","2-Vendaje $440","3-Vacuna $735", "4-Suero $420" , "5-Cuidado personal $377"]
menu_electrodomesticos = ["6-Microondas $2300", "7-Televisores $1400", "8-Refrigeradores $3400", "9-Computadoras $5700"]
menu_insumos = ["10-Articulos de baño $3700", "11-Articulos de Limpieza $3100", "12-Alimentos $5500", "13-Articulos de oficina $2500"]
total_compra = 0
seguir_comprando = True
print("Bienvenido, vamos a ver cuanto gastaste este mes:")
#(uso de ciclos)
while seguir_comprando:
    print("¿Qué categoría fue tu producto?")
    categorias = ["1-Farmacia", "2-Aparatos electronicos", "3-Insumos"]
    for categoria in categorias:
        print(categoria)
    opcion_del_categoria = int(input())
    while True:
        if opcion_del_categoria < 1 or opcion_del_categoria > 3:
            opcion_del_categoria=int(input("Opción invalida, intenta de nuevo: "))
        else:
            break
    print("¿Qué producto compraste?")
    menus(opcion_del_categoria)
    producto_escogido = int(input())
    valor = valor_pruducto_1(producto_escogido)
    if valor > 0:
        #(uso de operadores)
        print("Agregaste un producto con valor de $",(valor))
        print("Total acumulado: $",(total_compra))
    else:
        print("Producto no válido")
    print("¿Fue todo lo que compraste? (1-SÍ, 2-NO)")
    decision = int(input())
    
    if decision == 1:
        seguir_comprando = False
print("El total de tu gasto este mes fue de: $",(total_compra))
#(uso de ciclos anidados y listas anidadas)
for art in lista_de_compras:
    for articulos in art:
        print(articulos)
