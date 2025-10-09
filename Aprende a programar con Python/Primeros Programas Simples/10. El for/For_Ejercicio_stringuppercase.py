# Ejemplo: texto_usuario = "Hola, me llamo Nate. ¿Tu como te llamas?"
import string

# Output esperado:
mayuscula = 0


texto_usuario = input("Dame una frase y te cuento las mayúsculas que contenga:\n")
for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        mayuscula += 1


print("Número de mayúsculas: ", mayuscula)