import os
import random
import readchar
from typing import List, Dict, Union, Tuple

# --- CONSTANTES GLOBALES (CONVENCIONES) ---

# Posiciones y Mapa.
POS_X: int = 0
POS_Y: int = 1
MAP_WIDTH: int = 41
MAP_HEIGHT: int = 20
BAR_LENGTH: int = 20
MAP_FRAME_WIDTH: int = MAP_WIDTH * 2

# Estética y Emotes.
TITLE: str = "⚔️¡Un combate Pokémon comienza!⚔️"
PLAYER_EMOJI: str = "🐢 "
PORTER_EMOJI: str = "🙎‍♂️"
BOSS_EMOJI: str = "🌟"
ENEMY_GENERIC_EMOJI: str = "⭐"
DEFAULT_TAIL_EMOJI: str = "⚪ "

# --- ESTRUCTURAS DE DATOS ---

# Caravana de Pokémon (se usarán en el orden en que se derrotan).
# 1. Bulbasaur (🌿) / 2. Charmander (🔥) / 3. Meowth (😼) / 4. Pikachu (⚡).
POKEMON_CARAVAN_EMOJIS: List[str] = ["🌿 ", "🔥 ", "😼 ", "⚡ "]

# Datos de Squirtle (Jugador).
SQUIRTLE_DATA: Dict[str, Union[str, int, Dict]] = {
    "name": "Squirtle",
    "trainer": "Trainer Name Placeholder",  # Se actualiza con el input
    "turn_text": "⚔️'¡Turno de Squirtle!'💦 + \n",
    "player_turn_emotes": "🔻" * 13 + "\n",
    "initial_hp": 70,
    "attacks": {
        "tackle": 10,
        "water_gun": 12,
        "bubble": 9
    },
"attack_names_es": {
        "tackle": "Placaje",
        "water_gun": "Pistola Agua",
        "bubble": "Burbuja"
    }
}

# Datos de los Enemigos Fijos.
BULBASAUR_DATA: Dict[str, Union[str, int, Dict]] = {
    "name": "Bulbasaur",
    "trainer": "Erika",
    "turn_text": "🌿'¡Turno de Bulbasaur!'🌿 + \n",
    "turn_emotes": "🔹" * 12 + "\n",
    "initial_hp": 75,
    "attacks": {
        "tackle": 10,
        "vine_whip": 11,
        "leech_seed": 8
    },
    "attack_names_es": {
        "tackle": "Placaje",
        "vine_whip": "Látigo Cepa",
        "leech_seed": "Drenadoras"
    }

}

CHARMANDER_DATA: Dict[str, Union[str, int, Dict]] = {
    "name": "Charmander",
    "trainer": "Blaine",
    "turn_text": "🔥'¡Turno de Charmander!'🔥 + \n",
    "turn_emotes": "🔹" * 12 + "\n",
    "initial_hp": 80,
    "attacks": {
        "scratch": 10,
        "ember": 10,
        "fire_spin": 9,
    },
    "attack_names_es": {
        "scratch": "Arañazo",
        "ember": "Ascuas",
        "fire_spin": "Giro Fuego"
    }

}

BOSS_EEVEE_DATA: Dict[str, Union[str, int, Dict]] = {
    "name": "Eevee Oscuro",
    "trainer": "Gary (Archienemigo)",
    "turn_text": "💀'¡Turno de Eevee Oscuro!'🌟 + \n",
    "turn_emotes": "🔥" * 15 + "\n",
    "initial_hp": 90,
    "attacks": {
        "shadow_ball": 10,
        "quick_attack": 12,
        "dark_pulse": 8
    },
    "attack_names_es": {
        "shadow_ball": "Bola Sombra",
        "quick_attack": "Ataque Rápido",
        "dark_pulse": "Pulso Oscuro"
    }
}

# --- MAPEO Y UTILIDAD ---

STADIUM_PORTER_NAME: str = "Bruno"

# El Portero (NPC) y otros datos que no luchan.
PORTER_DATA: Dict[str, Union[str, int, Dict]] = {"name": STADIUM_PORTER_NAME, "initial_hp": 0, "attacks": {}}
PIKACHU_DATA: Dict[str, Union[str, int, Dict]] = {"name": "Pikachu (Fallback)", "initial_hp": 70, "attacks": {"a": 10}}

