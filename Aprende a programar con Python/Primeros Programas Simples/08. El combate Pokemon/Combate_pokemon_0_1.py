import random

#Variables
titulo = "COMBATE POKEMON"
turno_ataque = "'¡Turno de ataque!'"
turno_cpu = "'¡Es el turno de Ash!'"
#Variables Pikachu
hp_pikachu = 60
ataque_pikachu = None
impactrueno = 11
ataque_rapido = 10
#Variables Squirtle
hp_squirtle = 60
ataque_squirtle = None
placaje = 10
pistola_agua = 12
burbuja = 9

#Título
print("\n\n" + titulo + "\n" + "-" * len(titulo) + "\n")

print("¡Un combate Pokémon comienza!\n")
entrenador_pokemon = input("¿Cual es el nombre del entrenador Pokemon de hoy?\n\n")
print("\n¡{} envía a Squirtle!\n".format(entrenador_pokemon))
print("¡En la otra esquina, el Pikachu de Ash entra en combate!\n")


#Combate
while hp_pikachu > 0 and hp_squirtle > 0:

#Turno Usuario
    print(turno_ataque + "\n" + "º" * len(turno_ataque) + "\n" + "[1]: Placaje.\n[2]: Pistola Agua.\n[3]: Burbuja."
                                                                                "\n" + "º" * len(turno_ataque) + "\n")

    ataque_squirtle = input("Introduce el número del ataque (1, 2 o 3):\n\n")

#Mecánica 10% probabilidad de fallo.
    falla_squirtle = random.randint(1, 10)
    if falla_squirtle == 1:
        print("¡¡¡PIKACHU ESQUIVÓ EL ATAQUE!!!\n")
    else:
        if ataque_squirtle == "1":
            hp_pikachu -= placaje
            print("\n¡Squirtle usa Placaje!\n")
            if hp_pikachu > 50:
                print("¡Pikachu ha recibido daño, pero sigue con fuerzas!\n")
            elif hp_pikachu > 40:
                print("¡Pikachu ha recibido daño!\n")
            elif hp_pikachu > 30:
                print("¡Pikachu se siente resentido!\n")
            elif hp_pikachu > 20:
                print("¡Pikachu está debilitado!\n")
            else:
                print("¡Pikachu aguanta con muy poca energía!\n")
            input("Enter...\n")
        elif ataque_squirtle == "2":
            hp_pikachu -= pistola_agua
            print("\n¡Squirtle usa Pistola Agua!\n")
            if hp_pikachu > 50:
                print("¡Pikachu ha recibido daño, pero sigue con fuerzas!\n")
            elif hp_pikachu > 40:
                print("¡Pikachu ha recibido daño!\n")
            elif hp_pikachu > 30:
                print("¡Pikachu se siente resentido!\n")
            elif hp_pikachu > 20:
                print("¡Pikachu está debilitado!\n")
            else:
                print("¡Pikachu aguanta con muy poca energía!\n")
            input("Enter...\n")
        elif ataque_squirtle == "3":
            hp_pikachu -= burbuja
            print("\n¡Squirtle usa Burbuja!\n")
            if hp_pikachu > 50:
                print("¡Pikachu ha recibido daño, pero sigue con fuerzas!\n")
            elif hp_pikachu > 40:
                print("¡Pikachu ha recibido daño!\n")
            elif hp_pikachu > 30:
                print("¡Pikachu se siente resentido!\n")
            elif hp_pikachu > 20:
                print("¡Pikachu está debilitado!\n")
            else:
                print("¡Pikachu aguanta con muy poca energía!\n")
            input("Enter...\n")
        else:
            print("No has escogido un ataque.\n")
            input("Enter...\n")

#Mecánica para comprobar si el pikachu ha muerto :S
    if hp_pikachu <= 0:
        print("{} HA GANADO EL COMBATE CON SQUIRTLE!".format(entrenador_pokemon.upper()))
        input("Enter para cerrar. Enhorabuena!\n")
    else:
        print()
#Turno CPU
    print(turno_cpu + "\n" + "º" * len(turno_cpu) + "\n")

    ataque_pikachu = random.randint(1, 2)

#Mecánica 10% probabilidad de fallo.
    falla_pikachu = random.randint(1, 10)
    if falla_pikachu == 1:
        print("¡¡¡SQUIRTLE ESQUIVÓ EL ATAQUE!!!\n")
    else:
        if ataque_pikachu == 1:
            hp_squirtle -= impactrueno
            print("¡Pikachu usa Impactrueno!\n")
            if hp_squirtle > 50:
                print("¡Squirtle ha recibido daño, pero sigue con fuerzas!\n")
            elif hp_squirtle > 40:
                print("¡Squirtle ha recibido daño!\n")
            elif hp_squirtle > 30:
                print("¡Squirtle se siente resentido!\n")
            elif hp_squirtle > 20:
                print("¡Squirtle está debilitado!\n")
            else:
                print("¡Squirtle aguanta con muy poca energía!\n")
            input("Enter...\n")
        else:
            hp_squirtle -= ataque_rapido
            print("¡Pikachu usa Ataque Rápido!\n")
            if hp_squirtle > 50:
                print("¡Squirtle ha recibido daño, pero sigue con fuerzas!\n")
            elif hp_squirtle > 40:
                print("¡Squirtle ha recibido daño!\n")
            elif hp_squirtle > 30:
                print("¡Squirtle se siente resentido!\n")
            elif hp_squirtle > 20:
                print("¡Squirtle está debilitado!\n")
            else:
                print("¡Squirtle aguanta con muy poca energía!\n")
            input("Enter...\n")

#Mecánica para comprobar si el squirtle ha muerto :S
if hp_pikachu <= 0:
    print("{} HA GANADO EL COMBATE CON SU SQUIRTLE!".format(entrenador_pokemon.upper()))
    input("Enter para cerrar. Enhorabuena!\n")
else:
    print("EL ENTRENADOR ASH HA GANADO EL COMBATE CON SU PIKACHU!\n")
    input("Enter para cerrar. ¡Suerte la próxima vez!\n")
