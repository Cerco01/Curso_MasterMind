import random



#Variables

titulo = "⚔️¡Un combate Pokémon comienza!⚔️"
turno_ataque = "⚔️'¡Turno de ataque!'💦"
turno_cpu = "🧢'¡Es el turno de Ash!'⚡"
LONGITUD_BARRA = 20

#Variables Pikachu

HP_INICIAL_PIKACHU = 70
hp_pikachu = 70

#Variables viejas de la primera versión de la barra de salud PIKACHU

"""porcentaje_hp_pikachu = hp_pikachu / HP_INICIAL_PIKACHU
relleno_pikachu = int(porcentaje_hp_pikachu * longitud_barra)
barra_pikachu = "[" + "🔷" * relleno_pikachu + "-" * (longitud_barra - relleno_pikachu) + "]"""

#Variables Squirtle

HP_INICIAL_SQUIRTLE = 70
hp_squirtle = 70

#Variables viejas de la primera versión de la barra de salud SQUIRTLE

"""porcentaje_hp_squirtle = hp_squirtle / HP_INICIAL_SQUIRTLE
relleno_squirtle = int(porcentaje_hp_squirtle * longitud_barra)
barra_squirtle = "[" + "🔶" * relleno_squirtle + "-" * (longitud_barra - relleno_squirtle) + "]"""





# Título
print(r"""
                                  ,'\                                
    _.----.        ____         ,'  _\   ___    ___     ____         
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.   
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |  
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |  
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |  
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |  
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |  
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |  
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |  
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |  
                                `'                            '-._| 
                                                           
""")
input("✅ Okay... ¡Let's Go!")
print("\n\n" + titulo + "\n" + "-" * len(titulo) + "\n")
input("✅ Enter...")




#Separador claro
#He visto que según el tamaño de la ventana puede romper la estética. Aun así me gusta como queda y haciendo unas
#consultas he visto que en la mayoría de ventanas, un valor de entre 20 y 30 queda bien.
#Viene bien ya que de momento mientras el programa tenga la interfaz en la terminal, así se ve mejor en que paso estás
#y no se mezclan las acciones.

separador_largo = 25
print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")




entrenador_pokemon = input("🧑 ¿Cual es el nombre del entrenador Pokemon de hoy?\n\n")
print("\n🧑 ¡{} envía a Squirtle!💦\n".format(entrenador_pokemon))
print("¡En la otra esquina, el Pikachu⚡ de Ash🧢 entra en combate!\n")
input("✅ Enter...")
print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")





#Combate