# Mapeo de datos.
ENEMY_DATA_LOOKUP: Dict[str, Dict] = {
    "BULBASAUR_DATA": BULBASAUR_DATA,
    "CHARMANDER_DATA": CHARMANDER_DATA,
    "PORTERO_DATA": PORTER_DATA,
    "BOSS_EEVEE_DATA": BOSS_EEVEE_DATA
}

# Coordenadas [X, Y, Tipo_de_Objeto/Pokemon].
FIXED_MAP_OBJECTS: List[List[Union[int, str]]] = [
    [5, 1, "BULBASAUR_DATA"],
    [35, 1, "CHARMANDER_DATA"],
    [20, 17, "PORTERO_DATA"]
]

# Diseño del Mapa (Árboles = #).
OBSTACLE_DEFINITION_RAW: str = """\
#########################################
#       # ######################### #   #
# ##### # ####################### # #####
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# #   # # ################### # # #   # #
# ####### ####################### # #####
# #       # ###           ######### #   #
##                                     ##
#########################################\
"""

# --- VARIABLES DE ESTADO ---
map_objects: List[List[int]] = []
obstacle_definition: List[List[str]] = []
BANDS_OBTAINED: int = 0


# --- FUNCIONES DE UTILIDAD DEL MAPA ---
def parse_obstacle_map(raw_map: str) -> List[List[str]]:
    """Convierte la cadena de texto del mapa en una lista 2D para la lógica de colisión."""
    temp_map = raw_map.split("\n")
    parsed_map = []
    for row in temp_map:
        # 1. Limpia espacios en blanco al final de la línea.
        clean_row: str = row.rstrip()

        # 2. Corta la línea a MAP_WIDTH (por si se pasaba).
        truncated_row: str = clean_row[:MAP_WIDTH]

        # 3. Rellena la línea a MAP_WIDTH (por si era corta).
        padded_row: str = truncated_row.ljust(MAP_WIDTH)

        # 4. Añade la lista de caracteres (ahora SIEMPRE de 41).
        parsed_map.append(list(padded_row))
    return parsed_map

# --- FUNCION PARA CARGAR LOS ENTRENADORES Y EL GUARDIÁN DEL ESTADIO ---
def generate_map_objects() -> None:
    """Carga los datos (Tipo y Posición) de los entrenadores y el Guardián al mapa de objetos activos."""
    global map_objects

    map_objects.clear()

    # Iteramos sobre la lista fija y añadimos el tipo de data, y la coordenada [X, Y].
    for obj_data in FIXED_MAP_OBJECTS:
        # [Data_Name, POS_X, POS_Y]
        map_objects.append([obj_data[2], obj_data[POS_X], obj_data[POS_Y]])

# --- FUNCIÓN DE UTILIDAD DEL JUEGO ---
def check_porter_block(new_position: List[int], bands_obtained: int) -> bool:
    """Verifica si la nueva posición es la del portero y maneja el diálogo/bloqueo.
    Devuelve True si el movimiento debe ser bloqueado, False si no hay interacción o si pasa."""

    PORTER_POSITION: List[int] = [20, 17]

    if new_position == PORTER_POSITION:
        if bands_obtained < 2:
            # Bloqueo.
            os.system("cls")
            print(f"{PORTER_EMOJI} {STADIUM_PORTER_NAME} (Guardián):")
            print("¡Alto ahí! Necesitas obtener las 2 Bandas de Entrenador para entrar al Estadio.")
            input("\n✅ Enter para continuar...")
            os.system("cls")
            return True  # Bloqueado
        else:
            # Paso libre.
            os.system("cls")
            print(f"{PORTER_EMOJI} {STADIUM_PORTER_NAME}: ¡Adelante, eres digno de enfrentarte a Eevee Oscuro!")
            input("\n✅ Enter para entrar al Estadio...")
            os.system("cls")
            # No bloqueado.
            return False

    return False


# --- FUNCIÓN DE COMBATE ---

