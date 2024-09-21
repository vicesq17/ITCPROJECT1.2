def menus(opcion):
    if opcion == 1:
        menu_farmacia = ["1-Medicina $570","2-Vendaje $440","3-Vacuna $735", "4-Suero $420" , "5-Cuidado personal $377"]
        for i in menu_farmacia:
            print (i) 
    elif opcion == 2:
        menu_electrodomesticos = ["6-Microondas $2300", "7-Televisores $1400", "8-Refrigeradores $3400", "9-Computadoras $5700"]
        for i in menu_electrodomesticos:
            print(i)
    elif opcion == 3:
        menu_insumos = ["10-Articulos de baño $3700", "11-Articulos de Limpieza $3100", "12-Alimentos $5500", "13-Articulos de oficina $2500"]
        for i in menu_insumos:
            print(i)
    elif opcion > 3 or opcion < 1:
        return "Esa categoria no existe"
    
def valor_pruducto(producto): 
    if producto == 1:
        return 570
    elif producto == 2:
        return  440
    elif producto == 3:
        return  735
    elif producto == 4:
        return  420
    elif producto == 5:
        return  377
    elif producto == 6:
        return  2300
    elif producto == 7:
        return  1400
    elif producto == 8:
        return  3400
    elif producto == 9:
        return  5700
    elif producto == 10:
        return  3700
    elif producto == 11:
        return  3100
    elif producto == 12:
        return  5500
    elif producto == 13:
        return  2500
    else:
        return 0
    
total_compra = 0
seguir_comprando = True

print("Bienvenido, vamos a ver cuanto gastaste este mes:")

while seguir_comprando:
    print("¿Qué categoría fue tu producto?")
    categorias = ["1-Farmacia", "2-Aparatos electronicos", "3-Insumos"]
    for categoria in categorias:
        print(categoria)

    opcion_del_menu = int(input())
    print("¿Qué producto compraste?")
    menus(opcion_del_menu)

    producto_escogido = int(input())
    valor = valor_pruducto(producto_escogido)

    if valor > 0:
        total_compra = total_compra + valor
        print("Agregaste un producto con valor de $",(valor))
        print("Total acumulado: $",(total_compra))
    else:
        print("Producto no válido")

    print("¿Fue todo lo que compraste? (1-SÍ, 2-NO)")
    decision = int(input())
    
    if decision == 1:
        seguir_comprando = False

print("El total de tu gasto este mes fue de: $",(total_compra))

