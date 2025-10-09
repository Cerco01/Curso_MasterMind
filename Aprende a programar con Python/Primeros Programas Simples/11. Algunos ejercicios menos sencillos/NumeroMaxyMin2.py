
# Números usuario
numeros = []

# Output
numero_mas_pequenio = 0
numero_mas_grande = 0
anadir_mas = "S"

input_de_usuario = int(input("Dame un numero para tu lista."))
numeros.append(input_de_usuario)

while input("¿Quieres añadir otro? [S/N]").upper() == "S":
    input_de_usuario = int(input("Dame un numero para tu lista."))
    numeros.append(input_de_usuario)
    print(f"¡{input_de_usuario} añadido!")
    print(numeros)
    numero_mas_grande = max(numeros)
    numero_mas_pequenio = min(numeros)
    print(f"El número máximo de la lista es el: {numero_mas_grande} y el más pequeño es el: {numero_mas_pequenio}.")

    anadir_mas = input("¿Quieres añadir otro? [S/N]").upper()
    if anadir_mas == "S":
        pass
    else:
        exit()



