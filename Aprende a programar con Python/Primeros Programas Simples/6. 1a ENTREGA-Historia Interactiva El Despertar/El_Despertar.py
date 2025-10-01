import random

titulo = "El Empleado de Oficina y el Café Mágico."
print("\n" + titulo + "\n" + "º" * len(titulo))
print("Una historia de Gemini. :'O\n\n")


#1. El Despertar y la Búsqueda del Café
print("Te despiertas en tu escritorio, babeando sobre el teclado. El reloj marca las 9:07 AM.")
nombre = input("Te llamas:")
print("\n¡Y LLEGAS TARDE A LA REUNIÓN DE VISIÓN ESTRATÉGICA!\n"
      "Te pones de pie de un salto, sintiendo el pánico. Tienes solo cinco minutos para llegar al décimo piso,\n"
      "donde está la sala de juntas. Pero antes de salir corriendo, miras a tu desordenado cubículo."
      "\n\nHay dos cosas que podrías hacer:")
opcion_taza = input("[A]: Recoger la Taza Térmica de la Suerte: Un reluciente recipiente de acero inoxidable que dice:\n"
                    "Soy 99% café, 1% persona.\n"
                    "[B]: Ignorar la taza: No hay tiempo. Sales con las manos vacías.\n"
                    "\n-->Elige una opción [A/B]: ")

if opcion_taza == "A":
    taza = True
else:
    taza = False


#2. El Encuentro con el Gurú del Networking
print("\nCorres por el pasillo del noveno piso, pero un hombre musculoso y sonriente te intercepta.\n"
      "Es Chad, el Gurú de la Productividad, conocido por sus charlas interminables.\n"
      "-CHAD: ¡Amigo! ¡Alto ahí! ¡Un poco de 'calentamiento cerebral' antes de la gran reunión! \n-dice Chad, "
      "bloqueando el ascensor. \n-CHAD: No me caes bien. Eres demasiado silencioso. Pero te daré una oportunidad:\n"
      "Si fallas este desafío, le diré a la jefa que te vi robando bolígrafos.\n\n"
      "-Chad te plantea un desafío aritmético inesperado:\n")
numero1_random_Chad = random.randint(1, 100)
numero2_random_Chad = random.randint(1, 100)
resultado = int(input("-CHAD: Tengo un número {} y otro número {}. Multiplícalos en tu cabeza: {}*{}.¡Rápido!\n"
      "\n-->Responde, RÁPIDO! {} * {}, Chad se esta riendo:"
      .format(numero1_random_Chad, numero2_random_Chad, numero1_random_Chad, numero2_random_Chad,
                                                                            numero1_random_Chad, numero2_random_Chad)))

if resultado == numero1_random_Chad * numero2_random_Chad:
    print("\n\nEl rostro de Chad se contrae en una máscara de pura furia.\n"
        "-CHAD: ¡Lo hiciste bien! ¡Odio a los cerebritos! "
        "¡Odio a la gente que me recuerda que hay otras cosas además del networking!"
        "-Chad saca una mini-pistola de dardos tranquilizantes y te dispara al cuello. Caes desplomado.\n"
        "¡FIN DE LA HISTORIA! Mueres a manos del Gurú de la Productividad.")
    input("\nPulsa INTRO para cerrar. Gracias.")
    exit()

else:
    print("\nChad se ríe a carcajadas.\n"
        "-CHAD: ¡Qué decepción! Solo era un calentamiento, colega. Pero no importa, sigue. Te veo en el ascensor.\n"
        "-Conclusión: Te deja pasar, pero te mira con desprecio. Tu vida continúa (por ahora).\n")


#3. El Dilema del Desayuno
print("Logras escapar de Chad (o sobrevivir a su furia).\n"
      "Llegas al décimo piso y ves la sala de conferencias, "
      "pero te das cuenta de que no has comido nada. \n"
      "Tu estómago ruge como un servidor sobrecalentado.\n\n"
      "[A]Entrar directamente a la reunión: Ignoras el hambre. La concentración es clave.\n"
      "[B]Ir a la cocina a por un muffin: Es un desvío arriesgado,\n"
      "pero un poco de azúcar te ayudará a sobrevivir la presentación.")

while True:

    opcion = input("Elige una opción [A/B]: \n")



    if opcion == "A": #Saltas a la 4ª sección directamente
        print("Has llegado a la reunión y sobrevivido al encuentro con la Sra. Grimson "
          "(o has evitado la cocina por completo). Te sientas en la mesa y te das cuenta de que la reunión es sobre... "
          "cómo organizar una fiesta de cumpleaños para el perro del jefe.\n"
          "-SRA. GRIMSON: ¡Felicidades! Parece que has superado la prueba de estrés de la mañana. "
          "Ahora, ¿qué color de gorro le ponemos al caniche? Tu opinión es estratégica.\n\n")
        print("¡FIN DE LA HISTORIA! Sobrevives (pero tu futuro laboral es más incierto que nunca).")
        input("\nPulsa INTRO para cerrar. Gracias.")
        break

    elif opcion == "B": #Saltas a la 4ª sección directamente
        print("\n\nTe diriges a la cocina. Tomas un muffin rancio y, al darte la vuelta, te encuentras con la Sra. Grimson, "
          "que está mirando fijamente una pila de vasos desechables sucios en la encimera. \n"
          "Su aura es de puro resentimiento corporativo.")
        break

    else:
        print("\n\nSolo puedes escribir [A/B]. Revisa que sea en mayúsculas.")


if taza == True:
        print("-SRA. GRIMSON: Dime, empleado, veo que tienes una taza. \n"
              "-Le muestras la reluciente taza y le dices asustado:")
        print("-" + nombre.upper() + ": ¡Solo agua en mi taza reutilizable, Sra. Grimson! "
              "¡Por el planeta y la eficiencia!\n"
              "-La jefa parpadea.\n"
              "-SRA.GRIMSON: Bien. La sostenibilidad es... encomiable. Vuelve al trabajo.\n")
        input("\nPulsa INTRO para continuar...\n")
        print("Conclusión: Te salva el objeto. Te deja pasar.\n")

        #4. El Desenlace (Supervivencia)
        print("Has llegado a la reunión y sobrevivido al encuentro con la Sra. Grimson "
              "(o has evitado la cocina por completo). Te sientas en la mesa y "
              "te das cuenta de que la reunión es sobre... "
              "cómo organizar una fiesta de cumpleaños para el perro del jefe.\n"
              "-SRA. GRIMSON: ¡Felicidades! Parece que has superado la prueba de estrés de la mañana. "
              "Ahora, ¿qué color de gorro le ponemos al caniche? Tu opinión es estratégica.\n\n"
              "¡FIN DE LA HISTORIA! Sobrevives (pero tu futuro laboral es más incierto que nunca).")
        input("\nPulsa INTRO para cerrar. Gracias.")

elif taza == False:
        print("Sostienes el vaso de plástico desechable que acabas de agarrar. "
              "La Sra. Grimson grita, con la vena del cuello hinchada: \n"
              "-SRA.GRIMSON: ¡VASOS DESECHABLES! ¡ESTÁN ARRUINANDO EL PLANETA Y MI ESTADO DE ÁNIMO! ¡ESTÁS DESPEDIDO!"
              "¡Y POR CIERTO, ESO ES UN MUFFIN CADUCADO! \n\n"
              "¡FIN DE LA HISTORIA! Mueres de vergüenza y despedido.")
        input("\nPulsa INTRO para cerrar. Gracias.")