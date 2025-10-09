"""
# Numero elegido por el usuario: 2,
output esperado:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
"""

lista_multiplos = []
numero_a_multiplicar = int(input("Que tabla de multiplicar quieres que te muestre? >"))
print(f"La tabla del {numero_a_multiplicar}:")
for i in range(1, 11):
    if i % 2 == 0:
        solucion = numero_a_multiplicar * i
        print(f"{numero_a_multiplicar} * {i} = {solucion}")

        """multiplos = solucion % 2
        if multiplos == 0:
            lista_multiplos.append(solucion)

    print(f"Los múltiplos de 2 en esta tabla son: {lista_multiplos}")"""