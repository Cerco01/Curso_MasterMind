#Asignaciónes
euro_a_dolar = 0
dolar_a_euro = 0
euro_a_libra = 0
libra_a_euro = 0
opcion = 0


#Presentación
titulo = "BIENVENIDO AL CONVERSOR DE EUROS."
print("\n" + titulo + "\n" + "º" * len(titulo) + "\n")

#Tipo de cambio
while True:
    titulo_cambio = "¿Que intercambio de divisas quiere consultar?"
    print(titulo_cambio + "\n" + "-" * len(titulo_cambio) + "\n")
    opcion = input("A - EURO (EUR) A DOLAR (USD) \n"
                        "B - DOLAR (USD) A EURO (EUR) \n"
                        "C - EURO (EUR) A LIBRA (GBP) \n"
                        "D - LIBRA (GBP) A EURO (EUR) \n"
                        "¿A, B, C o D?:\n")

    if opcion == "A":
        primera_divisa = "EUR"
        segunda_divisa = "USD"
        break
    elif opcion == "B":
        primera_divisa = "USD"
        segunda_divisa = "EUR"
        break
    elif opcion == "C":
        primera_divisa = "EUR"
        segunda_divisa = "GBP"
        break
    elif opcion == "D":
        primera_divisa = "GBP"
        segunda_divisa = "EUR"
        break
    else:
        print("\nPor favor, escoja un intercambio de divisas.\n")

#DUDA
"""He visto que al poner un "else" para que me imprima que el usuario introduzca un valor float con la coma en caso 
de haber introducido una letra ("str") por ejemplo, en la consola directamente da un error de que no puede convertir 
un tipo "str" a "float". He visto que metiendo un:"""

# Bucle para introducir la tasa de cambio (una sola vez) y corregir el ValueError por el que se salta el else de arriba.
"""while True:
    try:
        prompt = f"Introduzca el valor de 1 {primera_divisa} en {segunda_divisa} (formato: 1.07): "
        tasa_cambio = float(input(prompt))
        break
    except ValueError:
        print("\nPor favor, introduzca un valor numérico válido. Use un punto '.' para los decimales.\n")"""


#Introducir el cambio actual
while True:

    if opcion == "A":
        euro_a_dolar = float(input("Introduzca el valor de 1 {} en {} (formato: 1.07):"
                                                                        .format(primera_divisa, segunda_divisa)))
        break
    if opcion == "B":
        dolar_a_euro = float(input("Introduzca el valor de 1 {} en {} (formato: 1.07):"
                                                                        .format(primera_divisa, segunda_divisa)))
        break
    if opcion == "C":
        euro_a_libra = float(input("Introduzca el valor de 1 {} en {} (formato: 1.07):"
                                                                        .format(primera_divisa, segunda_divisa)))
        break
    if opcion == "D":
        libra_a_euro = float(input("Introduzca el valor de 1 {} en {} (formato: 1.07):"
                                                                        .format(primera_divisa, segunda_divisa)))
        break
    else:
        print("\nPor favor, introduzca el valor correctamente. Revise que la coma flotante sea un punto"
                                                                                                "(formato: 1.07):\n")

#Cantidad de divisa
resultado_final = float(input("¿Que cantidad de {} quieres cambiar a {}?:".format(primera_divisa, segunda_divisa)))
while True:
    if opcion == "A":
        print("{} {} serían {} {}.".format(resultado_final, primera_divisa,
                                           round(resultado_final * euro_a_dolar, 2), segunda_divisa))
        break
    if opcion == "B":
        print("{} {} serían {} {}.".format(resultado_final, primera_divisa,
                                           round(resultado_final * dolar_a_euro, 2), segunda_divisa))
        break
    if opcion == "C":
        print("{} {} serían {} {}.".format(resultado_final, primera_divisa,
                                           round(resultado_final * euro_a_libra, 2), segunda_divisa))
        break
    if opcion == "D":
        print("{} {} serían {} {}.".format(resultado_final, primera_divisa,
                                           round(resultado_final * libra_a_euro, 2), segunda_divisa))
        break
    else:
        print("Por favor, introduzca un numero. \n")