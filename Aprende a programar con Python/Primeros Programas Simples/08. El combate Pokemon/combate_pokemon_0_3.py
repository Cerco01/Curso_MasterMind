import random
import os


#Variables

title = "⚔️¡Un combate Pokémon comienza!⚔️"
cpu_turn_text = "🧢'¡Turno de Pikachu!'⚡ + \n"
cpu_turn_emotes = "🔹" * 12 + "\n"
player_turn_text = "⚔️'¡Turno de Squirtle!'💦 + \n"
player_turn_emotes = "🔻" * 13 + "\n"
BAR_LENGTH = 20


#Variables Pikachu

PIKACHU_INITIAL_HP = 70
pikachu_hp = 70
thunder_shock_damage = 11
quick_attack_damage = 10


#Variables Squirtle

SQUIRTLE_INITIAL_HP = 70
squirtle_hp = 70
tackle_damage = 10
water_gun_damage = 12
bubble_damage = 9




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

print("\n\n" + title + "\n" + "-" * len(title) + "\n")
input("✅ Enter...")
os.system("cls")




#Asignación del nombre del "entrenador pokemon".

pokemon_trainer_name = input("🧑 ¿Cual es el nombre del entrenador Pokemon de hoy?\n\n")
os.system("cls")
print(f"\n🧑 ¡{pokemon_trainer_name} envía a Squirtle!💦\n")
print("¡En la otra esquina, el Pikachu⚡ de Ash🧢 entra en combate!\n")
input("✅ Enter...")
os.system("cls")




#************************************************ "#Combate ************************************************************




while pikachu_hp > 0 and squirtle_hp > 0:
    #Se desenvuelven los turnos de combate.