while hp_pikachu > 0 and hp_squirtle > 0:

    #Se desenvuelven los turnos de combate.




    #Turno Pikachu (CPU).




    #Título turno Pikachu.

    print("🔹" * 13 + "\n" + turno_cpu + "\n" + "🔹" * 13)

    #Selección de ataque random CPU.

    ataque_pikachu = random.randint(1, 2)


    # Mecánica 10% probabilidad de fallo.

    falla_pikachu = random.randint(1, 10)

    if falla_pikachu == 1:
        print("\n🌀¡¡¡SQUIRTLE ESQUIVÓ EL ATAQUE!!!💨\n")
        input("\n✅ Enter...")
        print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")




        #Barra de vida.

        barras_de_vida_pikachu = int(hp_pikachu * LONGITUD_BARRA / HP_INICIAL_PIKACHU)
        barras_de_vida_squirtle = int(hp_squirtle * LONGITUD_BARRA / HP_INICIAL_SQUIRTLE)
        print("La vida de Pikachu  es de [{}{}]({}/{})hp."
                                    .format("🔶" * barras_de_vida_pikachu, "🔸" *
                                            (LONGITUD_BARRA - barras_de_vida_pikachu), hp_pikachu, HP_INICIAL_PIKACHU))
        print("\nLa vida de Squirtle es de [{}{}]({}/{})hp. \n"
                                  .format("🔷" * barras_de_vida_squirtle, "🔹" *
                                          (LONGITUD_BARRA - barras_de_vida_squirtle), hp_squirtle, HP_INICIAL_SQUIRTLE))
        input("✅ Enter...")
        print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")




        #Este es mi primer modelo que hice de barra de salud por mí mismo. No hacía falta, ya que Nate dijo que
        #copiaramos, pero quería aprovechar para escribir este código por mí mismo. Solo utilicé google y gemini
        #cuando me quedaba completamente atascado y después de romperme un poquito la cabeza. La verdad es que estoy
        #bastante orgulloso porque no llevo ni una semana con esto y estoy entusiasmado jajaja ya vendrán los días duros
        #supongo jajaja
        #me guardo esto por si algún día me da por revisar mis primeros proyectos jajaja Y aparte seguro que si tenéis
        #que revisar el programa os echáis unas risas.



        # Barra de vida antigua. Mantenida como apunte. BORRAR PARA LA ENTREGA.
        # Variables y barra de vida. Las coloco aquí para que se calculen en cada turno. Sinó no se actualizan.

        """porcentaje_hp_pikachu = hp_pikachu / HP_INICIAL_PIKACHU
        relleno_pikachu = int(porcentaje_hp_pikachu * longitud_barra)
        barra_pikachu = "[" + "🔶" * relleno_pikachu + "🔸" * (longitud_barra - relleno_pikachu) + "]"

        porcentaje_hp_squirtle = hp_squirtle / HP_INICIAL_SQUIRTLE
        relleno_squirtle = int(porcentaje_hp_squirtle * longitud_barra)
        barra_squirtle = "[" + "🔷" * relleno_squirtle + "🔹" * (longitud_barra - relleno_squirtle) + "]"

        print("\nLa vida de Pikachu  es de {} hp. {}\n\nLa vida de Squirtle es de {} hp. {}\n"
              "".format(hp_pikachu, barra_pikachu, hp_squirtle, barra_squirtle))
        input("✅ Enter...")
        print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")"""





    else:

        if ataque_pikachu == 1:

            #Impactrueno.

            print("\n¡Pikachu usa Impactrueno! ⚡⚡⚡\n")
            print(">--< Pikachu lanza un rayo eléctrico.\n")
            hp_squirtle -= 11
            hp_squirtle = max(hp_squirtle, 0)

            if hp_squirtle > 50:
                mensaje_estado_squirtle = "¡Squirtle ha recibido daño, pero sigue con fuerzas!\n"
            elif hp_squirtle > 40:
                mensaje_estado_squirtle = "¡Squirtle ha recibido daño!\n"
            elif hp_squirtle > 30:
                mensaje_estado_squirtle = "¡Squirtle se siente resentido!\n"
            elif hp_squirtle > 20:
                mensaje_estado_squirtle = "¡Squirtle está debilitado!\n"
            else:
                mensaje_estado_squirtle = "¡Squirtle aguanta con muy poca energía!\n"
            print(mensaje_estado_squirtle)

            input("✅ Enter...")
            print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")




        else:

            #Ataque rápido.

            print("\n¡Pikachu usa Ataque Rápido! 💨💨💨\n")
            print(">>>>> Pikachu se mueve a toda velocidad.\n")
            hp_squirtle -= 10
            hp_squirtle = max(hp_squirtle, 0)

            if hp_squirtle > 50:
                mensaje_estado_squirtle = "¡Squirtle ha recibido daño, pero sigue con fuerzas!\n"
            elif hp_squirtle > 40:
                mensaje_estado_squirtle = "¡Squirtle ha recibido daño!\n"
            elif hp_squirtle > 30:
                mensaje_estado_squirtle = "¡Squirtle se siente resentido!\n"
            elif hp_squirtle > 20:
                mensaje_estado_squirtle = "¡Squirtle está debilitado!\n"
            else:
                mensaje_estado_squirtle = "¡Squirtle aguanta con muy poca energía!\n"
            print(mensaje_estado_squirtle)

            input("✅ Enter...")
            print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")




        #Barra de vida.

        barras_de_vida_pikachu = int(hp_pikachu * LONGITUD_BARRA / HP_INICIAL_PIKACHU)
        barras_de_vida_squirtle = int(hp_squirtle * LONGITUD_BARRA / HP_INICIAL_SQUIRTLE)
        print("La vida de Pikachu  es de [{}{}]({}/{})hp."
                                .format("🔶" * barras_de_vida_pikachu, "🔸" *
                                            (LONGITUD_BARRA - barras_de_vida_pikachu), hp_pikachu, HP_INICIAL_PIKACHU))
        print("La vida de Squirtle es de [{}{}]({}/{})hp. "
                                .format("🔷" * barras_de_vida_squirtle, "🔹" *
                                        (LONGITUD_BARRA - barras_de_vida_squirtle), hp_squirtle, HP_INICIAL_SQUIRTLE))

        input("\n✅ Enter...")
        print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")





        # Barra de vida antigua. Mantenida como apunte. BORRAR PARA LA ENTREGA.
        # Variables y barra de vida. Las coloco aquí para que se calculen en cada turno. Sinó no se actualizan.
        """porcentaje_hp_pikachu = hp_pikachu / HP_INICIAL_PIKACHU
        relleno_pikachu = int(porcentaje_hp_pikachu * longitud_barra)
        barra_pikachu = "[" + "🔶" * relleno_pikachu + "🔸" * (longitud_barra - relleno_pikachu) + "]"

        porcentaje_hp_squirtle = hp_squirtle / HP_INICIAL_SQUIRTLE
        relleno_squirtle = int(porcentaje_hp_squirtle * longitud_barra)
        barra_squirtle = "[" + "🔷" * relleno_squirtle + "🔹" * (longitud_barra - relleno_squirtle) + "]"

        print("\nLa vida de Pikachu  es de {} hp. {}\n\nLa vida de Squirtle es de {} hp. {}\n"
              "".format(hp_pikachu, barra_pikachu, hp_squirtle, barra_squirtle))
        input("✅ Enter...")
        print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")"""




    #Mecánica para comprobar si pikachu ha muerto. :S

    if hp_pikachu == 0:
        print("🎉🏆 ¡{} HA GANADO EL COMBATE CON SU SQUIRTLE! 💦️⚔️".format(entrenador_pokemon.upper()))
        input("\n✅ Enter para cerrar. Enhorabuena!")
        break