def start_battle(squirtle_current_hp: int, enemy_data: Dict) -> Tuple[int, str]:
    """
    Ejecuta el bucle de combate entre Squirtle y un enemigo universal.
    Devuelve la HP final de Squirtle y el resultado del combate.
    """
    squirtle_hp: int = squirtle_current_hp
    squirtle_initial_hp: int = SQUIRTLE_DATA["initial_hp"]

    enemy_name: str = enemy_data["name"]
    enemy_initial_hp: int = enemy_data["initial_hp"]
    enemy_hp: int = enemy_data["initial_hp"]
    enemy_turn_text: str = enemy_data["turn_text"]
    enemy_turn_emotes: str = enemy_data["turn_emotes"]

    # Ataques de Squirtle (Obtenidos de SQUIRTLE_DATA).
    squirtle_tackle: int = SQUIRTLE_DATA["attacks"]["tackle"]
    squirtle_water_gun: int = SQUIRTLE_DATA["attacks"]["water_gun"]
    squirtle_bubble: int = SQUIRTLE_DATA["attacks"]["bubble"]

    # --- BUCLE DE COMBATE ---
    while enemy_hp > 0 and squirtle_hp > 0:
        os.system("cls")

        # --------------------------------------------- Turno CPU (Enemigo). -------------------------------------------


        print(enemy_data["turn_emotes"] + enemy_data["turn_text"] + enemy_data["turn_emotes"])

        # MODIFICACIÓN: Obtener nombre clave (inglés) y daño (int)
        enemy_attacks_items: List[Tuple[str, int]] = list(enemy_data["attacks"].items())
        attack_name_key, enemy_damage = random.choice(enemy_attacks_items)

        # Obtener la traducción en español. Fallback al inglés si no encuentra la traducción.
        attack_name_es: str = enemy_data["attack_names_es"].get(attack_name_key,
                                                                attack_name_key)

        squirtle_dodge_roll: int = random.randint(1, 10)

        if squirtle_dodge_roll == 1:
            print(f"\n🌀Pero... ¡¡¡SQUIRTLE ESQUIVÓ EL ATAQUE DE {enemy_name.upper()}!!!💨\n")

        else:
            # MODIFICACIÓN: Imprimir el nombre del ataque en ESPAÑOL
            print(f"¡{enemy_name} usa {attack_name_es.upper()}! Recibes {enemy_damage} de daño.\n")
            squirtle_hp -= enemy_damage
            squirtle_hp = max(squirtle_hp, 0)

            if squirtle_hp > 0:
                print(f"¡Squirtle💦 ha recibido daño, pero sigue con {squirtle_hp}hp!\n")

        # ... (el resto del turno de la CPU sigue igual) ...

        # Dibujar Barras de Vida.
        enemy_hp_bars: int = int(enemy_hp * BAR_LENGTH / enemy_initial_hp)
        squirtle_hp_bars: int = int(squirtle_hp * BAR_LENGTH / squirtle_initial_hp)

        print(
            f"La vida de {enemy_name} es de [{"🔶" * enemy_hp_bars}{"🔸" * (BAR_LENGTH - enemy_hp_bars)}]"
            f"({enemy_hp}/{enemy_initial_hp})hp.")
        print(
            f"La vida de Squirtle es de [{"🔷" * squirtle_hp_bars}{"🔹" * (BAR_LENGTH - squirtle_hp_bars)}]"
            f"({squirtle_hp}/{squirtle_initial_hp})hp. \n")

        input("✅ Enter...")
        os.system("cls")

        # --- Comprobar derrota del jugador ---
        if squirtle_hp == 0:
            print(f"💀 ¡{enemy_name.upper()} HA GANADO EL COMBATE! 💀\n")
            input("🔁 Enter para continuar (Squirtle ha perdido HP).")
            return 0, "DERROTA"

        # ------------------------------------------- Turno Squirtle (Usuario). ----------------------------------------

        # Título del turno de ataque del Usuario.
        print(SQUIRTLE_DATA["player_turn_emotes"] + SQUIRTLE_DATA["turn_text"] + SQUIRTLE_DATA["player_turn_emotes"] +
              "🤜 [P]lacaje.\n💦 Pistola [A]gua.\n🫧 [B]urbuja.\n 🤷[N]o hacer nada.\n" + SQUIRTLE_DATA[
                  "player_turn_emotes"])

        # Input y selección del ataque del Usuario.
        squirtle_attack_input: str = (input("Introduce la letra del ataque (🤜[P], 💦[A], 🫧[B] o 🤷[N]): ")
                                                                                                    .strip().upper())

        while squirtle_attack_input not in ["P", "A", "B", "N"]:
            print("\nOpción no válida. Solo se admite P, B, A o N.\n")
            squirtle_attack_input = (input("Introduce la letra del ataque (🤜[P], 💦[A], 🫧[B] o 🤷[N]): ")
                                                                                                    .strip().upper())

        os.system("cls")
        print(SQUIRTLE_DATA["player_turn_emotes"] + SQUIRTLE_DATA["turn_text"] + SQUIRTLE_DATA["player_turn_emotes"])

        # Mecánica 10% probabilidad de esquivar del enemigo.
        enemy_dodge_roll: int = random.randint(1, 10)
        damage_to_enemy: int = 0

        if enemy_dodge_roll == 1 and squirtle_attack_input != "N":
            # Enemigo esquiva.
            print(f"🌀 ¡¡¡{enemy_name.upper()} ESQUIVÓ EL ATAQUE!!!💨\n")

        else:
            # Cálculo de daño de Squirtle.
            if squirtle_attack_input == "P":
                print("¡Squirtle usa Placaje! 🤜💥\n")
                damage_to_enemy = squirtle_tackle
            elif squirtle_attack_input == "A":
                print("¡Squirtle usa Pistola Agua! 💦💦💦\n")
                damage_to_enemy = squirtle_water_gun
            elif squirtle_attack_input == "B":
                print("¡Squirtle usa Burbuja! 🫧🫧🫧\n")
                damage_to_enemy = squirtle_bubble
            elif squirtle_attack_input == "N":
                print(f"🤷 ¡{SQUIRTLE_DATA['trainer']} decide no hacer nada! 🤷\n")
                damage_to_enemy = 0

            # Aplicar daño al enemigo.
            if damage_to_enemy > 0:
                enemy_hp -= damage_to_enemy
                enemy_hp = max(enemy_hp, 0)
                print(f"¡{enemy_name} ha recibido {damage_to_enemy} de daño y le quedan {enemy_hp}hp!\n")

            if damage_to_enemy == 0 and squirtle_attack_input != "N":
                print(f"¡{enemy_name} no ha recibido daño!")

            # Barra de vida.
            enemy_hp_bars: int = int(enemy_hp * BAR_LENGTH / enemy_initial_hp)
            squirtle_hp_bars: int = int(squirtle_hp * BAR_LENGTH / squirtle_initial_hp)

            print(
                f"La vida de {enemy_name} es de [{"🔶" * enemy_hp_bars}{"🔸" * (BAR_LENGTH - enemy_hp_bars)}]"
                f"({enemy_hp}/{enemy_initial_hp})hp.")
            print(
                f"La vida de Squirtle es de [{"🔷" * squirtle_hp_bars}{"🔹" * (BAR_LENGTH - squirtle_hp_bars)}]"
                f"({squirtle_hp}/{squirtle_initial_hp})hp. \n")

            input("\n✅ Enter...")
            os.system("cls")

        # --- Comprobar victoria del jugador ---
        if enemy_hp == 0:
            print(f"🎉🏆 ¡{SQUIRTLE_DATA['trainer'].upper()} HA GANADO EL COMBATE CONTRA {enemy_name.upper()}! 💦️⚔️")
            print("Insertar... 🎵 Música de victoria 🎵")
            input("✅ Enter para volver al mapa. ¡Enhorabuena! 🎉🏆")
            return squirtle_hp, "VICTORIA"

    return squirtle_hp, "ERROR"  # Nunca se debería llegar aquí.


