# Ejemplo: texto_usuario = "Hola, me llamo Nate. ¿Tu como te llamas?"

# Output esperado:

espacios = 0
puntos = 0
comas = 0

texto_usuario = input("Dame una frase y te cuento los espacios, puntos y comas que contenga:\n")
for letras in texto_usuario:
    if letras == " ":
        espacios += 1
    elif letras == ".":
        puntos += 1
    elif letras == ",":
        comas += 1

print(f"Espacios: {espacios}")
print(f"Puntos: {puntos}")
print(f"Comas: {comas}")