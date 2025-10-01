import random
import os


#Variables

titulo = "⚔️¡Un combate Pokémon comienza!⚔️"
turno_cpu = "🧢'¡Turno de Pikachu!'⚡ + \n"
emotes_turno_cpu = "🔹" * 12 + "\n"
turno_ataque = "⚔️'¡Turno de Squirtle!'💦 + \n"
emotes_turno_ataque = "🔻" * 13 + "\n"
LONGITUD_BARRA = 20


#Variables Pikachu

HP_INICIAL_PIKACHU = 70
hp_pikachu = 70
impactrueno = 11
ataque_rapido = 10


#Variables Squirtle

HP_INICIAL_SQUIRTLE = 70
hp_squirtle = 70
placaje = 10
pistola_agua = 12
burbuja = 9




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
os.system("cls")

print("\n\n" + titulo + "\n" + "-" * len(titulo) + "\n")
input("✅ Enter...")
os.system("cls")




#Asignación del nombre del "entrenador pokemon".

entrenador_pokemon = input("🧑 ¿Cual es el nombre del entrenador Pokemon de hoy?\n\n")
os.system("cls")
print(f"\n🧑 ¡{entrenador_pokemon} envía a Squirtle!💦\n")
print("¡En la otra esquina, el Pikachu⚡ de Ash🧢 entra en combate!\n")
input("✅ Enter...")
os.system("cls")




#************************************************ "#Combate ************************************************************




while hp_pikachu > 0 and hp_squirtle > 0:
    #Se desenvuelven los turnos de combate.




