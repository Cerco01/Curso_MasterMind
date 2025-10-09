
respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta != "C":
    respuesta = input("¿A, B o C?:")

    #Dentro de while puedo meter todos los espacios y código que seguirá dentro del bucle.
    print("Comprobando respuesta.")



if respuesta == "A":
    print("Has elegido bien.")
elif respuesta == "B":
    print("Podrías haber elegido mejor.")
elif respuesta == "C":
    print("Elegiste mal.")
else:
    print("No me has dado una respuesta con sentido.")