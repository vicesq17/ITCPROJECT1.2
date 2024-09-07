# Definir las variables
peso_maximo = 5.75
peso_minimo = 0.5
limite_altura = 0.75
lista = [
    "electrodomesticos", "dispositivos electronicos", "dispositivos medicos"
]
tarifa_multa = 100.00


# Definir la función
def clasificar_mercancia(peso, altura, tipo_mercancia):
    while True:
        if peso > peso_maximo or peso < peso_minimo or altura > limite_altura:
            return f"No cumple con los parámetros. Tarifa de multa: ${tarifa_multa:.2f}"
        elif tipo_mercancia in lista:
            return "Clasificable"
            break
        else:
            return "No clasificable"

while True:
    # Solicitar
    peso = float(input("Introduce el peso del objeto en kilogramos: "))
    altura = float(input("Introduce la altura del objeto en metros: "))
    tipo_mercancia = input("Introduce el tipo de mercancía: ").lower()

    # Mostrar
    resultado = clasificar_mercancia(peso, altura, tipo_mercancia)
    print(resultado)
    continuar=input("¿Deseas continuar?"(s/n)).lower()
    if continuar != "s":
        break