
    
    return gasto



def menu_electrodomesticos():
    print("1. Televisor $800")
    print("2. Refrigerador $1500")
    print("3. Lavadora $1200")
    print("4. Horno $600")
    print("5. Aspiradora $300")

def prod_electrodomesticos(producto, gasto):
    if producto == 1:
        gasto += 800
    elif producto == 2:
        gasto += 1500
    elif producto == 3:
        gasto += 1200
    elif producto == 4:
        gasto += 600
    elif producto == 5:
        gasto += 300
    
    return gasto
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def main():
    continuar = True
    gasto = 0
    while continuar == True:
        print("1. Añadir producto")
        print("2. Salir")
        seleccion = int(input("¿Qué deseas hacer? : "))
        
        if seleccion == 1:
            menu_categorias()
            selec_categ = int(input("¿De qué categoría es tu producto? : "))
            if selec_categ == 1:
                menu_farmacia()
                select_farm = int(input("¿Qué producto compraste? : "))
                
                res = prod_farm(select_farm)
                print (res)
            
        
        elif seleccion == 2:
            
            
            continua = False

                
            
    
main()