#Turno Squirtle (Usuario).





    #Título del turno de ataque del Usuario.

    # noinspection SpellCheckingInspection
    print("🔻" * 10 + "\n" + turno_ataque + "\n" + "🔺" * 10 + "\n" + ""
                                "🤜[P]lacaje.\n💦Pistola [A]gua.\n🫧[B]urbuja.\n" + "🔺" * 10 + "\n")



    ataque_squirtle = None

    #Input y selección del ataque del Usuario.

    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input("Introduce la letra del ataque (🤜[P], 💦[A] o 🫧[B]):")
        print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")




    #Mecánica 10% probabilidad de fallo.

    falla_squirtle = random.randint(1, 10)

    if falla_squirtle == 1:
        print("\n⚡¡¡¡PIKACHU ESQUIVÓ EL ATAQUE!!!💨\n")
        input("✅ Enter...")
        print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")




        #Barra de vida.

        barras_de_vida_pikachu = int(hp_pikachu * LONGITUD_BARRA / HP_INICIAL_PIKACHU)
        barras_de_vida_squirtle = int(hp_squirtle * LONGITUD_BARRA / HP_INICIAL_SQUIRTLE)
        print("La vida de Pikachu  es de [{}{}]({}/{})hp."
              .format("🔶" * barras_de_vida_pikachu, "🔸" * (LONGITUD_BARRA - barras_de_vida_pikachu),
                      hp_pikachu, HP_INICIAL_PIKACHU))
        print("La vida de Squirtle es de [{}{}]({}/{})hp. "
              .format("🔷" * barras_de_vida_squirtle, "🔹" * (LONGITUD_BARRA - barras_de_vida_squirtle),
                      hp_squirtle, HP_INICIAL_SQUIRTLE))

        input("\n✅ Enter...")
        print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")





        # Barra de vida antigua. Mantenida como apunte. BORRAR PARA LA ENTREGA.
        # Variables y barra de vida. Las coloco aquí para que se calculen en cada turno. Sinó no se actualizan.

        """porcentaje_hp_pikachu = hp_pikachu / HP_INICIAL_PIKACHU
        relleno_pikachu = int(porcentaje_hp_pikachu * longitud_barra)
        barra_pikachu = "[" + "🔶" * relleno_pikachu + "🔸" * (longitud_barra - relleno_pikachu) + "]"

        porcentaje_hp_squirtle = hp_squirtle / HP_INICIAL_SQUIRTLE
        relleno_squirtle = int(porcentaje_hp_squirtle * longitud_barra)
        barra_squirtle = "[" + "🔷" * relleno_squirtle + "🔹" * (longitud_barra - relleno_squirtle) + "]"

        print("\n⚡🐭 La vida de Pikachu  es de {} hp. {}\n\n💦️⚔️ La vida de Squirtle es de {} hp. {}\n"
              "".format(hp_pikachu, barra_pikachu, hp_squirtle, barra_squirtle))
        input("✅ Enter...")
        print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")"""



    else:


        if ataque_squirtle == "P":
            #Placaje.

            print("\n¡Squirtle usa Placaje! 🤜💥\n")
            print("Squirtle embiste con fuerza.\n")
            hp_pikachu -= 10
            hp_pikachu = max(hp_pikachu, 0)

            if hp_pikachu > 50:
                mensaje_estado_pikachu = "¡Pikachu ha recibido daño, pero sigue con fuerzas!\n"
            elif hp_pikachu > 40:
                mensaje_estado_pikachu = "¡Pikachu ha recibido daño!\n"
            elif hp_pikachu > 30:
                mensaje_estado_pikachu = "¡Pikachu se siente resentido!\n"
            elif hp_pikachu > 20:
                mensaje_estado_pikachu = "¡Pikachu está debilitado!\n"
            else:
                mensaje_estado_pikachu = "¡Pikachu aguanta con muy poca energía!\n"
            print(mensaje_estado_pikachu)




        elif ataque_squirtle == "A":
            # Pistola Agua.

            print("\n¡Squirtle usa Pistola Agua! 💦💦💦\n")
            print("~~~> Squirtle dispara agua a presión.\n")
            hp_pikachu -= 12
            hp_pikachu = max(hp_pikachu, 0)

            if hp_pikachu > 50:
                mensaje_estado_pikachu = "¡Pikachu ha recibido daño, pero sigue con fuerzas!\n"
            elif hp_pikachu > 40:
                mensaje_estado_pikachu = "¡Pikachu ha recibido daño!\n"
            elif hp_pikachu > 30:
                mensaje_estado_pikachu = "¡Pikachu se siente resentido!\n"
            elif hp_pikachu > 20:
                mensaje_estado_pikachu = "¡Pikachu está debilitado!\n"
            else:
                mensaje_estado_pikachu = "¡Pikachu aguanta con muy poca energía!\n"
            print(mensaje_estado_pikachu)




        elif ataque_squirtle == "B":
            #Burbuja.

            print("\n¡Squirtle usa Burbuja! 🫧🫧🫧\n")
            print("o o o Squirtle lanza burbujas.\n")
            hp_pikachu -= 9
            hp_pikachu = max(hp_pikachu, 0)

            if hp_pikachu > 50:
                mensaje_estado_pikachu = "¡Pikachu ha recibido daño, pero sigue con fuerzas!\n"
            elif hp_pikachu > 40:
                mensaje_estado_pikachu = "¡Pikachu ha recibido daño!\n"
            elif hp_pikachu > 30:
                mensaje_estado_pikachu = "¡Pikachu se siente resentido!\n"
            elif hp_pikachu > 20:
                mensaje_estado_pikachu = "¡Pikachu está debilitado!\n"
            else:
                mensaje_estado_pikachu = "¡Pikachu aguanta con muy poca energía!\n"
            print(mensaje_estado_pikachu)

            input("✅ Enter...")
            print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")




        #Barra de vida.

        barras_de_vida_pikachu = int(hp_pikachu * LONGITUD_BARRA / HP_INICIAL_PIKACHU)
        barras_de_vida_squirtle = int(hp_squirtle * LONGITUD_BARRA / HP_INICIAL_SQUIRTLE)
        print("La vida de Pikachu  es de [{}{}]({}/{})hp."
              .format("🔶" * barras_de_vida_pikachu, "🔸" * (LONGITUD_BARRA - barras_de_vida_pikachu),
                      hp_pikachu, HP_INICIAL_PIKACHU))
        print("La vida de Squirtle es de [{}{}]({}/{})hp. "
              .format("🔷" * barras_de_vida_squirtle, "🔹" * (LONGITUD_BARRA - barras_de_vida_squirtle),
                      hp_squirtle, HP_INICIAL_SQUIRTLE))

        input("\n✅ Enter...")
        print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")






        #Barra de vida antigua. Mantenida como apunte. BORRAR PARA LA ENTREGA.
        #Variables y barra de vida. Las coloco aquí para que se calculen en cada turno. Sinó no se actualizan.


        """porcentaje_hp_pikachu = hp_pikachu / HP_INICIAL_PIKACHU
        relleno_pikachu = int(porcentaje_hp_pikachu * longitud_barra)
        barra_pikachu = "[" + "🔶" * relleno_pikachu + "🔸" * (longitud_barra - relleno_pikachu) + "]"

        porcentaje_hp_squirtle = hp_squirtle / HP_INICIAL_SQUIRTLE
        relleno_squirtle = int(porcentaje_hp_squirtle * longitud_barra)
        barra_squirtle = "[" + "🔷" * relleno_squirtle + "🔹" * (longitud_barra - relleno_squirtle) + "]"

        print("\nLa vida de Pikachu  es de {} hp. {}\n\nLa vida de Squirtle es de {} hp. {}\n"
              "".format(hp_pikachu, barra_pikachu, hp_squirtle, barra_squirtle))
        input("✅ Enter...")
        print("\n" + "🔹🔸" * separador_largo + "\n" + "🔸🔹" * separador_largo + "\n")"""






    if hp_squirtle <= 0:

        print("⚡👑 ¡EL ENTRENADOR ASH HA GANADO EL COMBATE CON SU PIKACHU! ⚡🐭\n")
        input("🔁 Enter para cerrar. ¡Suerte la próxima vez!")
        break


    elif hp_pikachu <= 0:

        print("🎉🏆 ¡{} HA GANADO EL COMBATE CON SU SQUIRTLE! 💦️⚔️".format(entrenador_pokemon.upper()))
        print("Insertar... 🎵 Música de victoria 🎵")
        input("✅ Enter para cerrar. Enhorabuena! 🎉🏆")
        break
