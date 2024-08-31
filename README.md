# ITCPROJECT1.2

Proyecto de r_notesAvance 1: Selecciona un tema para tu proyeto y setup de repositorio
Describe su contexto y porque crees que es interesante. Escribe un algoritmo que describa tu proyecto.

Sube el contexto y el algoritmo al archivo readme en Github. Entrega el link de tu repositorio en canvas.(Individual)

Sigue el formato que viene en este ejemplo Proyecto Demo

Entrega: Noche de la siguiente sesión 11:30 pmprogra
Gracias.
-A01708849
Mi proyecto se basa en un sistema para clasificar distintos tipos de mercancías que acceden a aduanas mexicanas, incluyendo aranceles y pago de impuestos, esto lo considero de gran relevancia ya que se sabe que desde las nuevas políticas ha habido un rezago en cuanto al acceso de nuevos productos y de como se llegan a etiquetar en programas y si llegan o no a ser clasificados en general. 

*Solicitar al usuario del tipo de mercancia, dependiendo de su peso; si llega a exceder cierto porcentaje se lleva a etiquetado o a revisión de las autoridades, en caso de proceder se lleva a un sistema que valida si es que se debe de pagar o no impuestos por clasificación (+.16) de IVA, de igual manera se pide al usuario dentro de una base de datos ya dada (import) junto con los tipos de mercancía en la normativa; acto seguido se pide como es el etiquetado de mercancía aduanera, así como su destinatario (igualmente un sistema que verifique un sistema de datos con los continentes y el destinatario)
(Base de datos dada con una lista que te diga tipo de producto, ejemplo dispositivo electrónico, insumo de inmuebles, etc)(funciones de clasificación dadas por el usuario simulando el registro junto con pago); 
Al final se accesa a la calaoficación con una lista predeterminada de variables que te arrojan datos dependiendo de su inportancia). 
(Calculadora con 
(En conclusión se basa en una red de lista predefinida con variables que arrojan resultados dependiendo de su clasificación dada con inputs del usuario).(resultado de consulta).
peso_maximo = 5.75
peso_minimo = 0.5
limite_altura = 0.75

lista = ["electrodomesticos", "dispositivos electronicos", "dispositivos medicos"]

def clasificar_mercancia(peso, altura, tipo_mercancia):
    if peso > peso_maximo or peso < peso_minimo or altura > limite_altura:
        return "No cumple con los parámetros"
    elif tipo_mercancia in lista:
        return "Clasificable"
    else:
        return "No clasificable"

peso = float(input("Introduce el peso del objeto en kilogramos: "))
altura = float(input("Introduce la altura del objeto en metros: "))
tipo_mercancia = input("Introduce el tipo de mercancía: ").lower()

resultado = clasificar_mercancia(peso, altura, tipo_mercancia)

print(resultado)
peso_maximo = 5.75
peso_minimo = 0.5
limite_altura = 0.75

lista = ["electrodomesticos", "dispositivos electronicos", "dispositivos medicos"]

tarifa_multa = 100.00

def clasificar_mercancia(peso, altura, tipo_mercancia):
    if peso > peso_maximo or peso < peso_minimo or altura > limite_altura:
        return f"No cumple con los parámetros. Tarifa de multa: ${tarifa_multa:.2f}"
    elif tipo_mercancia in lista:
        return "Clasificable"
    else:
        return "No clasificable"

peso = float(input("Introduce el peso del objeto en kilogramos: "))
altura = float(input("Introduce la altura del objeto en metros: "))
tipo_mercancia = input("Introduce el tipo de mercancía: ").lower()

resultado = clasificar_mercancia(peso, altura, tipo_mercancia)

print(resultado)
