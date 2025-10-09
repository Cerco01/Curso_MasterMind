#Asignaciones

titulo = "Bienvenido al Test sobre queso."
puntuacion = 0
pregunta1 = "Pregunta 1: ¿Que hace cuando ve una tabla de quesos?"
pregunta2 = "Pregunta 2: ¿Como te gusta la hamburguesa?"
pregunta3 = "Pregunta 3: ¿Eres intolerante a la lactosa?"

#Código

#Título

print("\n" + titulo + "\n" + "*" * len(titulo) + "\n")

#Preguntas
while True:


    #Pregunta 1
    opcion = input(pregunta1 + "\n" + "º" * len(pregunta1) + "\n\n"
                            "A - Salgo corriendo.\n"
                            "B - Pruebo uno de los quesos o incluso varios.\n"
                            "C - No puedo evitar devorarla.\n\n\n"
                            "Responda A, B o C: ")

    if opcion == "A":
        puntuacion += 0

    elif opcion == "B":
        puntuacion += 5

    elif opcion == "C":
        puntuacion += 10

    else:
        puntuacion == "none"
        puntuacion != isinstance(puntuacion, int)
        print("\nLas respuestas disponibles son A, B y C. Si quiere una respuesta, reinicie el Quiz. ")
        break




    #Pregunta 2
    opcion = input("\n" + pregunta2 + "\n" + "º" * len(pregunta2) + "\n\n"
                            "A - Sin queso. \n"
                            "B - Con queso.\n"
                            "C - Pan y queso.\n\n\n"
                            "Responda A, B o C: ")

    if opcion == "A":
        puntuacion += 0

    elif opcion == "B":
        puntuacion += 5

    elif opcion == "C":
        puntuacion += 10


    else:
        puntuacion == "none"
        puntuacion != isinstance(puntuacion, int)
        print("\nLas respuestas disponibles son A, B y C. Si quiere una respuesta, reinicie el Quiz. ")
        break

    #Pregunta 3
    opcion = input("\n" + pregunta3 + "\n" + "º" * len(pregunta3) + "\n\n"
                            "A - Si. \n"
                            "B - A veces.\n"
                            "C - No.\n\n\n"
                            "Responda A, B o C: ")

    if opcion == "A":
        puntuacion += 0

    elif opcion == "B":
        puntuacion += 5

    elif opcion == "C":
        puntuacion += 10

    else:
        puntuacion == "none"
        puntuacion != isinstance(puntuacion, int)
        print("\nLas respuestas disponibles son A, B y C. Si quiere una respuesta, reinicie el Quiz. ")
        break

    #Resultado

    print("\nSu puntuación es de {} sobre 30. ".format(puntuacion))

    if puntuacion == 0:
            print("Cada persona tiene sus gustos. Ni opinamos ni juzgamos...")

    elif puntuacion < 15:
        print("Se podría decir que no es su comida favorita. ")

    elif puntuacion >= 30:
            print("Su gusto por el queso no tiene explicación razonable. Vaya a consultar con un experto. ")

    elif puntuacion >= 25:
            print("Le puede el ansia cuando hablamos de quesos. Jajajaja. ")

    elif puntuacion >= 15:
            print("¿A quien no le gusta el queso? ")

    break