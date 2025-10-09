# Output
numero_mas_pequenio = 0
numero_mas_grande = 0
anadir_mas = "S"


# Mi fórmula

"""
numeros_de_usuario = []
numeros_introducidos = input("Dame numero para tu lista separados por comas: ")
numeros_de_usuario = numeros_introducidos.split(",")
numeros_de_usuario_limpios = []

while input("¿Quieres añadir otro? [S/N]").upper() == "S":
    numeros_introducidos = int(input("Dame un numero para tu lista."))
    numeros_de_usuario.append(numeros_introducidos)
    print(f"¡{numeros_introducidos} añadido!")
    print(numeros_de_usuario)
    numero_mas_grande = max(numeros)
    numero_mas_pequenio = min(numeros)
    print(f"El número máximo de la lista es el: {numero_mas_grande} y el más pequeño es el: {numero_mas_pequenio}.")

    anadir_mas = input("¿Quieres añadir otro? [S/N]").upper()
    if anadir_mas == "S":
        pass
    else:
        exit()
"""

# La de Nate

"""
numeros_de_usuario = []
numeros_introducidos = input("Dame numero para tu lista separados por comas: ")
numeros_de_usuario = numeros_introducidos.split(",")
numeros_de_usuario_limpios = []

for numero in numeros_de_usuario:
    numeros_de_usuario_limpios.append(int(numero))

print(numeros_de_usuario_limpios)
"""

# 2a formula de Nate ## List Comprehesion

numeros_de_usuario_enteros = []

while anadir_mas == "S":

    numeros_introducidos = input("Dame numeros para tu lista separados por comas: ")
    lista_de_strings = numeros_introducidos.split(",")

    numeros_de_usuario_enteros.extend([int(n) for n in lista_de_strings])  # Esto es List Comprehesion


    print(f"¡{numeros_introducidos} añadido!")
    print(numeros_de_usuario_enteros)
    numero_mas_grande = max(numeros_de_usuario_enteros)
    numero_mas_pequenio = min(numeros_de_usuario_enteros)
    print(f"El número máximo de la lista es el: {numero_mas_grande} y el más pequeño es el: {numero_mas_pequenio}.")

    anadir_mas = input("¿Quieres añadir otro? [S/N]").upper()

exit()