# --- BUCLE PRINCIPAL ---

def main():
    # Variables de estado que cambian
    global obstacle_definition, BANDS_OBTAINED, map_objects

    # Inicialización de Variables de Estado.
    my_position: List[int] = [20, 18]  # [X, Y]
    tail_length: int = 0
    tail: List[List[int]] = []
    last_direction: str = ""

    # Variables de Squirtle (inicializadas).
    squirtle_current_hp: int = SQUIRTLE_DATA["initial_hp"]

    # Pre-cálculos.
    obstacle_definition = parse_obstacle_map(OBSTACLE_DEFINITION_RAW)
    generate_map_objects()

    # Secuencia de Inicio.

    # Arte ASCII
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

    # Asignación de Nombre e Introducción.
    my_pokemon_trainer_name: str = input("🧑 ¿Cual es el nombre del entrenador Pokemon de hoy?\n\n")
    SQUIRTLE_DATA["trainer"] = my_pokemon_trainer_name

    os.system("cls")

    # Contexto e Instrucciones.
    print(f"🌟 ¡Bienvenido a la Liga Pokémon Snake, {my_pokemon_trainer_name}! 🌟")
    print(f"\nTu misión es guiar a Squirtle{PLAYER_EMOJI} a través del laberinto. (Con WASD de tu teclado).")
    print("El objetivo es obtener las 2 Bandas de Entrenador (⭐) y desafiar al Jefe Final (👑) en el Estadio.")
    print(f"\n🧑 ¡{my_pokemon_trainer_name} con su Squirtle comienzan esta aventura!💦\n")

    input("✅ Pulsa Enter para iniciar el mapa...")
    os.system("cls")

    # Main Loop.
    while True:

        # --- Dibujado del Mapa ---
        os.system("cls")
        print("Bienvenido a Pokémon Snake.\n" + "+" + "-" * MAP_FRAME_WIDTH + "+")

        for coordinate_y in range(MAP_HEIGHT):
            print("|", end="")

            for coordinate_x in range(MAP_WIDTH):
                char_to_draw: str = "  "

                # Obstacles (Árboles 🌳).
                if obstacle_definition[coordinate_y][coordinate_x] == "#":
                    char_to_draw = "🌳 "

                # Dibujo del estadio.
                elif coordinate_y == 17 and 15 <= coordinate_x <= 25 and obstacle_definition[coordinate_y][
                    coordinate_x] == " ":
                    if coordinate_x == 20:
                        char_to_draw = "👑"
                    elif coordinate_x == 15 or coordinate_x == 25:
                        char_to_draw = "🏟️"
                    else:
                        char_to_draw = " ═"

                # Enemigos (NPCs, Jefe).
                is_object: bool = False
                for data_name, obj_x, obj_y in map_objects:
                    if obj_x == coordinate_x and obj_y == coordinate_y:
                        # Obtener el diccionario de datos usando el nombre.
                        enemy_data_name: str = ENEMY_DATA_LOOKUP[data_name]["name"]
                        if enemy_data_name == STADIUM_PORTER_NAME:
                            char_to_draw = PORTER_EMOJI
                        elif enemy_data_name == BOSS_EEVEE_DATA["name"]:
                            char_to_draw = BOSS_EMOJI
                        else:
                            char_to_draw = ENEMY_GENERIC_EMOJI
                        is_object = True
                        break

                # Tail (Caravana de Pokémon).
                if not is_object:
                    for i, tail_piece in enumerate(tail):
                        if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                            if i < len(POKEMON_CARAVAN_EMOJIS):
                                char_to_draw = POKEMON_CARAVAN_EMOJIS[i]
                            else:
                                char_to_draw = DEFAULT_TAIL_EMOJI
                            break

                # Squirtle (🐢).
                if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                    char_to_draw = PLAYER_EMOJI

                print(f"{char_to_draw}", end="")

            print("|")

        print("+" + "-" * MAP_FRAME_WIDTH + "+")
        print(
            f"Puntuación: {tail_length} | HP: {squirtle_current_hp}/{SQUIRTLE_DATA['initial_hp']} "
            f"| Bandas: {BANDS_OBTAINED}")

        # --- Input y Cálculo de Movimiento ---
        direction: str = readchar.readchar().lower()
        new_position: Union[List[int], None] = None

        # Calcular nueva posición con Wrap-Around.
        if direction == "w":
            new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
        elif direction == "s":
            new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
        elif direction == "a":
            new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
        elif direction == "d":
            new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
        elif direction == "q":
            break

        # Restricción de 180 grados (Solo si tiene cola).
        if new_position and tail_length > 0:
            is_opposite_move: bool = (direction == "w" and last_direction == "s") or \
                                     (direction == "s" and last_direction == "w") or \
                                     (direction == "a" and last_direction == "d") or \
                                     (direction == "d" and last_direction == "a")
            if is_opposite_move:
                new_position = None

        # --- Lógica de Bloqueo del Guardián ---
        if new_position:
            if check_porter_block(new_position, BANDS_OBTAINED):
                new_position = None  # Bloquea el movimiento si la función devuelve True.

        # --- Ejecución Final de Movimiento ---
        if new_position:
            # Checkea colisión con pared (Obstáculos #).
            if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
                last_direction = direction

                # Lógica de movimiento (actualizar cola).
                tail.insert(0, my_position.copy())
                tail = tail[:tail_length]
                my_position = new_position

        # --- Lógica de Combate y Progresión ---
        # Buscamos si la posición de Squirtle está en la lista de objetos.
        object_to_interact_with: Union[List[Union[int, str]], None] = None

        # Iteramos sobre los objetos activos buscando una coincidencia de posición.
        for i, obj in enumerate(map_objects):
            data_name, obj_x, obj_y = obj
            if obj_x == my_position[POS_X] and obj_y == my_position[POS_Y]:
                object_to_interact_with = obj
                break

        if object_to_interact_with:
            # Obtener el diccionario de datos del objeto colisionado.
            data_name_key = object_to_interact_with[0]
            enemy_to_fight: Dict = ENEMY_DATA_LOOKUP[data_name_key]

            # --- Manejo Especial del Portero (No-Combate) ---
            if enemy_to_fight["name"] == STADIUM_PORTER_NAME:
                # Quitar al portero del mapa para que no vuelva a colisionar con él.
                map_objects.remove(object_to_interact_with)

            else:
                # Llamar al combate.
                squirtle_current_hp, battle_result = start_battle(squirtle_current_hp, enemy_to_fight)

                # Lógica de Victoria.
                if battle_result == "VICTORIA":

                    # Comprobación de Victoria Final.
                    if enemy_to_fight["name"] == BOSS_EEVEE_DATA["name"]:
                        os.system("cls")
                        print("🌟¡FELICIDADES, HAS DERROTADO A EEVEE OSCURO!🌟")
                        print(f"¡{SQUIRTLE_DATA['trainer'].upper()} es ahora el CAMPEÓN DE LA LIGA POKÉMON SNAKE!")
                        print(f"Puntuación final: {tail_length}")
                        input("\n🎉 Pulsa Enter para cerrar el juego y celebrar la victoria. 🎉")
                        os._exit(0)

                    # Victoria Normal (Ganar Banda/Crecer).
                    else:
                        map_objects.remove(object_to_interact_with)
                        tail_length += 1

                        # --- MECÁNICA DE CURACIÓN ---
                        # Recupera 70 puntos de vida al ganar, sin exceder el máximo.
                        HEAL_AMOUNT = 70
                        squirtle_current_hp = min(squirtle_current_hp + HEAL_AMOUNT, SQUIRTLE_DATA["initial_hp"])

                        # Ganar banda.
                        if BANDS_OBTAINED < 2:
                            BANDS_OBTAINED += 1

                # Lógica de Derrota (Game Over y Reinicio de mapa con Persistencia).
                elif battle_result == "DERROTA":
                    os.system("cls")
                    print(f"💀 GAME OVER 💀\n")

                    input("Enter para reiniciar el juego...")

                    # Resetear estado de Snake.
                    my_position = [20, 18]
                    tail_length = 0
                    tail = []

                    # Resetear vida (Persistencia de la progresión).
                    squirtle_current_hp = SQUIRTLE_DATA["initial_hp"]


# Inicialización.
if __name__ == "__main__":
    main()