#--------------------------------------------- Turno Pikachu (CPU). ----------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------




    #Título turno Pikachu.

    print(emotes_turno_cpu + turno_cpu + emotes_turno_cpu)


    #Selección de ataque random CPU.

    ataque_pikachu = random.randint(1, 2)


    # Mecánica 10% probabilidad de esquivar el ataque de pikachu.

    esquiva_squirtle = random.randint(1, 10)

    if esquiva_squirtle == 1:

        if ataque_pikachu == 1:

            print("¡Pikachu usa Impactrueno! ⚡⚡⚡\n")
            print(">--< Pikachu lanza un rayo eléctrico.⚡\n")
            print("\n⚡ 🌀Pero... ¡¡¡SQUIRTLE ESQUIVÓ IMPACTRUENO!!!💨\n")

        else:
            print("¡Pikachu usa Ataque Rápido! 💨💨💨\n")
            print(">>>>> Pikachu se mueve a toda velocidad.\n")
            print("\n⚡ 🌀Pero... ¡¡¡SQUIRTLE ESQUIVÓ EL ATAQUE RÁPIDO!!!💨\n")




        #Barra de vida por si falla Pikachu.

        barras_de_vida_pikachu = int(hp_pikachu * LONGITUD_BARRA / HP_INICIAL_PIKACHU)
        barras_de_vida_squirtle = int(hp_squirtle * LONGITUD_BARRA / HP_INICIAL_SQUIRTLE)
        print(f"La vida de Pikachu es de [{"🔶" * barras_de_vida_pikachu}{"🔸" * 
                                     (LONGITUD_BARRA - barras_de_vida_pikachu)}]({hp_pikachu}/{HP_INICIAL_PIKACHU})hp.")
        print(f"La vida de Squirtle es de [{"🔷" * barras_de_vida_squirtle}{"🔹" * 
                               (LONGITUD_BARRA - barras_de_vida_squirtle)}]({hp_squirtle}/{HP_INICIAL_SQUIRTLE})hp. \n")

        input("✅ Enter...")
        os.system("cls")



    #Ataques Pikachu.

    else:

        if ataque_pikachu == 1:
            # Impactrueno.
            print("¡Pikachu usa Impactrueno! ⚡⚡⚡\n")
            print(">--< Pikachu lanza un rayo eléctrico.⚡\n")

            danho = impactrueno
            hp_squirtle -= danho
            hp_squirtle = max(hp_squirtle, 0)

            icono = "⚡"

            if hp_squirtle > 50:
                mensaje_estado_squirtle = f"¡Squirtle💦 ha recibido {danho} de daño {icono}, pero sigue con fuerzas!\n"

            elif hp_squirtle > 40:
                mensaje_estado_squirtle = f"¡Squirtle💦 ha recibido {danho} de daño {icono}!\n"

            elif hp_squirtle > 30:
                mensaje_estado_squirtle = (f"¡Squirtle💦 ha recibido {danho} de daño {icono} "
                                           f"y ya se siente resentido!\n")

            elif hp_squirtle > 20:
                mensaje_estado_squirtle = f"¡Squirtle💦 ha recibido {danho} de daño {icono} y está debilitado!\n"

            elif hp_pikachu >= 1:
                mensaje_estado_squirtle = (f"¡Pikachu ha recibido {danho} de daño {icono}. "
                                           f"Ya aguanta con muy poca energía!\n")
                
            else:
                mensaje_estado_squirtle = f"¡Pikachu ha recibido daño y ha caído derrotado!\n"

            print(mensaje_estado_squirtle)


        else:
            # Ataque rápido.
            print("¡Pikachu usa Ataque Rápido! 💨💨💨\n")
            print(">>>>> Pikachu se mueve a toda velocidad.\n")

            danho = ataque_rapido
            hp_squirtle -= danho
            hp_squirtle = max(hp_squirtle, 0)

            icono = "💨"

            if hp_squirtle > 50:
                mensaje_estado_squirtle = (f"¡Squirtle💦 ha recibido {danho} de daño {icono}, "
                                           f"pero sigue con fuerzas!\n")

            elif hp_squirtle > 40:
                mensaje_estado_squirtle = f"¡Squirtle💦 ha recibido {danho} de daño {icono}!\n"

            elif hp_squirtle > 30:
                mensaje_estado_squirtle = (f"¡Squirtle💦 ha recibido {danho} de daño {icono} "
                                           f"y ya se siente resentido!\n")

            elif hp_squirtle > 20:
                mensaje_estado_squirtle = f"¡Squirtle💦 ha recibido {danho} de daño {icono} y está debilitado!\n"

            elif hp_pikachu >= 1:
                mensaje_estado_squirtle = (f"¡Pikachu ha recibido {danho} de daño {icono}. "
                                           f"Ya aguanta con muy poca energía!\n")
                
            else:
                mensaje_estado_squirtle = f"¡Pikachu ha recibido daño y ha caído derrotado!\n"

            print(mensaje_estado_squirtle)


        #Barra de vida.

        barras_de_vida_pikachu = int(hp_pikachu * LONGITUD_BARRA / HP_INICIAL_PIKACHU)
        barras_de_vida_squirtle = int(hp_squirtle * LONGITUD_BARRA / HP_INICIAL_SQUIRTLE)
        print(f"La vida de Pikachu es de [{"🔶" * barras_de_vida_pikachu}{"🔸" * 
                                     (LONGITUD_BARRA - barras_de_vida_pikachu)}]({hp_pikachu}/{HP_INICIAL_PIKACHU})hp.")
        print(f"\nLa vida de Squirtle es de [{"🔷" * barras_de_vida_squirtle}{"🔹" * 
                               (LONGITUD_BARRA - barras_de_vida_squirtle)}]({hp_squirtle}/{HP_INICIAL_SQUIRTLE})hp. \n")

        input("\n✅ Enter...")
        os.system("cls")




    #Mecánica para comprobar si squirtle ha muerto. :S

    if hp_squirtle == 0:
        print("⚡👑 ¡EL ENTRENADOR ASH HA GANADO EL COMBATE CON SU PIKACHU! ⚡🐭\n")
        input("🔁 Enter para cerrar. ¡Suerte la próxima vez!")
        exit()





    #------------------------------------------- Turno Squirtle (Usuario). ---------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------




    #Título del turno de ataque del Usuario.

    print(emotes_turno_ataque + turno_ataque + emotes_turno_ataque +
          "🤜 [P]lacaje.\n💦 Pistola [A]gua.\n🫧 [B]urbuja.\n 🤷[N]o hacer nada.\n" + emotes_turno_ataque)




    #Input y selección del ataque del Usuario.

    ataque_squirtle = input("Introduce la letra del ataque (🤜[P], 💦[A], 🫧[B] o 🤷[N]): ").strip().upper()

    while ataque_squirtle not in ["P", "A", "B", "N"]:

        print("\nOpción no válida. Solo se admite P, B, A o N.\n")
        ataque_squirtle = input("Introduce la letra del ataque (🤜[P], 💦[A], 🫧[B] o 🤷[N]): ").strip().upper()


    os.system("cls")
    print(emotes_turno_ataque + turno_ataque + emotes_turno_ataque)

    # Mecánica 10% probabilidad de esquivar el ataque de pikachu.

    esquiva_pikachu = random.randint(1, 10)

    if esquiva_pikachu == 1 and ataque_squirtle != "N":

        if ataque_squirtle == "P":
            #Esquiva Placaje.

            print("¡Squirtle usa Placaje! 🤜💥\n")
            print("Squirtle embiste con fuerza.\n")
            print("\n🤜🌀 Pero... ¡¡¡PIKACHU ESQUIVÓ PLACAJE!!!💨\n")

        elif ataque_squirtle == "A":
            #Esquiva Pistola Agua.

            print("¡Squirtle usa Pistola Agua! 💦💦💦\n")
            print("~~~> Squirtle dispara agua a presión.\n")
            print("\n💦🌀 Pero... ¡¡¡PIKACHU ESQUIVÓ PISTOLA AGUA!!!💨\n")

        else:
            #Esquiva Burbuja.

            print("¡Squirtle usa Burbuja! 🫧🫧🫧\n")
            print("o o o Squirtle lanza burbujas.\n")
            print("\n🫧🌀 Pero... ¡¡¡PIKACHU ESQUIVÓ BURBUJA!!!💨\n")


        # Barra de vida por si falla.

        barras_de_vida_pikachu = int(hp_pikachu * LONGITUD_BARRA / HP_INICIAL_PIKACHU)
        barras_de_vida_squirtle = int(hp_squirtle * LONGITUD_BARRA / HP_INICIAL_SQUIRTLE)
        print(f"La vida de Pikachu es de [{"🔶" * barras_de_vida_pikachu}{"🔸" * 
                                     (LONGITUD_BARRA - barras_de_vida_pikachu)}]({hp_pikachu}/{HP_INICIAL_PIKACHU})hp.")

        print(f"La vida de Squirtle es de [{"🔷" * barras_de_vida_squirtle}{"🔹" * 
                               (LONGITUD_BARRA - barras_de_vida_squirtle)}]({hp_squirtle}/{HP_INICIAL_SQUIRTLE})hp. \n")

        input("✅ Enter...")
        os.system("cls")

    else:

        if ataque_squirtle == "P":
            #Placaje.
            print("¡Squirtle usa Placaje! 🤜💥\n")
            print("Squirtle embiste con fuerza.\n")

            danho = placaje
            hp_pikachu -= danho
            hp_pikachu = max(hp_pikachu, 0)

            icono = "💥"

            if hp_pikachu > 50:
                mensaje_estado_pikachu = f"¡Pikachu⚡ ha recibido {danho} de daño {icono}, pero sigue con fuerzas!\n"

            elif hp_pikachu > 40:
                mensaje_estado_pikachu = f"¡Pikachu⚡ ha recibido {danho} de daño {icono}!\n"

            elif hp_pikachu > 30:
                mensaje_estado_pikachu = f"¡Pikachu⚡ ha recibido {danho} de daño {icono} y ya se siente resentido!\n"

            elif hp_pikachu > 20:
                mensaje_estado_pikachu = f"¡Pikachu⚡ ha recibido {danho} de daño {icono}. Está debilitado!\n"

            elif hp_pikachu >= 1:
                mensaje_estado_pikachu = (f"¡Pikachu ha recibido {danho} de daño {icono}. "
                                          f"Ya aguanta con muy poca energía!\n")
                
            else:
                mensaje_estado_pikachu = f"¡Pikachu ha recibido daño y ha caído derrotado!\n"

            print(mensaje_estado_pikachu)


        elif ataque_squirtle == "A":
            #Pistola Agua.
            print("¡Squirtle usa Pistola Agua! 💦💦💦\n")
            print("~~~> Squirtle dispara agua a presión.\n")

            danho = pistola_agua
            hp_pikachu -= danho
            hp_pikachu = max(hp_pikachu, 0)

            icono = "💦"

            if hp_pikachu > 50:
                mensaje_estado_pikachu = (f"¡Pikachu⚡ ha recibido {danho} de daño {icono}, "
                                          f"pero sigue con fuerzas!\n")

            elif hp_pikachu > 40:
                mensaje_estado_pikachu = f"¡Pikachu⚡ ha recibido {danho} de daño {icono}!\n"

            elif hp_pikachu > 30:
                mensaje_estado_pikachu = (f"¡Pikachu⚡ ha recibido {danho} de daño {icono} "
                                          f"y ya se siente resentido!\n")

            elif hp_pikachu > 20:
                mensaje_estado_pikachu = f"¡Pikachu⚡ ha recibido {danho} de daño {icono}. Está debilitado!\n"

            elif hp_pikachu >= 1:
                mensaje_estado_pikachu = (f"¡Pikachu ha recibido {danho} de daño {icono}. "
                                          f"Ya aguanta con muy poca energía!\n")
                
            else:
                mensaje_estado_pikachu = f"¡Pikachu ha recibido daño y ha caído derrotado!\n"

            print(mensaje_estado_pikachu)


        elif ataque_squirtle == "B":
            #Burbuja.
            print("¡Squirtle usa Burbuja! 🫧🫧🫧\n")
            print("o o o Squirtle lanza burbujas.\n")

            danho = burbuja
            hp_pikachu -= danho
            hp_pikachu = max(hp_pikachu, 0)

            icono = "🫧"

            if hp_pikachu > 50:
                mensaje_estado_pikachu = f"¡Pikachu ha recibido {danho} de daño {icono}, pero sigue con fuerzas!\n"

            elif hp_pikachu > 40:
                mensaje_estado_pikachu = f"¡Pikachu ha recibido {danho} de daño {icono}!\n"

            elif hp_pikachu > 30:
                mensaje_estado_pikachu = f"¡Pikachu ha recibido {danho} de daño {icono} y ya se siente resentido!\n"

            elif hp_pikachu > 20:
                mensaje_estado_pikachu = f"¡Pikachu ha recibido {danho} de daño {icono}. Está debilitado!\n"

            elif hp_pikachu >= 1:
                mensaje_estado_pikachu = (f"¡Pikachu ha recibido {danho} de daño {icono}. "
                                          f"Ya aguanta con muy poca energía!\n")
                
            else:
                mensaje_estado_pikachu = f"¡Pikachu ha recibido daño y ha caído derrotado!\n"

            print(mensaje_estado_pikachu)




        else:
            #No hacer nada.
            print(f"🤷 ¡{entrenador_pokemon} decide no hacer nada! 🤷\n")
            print("😴 Squirtle se tumba desesperado... 😴\n")
            print("Pikachu no ha recibido  daño. 🤷\n")




        #Barra de vida.

        barras_de_vida_pikachu = int(hp_pikachu * LONGITUD_BARRA / HP_INICIAL_PIKACHU)
        barras_de_vida_squirtle = int(hp_squirtle * LONGITUD_BARRA / HP_INICIAL_SQUIRTLE)
        print(f"La vida de Pikachu es de [{"🔶" * barras_de_vida_pikachu}{"🔸" * 
                                     (LONGITUD_BARRA - barras_de_vida_pikachu)}]({hp_pikachu}/{HP_INICIAL_PIKACHU})hp.")

        print(f"La vida de Squirtle es de [{"🔷" * barras_de_vida_squirtle}{"🔹" * 
                               (LONGITUD_BARRA - barras_de_vida_squirtle)}]({hp_squirtle}/{HP_INICIAL_SQUIRTLE})hp. \n")

        input("\n✅ Enter...")
        os.system("cls")




    # Mecánica para comprobar si Pikachu ha muerto (Después del ataque de Squirtle).

    if hp_pikachu == 0:
        print(f"🎉🏆 ¡{entrenador_pokemon.upper()} HA GANADO EL COMBATE CON SU SQUIRTLE! 💦️⚔️")
        print("Insertar... 🎵 Música de victoria 🎵")
        input("✅ Enter para cerrar. Enhorabuena! 🎉🏆")
        exit()