#--------------------------------------------- Turno Pikachu (CPU). ----------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------




    #Título turno Pikachu.

    print(cpu_turn_emotes + cpu_turn_text + cpu_turn_emotes)


    #Selección de ataque random CPU.

    pikachu_attack_choice = random.randint(1, 2)


    # Mecánica 10% probabilidad de esquivar el ataque de pikachu.

    squirtle_dodge_roll = random.randint(1, 10)

    if squirtle_dodge_roll == 1:

        if pikachu_attack_choice == 1:

            print("¡Pikachu usa Impactrueno! ⚡⚡⚡\n")
            print(">--< Pikachu lanza un rayo eléctrico.⚡\n")
            print("\n⚡ 🌀Pero... ¡¡¡SQUIRTLE ESQUIVÓ IMPACTRUENO!!!💨\n")

        else:
            print("¡Pikachu usa Ataque Rápido! 💨💨💨\n")
            print(">>>>> Pikachu se mueve a toda velocidad.\n")
            print("\n⚡ 🌀Pero... ¡¡¡SQUIRTLE ESQUIVÓ EL ATAQUE RÁPIDO!!!💨\n")




        #Barra de vida por si falla Pikachu.

        pikachu_hp_bars = int(pikachu_hp * BAR_LENGTH / PIKACHU_INITIAL_HP)
        squirtle_hp_bars = int(squirtle_hp * BAR_LENGTH / SQUIRTLE_INITIAL_HP)
        print(f"La vida de Pikachu es de [{"🔶" * pikachu_hp_bars}{"🔸" *
                                                                  (BAR_LENGTH - pikachu_hp_bars)}]({pikachu_hp}/{PIKACHU_INITIAL_HP})hp.")
        print(f"La vida de Squirtle es de [{"🔷" * squirtle_hp_bars}{"🔹" *
                                                                    (BAR_LENGTH - squirtle_hp_bars)}]({squirtle_hp}/{SQUIRTLE_INITIAL_HP})hp. \n")

        input("✅ Enter...")
        os.system("cls")



    #Ataques Pikachu.

    else:

        if pikachu_attack_choice == 1:
            # Impactrueno.
            print("¡Pikachu usa Impactrueno! ⚡⚡⚡\n")
            print(">--< Pikachu lanza un rayo eléctrico.⚡\n")

            damage = thunder_shock_damage
            squirtle_hp -= damage
            squirtle_hp = max(squirtle_hp, 0)

            icon = "⚡"

            if squirtle_hp > 50:
                squirtle_status_message = f"¡Squirtle💦 ha recibido {damage} de daño {icon}, pero sigue con fuerzas!\n"

            elif squirtle_hp > 40:
                squirtle_status_message = f"¡Squirtle💦 ha recibido {damage} de daño {icon}!\n"

            elif squirtle_hp > 30:
                squirtle_status_message = (f"¡Squirtle💦 ha recibido {damage} de daño {icon} "
                                           f"y ya se siente resentido!\n")

            elif squirtle_hp > 20:
                squirtle_status_message = f"¡Squirtle💦 ha recibido {damage} de daño {icon} y está debilitado!\n"

            elif pikachu_hp >= 1:
                squirtle_status_message = (f"¡Pikachu ha recibido {damage} de daño {icon}. "
                                           f"Ya aguanta con muy poca energía!\n")
                
            else:
                squirtle_status_message = f"¡Pikachu ha recibido daño y ha caído derrotado!\n"

            print(squirtle_status_message)


        else:
            # Ataque rápido.
            print("¡Pikachu usa Ataque Rápido! 💨💨💨\n")
            print(">>>>> Pikachu se mueve a toda velocidad.\n")

            damage = quick_attack_damage
            squirtle_hp -= damage
            squirtle_hp = max(squirtle_hp, 0)

            icon = "💨"

            if squirtle_hp > 50:
                squirtle_status_message = (f"¡Squirtle💦 ha recibido {damage} de daño {icon}, "
                                           f"pero sigue con fuerzas!\n")

            elif squirtle_hp > 40:
                squirtle_status_message = f"¡Squirtle💦 ha recibido {damage} de daño {icon}!\n"

            elif squirtle_hp > 30:
                squirtle_status_message = (f"¡Squirtle💦 ha recibido {damage} de daño {icon} "
                                           f"y ya se siente resentido!\n")

            elif squirtle_hp > 20:
                squirtle_status_message = f"¡Squirtle💦 ha recibido {damage} de daño {icon} y está debilitado!\n"

            elif pikachu_hp >= 1:
                squirtle_status_message = (f"¡Pikachu ha recibido {damage} de daño {icon}. "
                                           f"Ya aguanta con muy poca energía!\n")
                
            else:
                squirtle_status_message = f"¡Pikachu ha recibido daño y ha caído derrotado!\n"

            print(squirtle_status_message)


        #Barra de vida.

        pikachu_hp_bars = int(pikachu_hp * BAR_LENGTH / PIKACHU_INITIAL_HP)
        squirtle_hp_bars = int(squirtle_hp * BAR_LENGTH / SQUIRTLE_INITIAL_HP)
        print(f"La vida de Pikachu es de [{"🔶" * pikachu_hp_bars}{"🔸" *
                                                                  (BAR_LENGTH - pikachu_hp_bars)}]({pikachu_hp}/{PIKACHU_INITIAL_HP})hp.")
        print(f"\nLa vida de Squirtle es de [{"🔷" * squirtle_hp_bars}{"🔹" *
                                                                      (BAR_LENGTH - squirtle_hp_bars)}]({squirtle_hp}/{SQUIRTLE_INITIAL_HP})hp. \n")

        input("\n✅ Enter...")
        os.system("cls")




    #Mecánica para comprobar si squirtle ha muerto. :S

    if squirtle_hp == 0:
        print("⚡👑 ¡EL ENTRENADOR ASH HA GANADO EL COMBATE CON SU PIKACHU! ⚡🐭\n")
        input("🔁 Enter para cerrar. ¡Suerte la próxima vez!")
        exit()





    #------------------------------------------- Turno Squirtle (Usuario). ---------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------




    #Título del turno de ataque del Usuario.

    print(player_turn_emotes + player_turn_text + player_turn_emotes +
          "🤜 [P]lacaje.\n💦 Pistola [A]gua.\n🫧 [B]urbuja.\n 🤷[N]o hacer nada.\n" + player_turn_emotes)




    #Input y selección del ataque del Usuario.

    squirtle_attack_input = input("Introduce la letra del ataque (🤜[P], 💦[A], 🫧[B] o 🤷[N]): ").strip().upper()

    while squirtle_attack_input not in ["P", "A", "B", "N"]:

        print("\nOpción no válida. Solo se admite P, B, A o N.\n")
        squirtle_attack_input = input("Introduce la letra del ataque (🤜[P], 💦[A], 🫧[B] o 🤷[N]): ").strip().upper()


    os.system("cls")
    print(player_turn_emotes + player_turn_text + player_turn_emotes)

    # Mecánica 10% probabilidad de esquivar el ataque de pikachu.

    pikachu_dodge_roll = random.randint(1, 10)

    if pikachu_dodge_roll == 1 and squirtle_attack_input != "N":

        if squirtle_attack_input == "P":
            #Esquiva Placaje.

            print("¡Squirtle usa Placaje! 🤜💥\n")
            print("Squirtle embiste con fuerza.\n")
            print("\n🤜🌀 Pero... ¡¡¡PIKACHU ESQUIVÓ PLACAJE!!!💨\n")

        elif squirtle_attack_input == "A":
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

        pikachu_hp_bars = int(pikachu_hp * BAR_LENGTH / PIKACHU_INITIAL_HP)
        squirtle_hp_bars = int(squirtle_hp * BAR_LENGTH / SQUIRTLE_INITIAL_HP)
        print(f"La vida de Pikachu es de [{"🔶" * pikachu_hp_bars}{"🔸" *
                                                                  (BAR_LENGTH - pikachu_hp_bars)}]({pikachu_hp}/{PIKACHU_INITIAL_HP})hp.")

        print(f"La vida de Squirtle es de [{"🔷" * squirtle_hp_bars}{"🔹" *
                                                                    (BAR_LENGTH - squirtle_hp_bars)}]({squirtle_hp}/{SQUIRTLE_INITIAL_HP})hp. \n")

        input("✅ Enter...")
        os.system("cls")

    else:

        if squirtle_attack_input == "P":
            #Placaje.
            print("¡Squirtle usa Placaje! 🤜💥\n")
            print("Squirtle embiste con fuerza.\n")

            damage = tackle_damage
            pikachu_hp -= damage
            pikachu_hp = max(pikachu_hp, 0)

            icon = "💥"

            if pikachu_hp > 50:
                pikachu_status_message = f"¡Pikachu⚡ ha recibido {damage} de daño {icon}, pero sigue con fuerzas!\n"

            elif pikachu_hp > 40:
                pikachu_status_message = f"¡Pikachu⚡ ha recibido {damage} de daño {icon}!\n"

            elif pikachu_hp > 30:
                pikachu_status_message = f"¡Pikachu⚡ ha recibido {damage} de daño {icon} y ya se siente resentido!\n"

            elif pikachu_hp > 20:
                pikachu_status_message = f"¡Pikachu⚡ ha recibido {damage} de daño {icon}. Está debilitado!\n"

            elif pikachu_hp >= 1:
                pikachu_status_message = (f"¡Pikachu ha recibido {damage} de daño {icon}. "
                                          f"Ya aguanta con muy poca energía!\n")
                
            else:
                pikachu_status_message = f"¡Pikachu ha recibido daño y ha caído derrotado!\n"

            print(pikachu_status_message)


        elif squirtle_attack_input == "A":
            #Pistola Agua.
            print("¡Squirtle usa Pistola Agua! 💦💦💦\n")
            print("~~~> Squirtle dispara agua a presión.\n")

            damage = water_gun_damage
            pikachu_hp -= damage
            pikachu_hp = max(pikachu_hp, 0)

            icon = "💦"

            if pikachu_hp > 50:
                pikachu_status_message = (f"¡Pikachu⚡ ha recibido {damage} de daño {icon}, "
                                          f"pero sigue con fuerzas!\n")

            elif pikachu_hp > 40:
                pikachu_status_message = f"¡Pikachu⚡ ha recibido {damage} de daño {icon}!\n"

            elif pikachu_hp > 30:
                pikachu_status_message = (f"¡Pikachu⚡ ha recibido {damage} de daño {icon} "
                                          f"y ya se siente resentido!\n")

            elif pikachu_hp > 20:
                pikachu_status_message = f"¡Pikachu⚡ ha recibido {damage} de daño {icon}. Está debilitado!\n"

            elif pikachu_hp >= 1:
                pikachu_status_message = (f"¡Pikachu ha recibido {damage} de daño {icon}. "
                                          f"Ya aguanta con muy poca energía!\n")
                
            else:
                pikachu_status_message = f"¡Pikachu ha recibido daño y ha caído derrotado!\n"

            print(pikachu_status_message)


        elif squirtle_attack_input == "B":
            #Burbuja.
            print("¡Squirtle usa Burbuja! 🫧🫧🫧\n")
            print("o o o Squirtle lanza burbujas.\n")

            damage = bubble_damage
            pikachu_hp -= damage
            pikachu_hp = max(pikachu_hp, 0)

            icon = "🫧"

            if pikachu_hp > 50:
                pikachu_status_message = f"¡Pikachu ha recibido {damage} de daño {icon}, pero sigue con fuerzas!\n"

            elif pikachu_hp > 40:
                pikachu_status_message = f"¡Pikachu ha recibido {damage} de daño {icon}!\n"

            elif pikachu_hp > 30:
                pikachu_status_message = f"¡Pikachu ha recibido {damage} de daño {icon} y ya se siente resentido!\n"

            elif pikachu_hp > 20:
                pikachu_status_message = f"¡Pikachu ha recibido {damage} de daño {icon}. Está debilitado!\n"

            elif pikachu_hp >= 1:
                pikachu_status_message = (f"¡Pikachu ha recibido {damage} de daño {icon}. "
                                          f"Ya aguanta con muy poca energía!\n")
                
            else:
                pikachu_status_message = f"¡Pikachu ha recibido daño y ha caído derrotado!\n"

            print(pikachu_status_message)




        else:
            #No hacer nada.
            print(f"🤷 ¡{pokemon_trainer_name} decide no hacer nada! 🤷\n")
            print("😴 Squirtle se tumba desesperado... 😴\n")
            print("Pikachu no ha recibido  daño. 🤷\n")




        #Barra de vida.

        pikachu_hp_bars = int(pikachu_hp * BAR_LENGTH / PIKACHU_INITIAL_HP)
        squirtle_hp_bars = int(squirtle_hp * BAR_LENGTH / SQUIRTLE_INITIAL_HP)
        print(f"La vida de Pikachu es de [{"🔶" * pikachu_hp_bars}{"🔸" *
                                                                  (BAR_LENGTH - pikachu_hp_bars)}]({pikachu_hp}/{PIKACHU_INITIAL_HP})hp.")

        print(f"La vida de Squirtle es de [{"🔷" * squirtle_hp_bars}{"🔹" *
                                                                    (BAR_LENGTH - squirtle_hp_bars)}]({squirtle_hp}/{SQUIRTLE_INITIAL_HP})hp. \n")

        input("\n✅ Enter...")
        os.system("cls")




    # Mecánica para comprobar si Pikachu ha muerto (Después del ataque de Squirtle).

    if pikachu_hp == 0:
        print(f"🎉🏆 ¡{pokemon_trainer_name.upper()} HA GANADO EL COMBATE CON SU SQUIRTLE! 💦️⚔️")
        print("Insertar... 🎵 Música de victoria 🎵")
        input("✅ Enter para cerrar. Enhorabuena! 🎉🏆")
        exit()