lista_de_la_compra = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
vocales = ["a", "e", "i", "o", "u"]
frase = "Hola que tal estas?"
vocales_encontradas = 0

for item in lista_de_la_compra:
    print(item)

for letra in frase:
    if letra in vocales:
        print(f"He encontrado la vocal: {letra}")
        vocales_encontradas += 1

print(f"Vocales encontradas: {vocales_encontradas}")