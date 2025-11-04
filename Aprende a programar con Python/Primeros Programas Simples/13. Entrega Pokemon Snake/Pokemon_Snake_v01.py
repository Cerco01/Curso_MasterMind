import os
import random
import readchar
from typing import List, Dict, Union, Tuple
from wcwidth import wcswidth

"""
===================================================================
== NOTA PARA EL CORRECTOR / EJECUCIÓN ==
===================================================================

Este script requiere TRES (3) librerías externas para funcionar.

Asegúrese de instalarlas antes de ejecutar (se recomienda un venv):

    pip install readchar wcwidth

-------------------------------------------------------------------
NOTAS DE COMPATIBILIDAD:

1.  Versión de Python: 
    Desarrollado y probado en Python 3.12 y 3.13.

2.  Limpieza de Pantalla (cls/clear):
    Se utiliza una función `clear_screen()` personalizada 
    (en lugar de solo `os.system('cls')`) para que este
    mismo archivo .py funcione en Windows, macOS y Linux
    sin necesidad de modificaciones.

===================================================================
"""

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
PLAYER_EMOJI: str = "🐢"
PORTER_EMOJI: str = "🙎‍♂️"
BOSS_EMOJI: str = "🌟"
ENEMY_GENERIC_EMOJI: str = "⭐"
DEFAULT_TAIL_EMOJI: str = "⚪"


# --- ESTRUCTURAS DE DATOS ---

# Caravana de Pokémon (se usarán en el orden en que se derrotan).
# 1. Bulbasaur (🌿) / 2. Charmander (🔥) / 3. Meowth (😼) / 4. Pikachu (⚡).
POKEMON_CARAVAN_EMOJIS: List[str] = ["🌿", "🔥", "😼", "⚡"]

# Datos de Squirtle (Jugador).
SQUIRTLE_DATA: Dict[str, Union[str, int, Dict]] = {
    "name": "Squirtle",
    "trainer": "Trainer Name Placeholder",  # Se actualiza con el input
    "turn_text": "⚔️'¡Turno de Squirtle!'💦\n",
    "player_turn_emotes": "🔻" * 13 + "\n",
    "initial_hp": 80,
    "attacks": {
        "tackle": 11,
        "water_gun": 13,
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
    "emoji": "🌿",
    "turn_text": "🌿'¡Turno de Bulbasaur!'🌿\n",
    "turn_emotes": "🔹" * 12 + "\n",
    "initial_hp": 70,
    "attacks": {
        "tackle": 8,
        "vine_whip": 9,
        "leech_seed": 7
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
    "emoji": "🔥",
    "turn_text": "🔥'¡Turno de Charmander!'🔥\n",
    "turn_emotes": "🔹" * 12 + "\n",
    "initial_hp": 70,
    "attacks": {
        "scratch": 7,
        "ember": 10,
        "fire_spin": 8,
    },
    "attack_names_es": {
        "scratch": "Arañazo",
        "ember": "Ascuas",
        "fire_spin": "Giro Fuego"
    }

}

BOSS_EEVEE_DATA: Dict[str, Union[str, int, Dict]] = {
    "name": "Eevee Oscuro",
    "trainer": "Gary",
    "emoji": BOSS_EMOJI,
    "turn_text": "💀'¡Turno de Eevee Oscuro!'🌟\n",
    "turn_emotes": "🔥" * 15 + "\n",
    "initial_hp": 90,
    "attacks": {
        "shadow_ball": 9,
        "quick_attack": 10,
        "dark_pulse": 7
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
    [20, 17, "PORTERO_DATA"],
    [20, 15, "BOSS_EEVEE_DATA"]
]

# Diseño del Mapa (Árboles = #).
OBSTACLE_DEFINITION_RAW: str = """\
#########################################
#   #     #########################     #
#   #     #   #######   ###########   ###
#  #     ##########################   # #
#  #     ###########        #######   # #
#  #####   #############  #########    ##
#  #       #########      ###########   #
#  #   # ######################     #   #
#  #       #   #######################  #
#   #  ##########       #########   #   #
#  #     ###################### #   #   #
#     #   # ###    ###############  #   #
#   #    #####       #############  #   #
#  #  #   ######  ################  ##  #
#     #   ########     ######  #   #    #
#  ####     #######   ######  #   ####  #
#  ####   #  ###############  #  ##     #
#  #         ##           ###           #
#     #                         #   #   #
#########################################
"""

# --- VARIABLES DE ESTADO ---
map_objects: List[List[int]] = []
obstacle_definition: List[List[str]] = []
BANDS_OBTAINED: int = 0
PORTER_DEFEATED: bool = False
defeated_enemies_list: List[str] = []

# --- FUNCIÓN PARA MAC(posix)/WINDOWS(nt) ---
def clear_screen():
    """Limpia la pantalla de la terminal, compatible con Windows y macOS/Linux."""
    
    # Para Windows (NT)
    if os.name == 'nt':
        _ = os.system('cls')
    
    # Para macOS y Linux (POSIX)
    else:
        _ = os.system('clear')

    # Nota: Usamos '_ = os.system(...)' para asignar el resultado (que suele ser 0)
    # y evitar que a veces se imprima en la terminal.

# --- FUNCIONES DE UTILIDAD DEL MAPA ---
def parse_obstacle_map(raw_map: str) -> List[List[str]]:
    """Convierte la cadena de texto del mapa en una lista 2D para la lógica de colisión."""
    temp_map = raw_map.split("\n")
    parsed_map = []
    for row in temp_map:
        # Limpia espacios en blanco al final de la línea.
        clean_row: str = row.rstrip()

        # Corta la línea a MAP_WIDTH (por si se pasaba).
        truncated_row: str = clean_row[:MAP_WIDTH]

        # Rellena la línea a MAP_WIDTH (por si era corta).
        padded_row: str = truncated_row.ljust(MAP_WIDTH)

        # Añade la lista de caracteres (ahora SIEMPRE de 41).
        parsed_map.append(list(padded_row))
    return parsed_map

# --- FUNCIÓN PARA CARGAR LOS ENTRENADORES Y EL GUARDIÁN DEL ESTADIO ---
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
            clear_screen()
            print(f"{PORTER_EMOJI} {STADIUM_PORTER_NAME} (Guardián):")
            print("¡Alto ahí! Necesitas obtener las 2 Bandas de Entrenador para entrar al Estadio.")
            input("\n✅ Enter para continuar...")
            clear_screen()
            return True  # Bloqueado
        else:
            # Paso libre.
            clear_screen()
            print(f"{PORTER_EMOJI} {STADIUM_PORTER_NAME}: ¡Adelante, eres digno de enfrentarte a Eevee Oscuro!")
            input("\n✅ Enter para entrar al Estadio...")
            clear_screen()
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

    # --- Obtenemos el emoji del enemigo ---
    enemy_emoji: str = enemy_data.get("emoji", ENEMY_GENERIC_EMOJI)

    # Ataques de Squirtle (Obtenidos de SQUIRTLE_DATA).
    squirtle_tackle: int = SQUIRTLE_DATA["attacks"]["tackle"]
    squirtle_water_gun: int = SQUIRTLE_DATA["attacks"]["water_gun"]
    squirtle_bubble: int = SQUIRTLE_DATA["attacks"]["bubble"]

    # --- Pantalla de presentación del combate ---
    clear_screen()
    print("⚔️" * 18)
    print("¡UN COMBATE ESTÁ A PUNTO DE COMENZAR!")
    print("⚔️" * 18)
    print("\n")
    print(f"  {SQUIRTLE_DATA['trainer']} saca a {SQUIRTLE_DATA['name']} {PLAYER_EMOJI}")
    print("\n                VS\n")
    print(f"  {enemy_data['trainer']} saca a {enemy_name} {enemy_emoji}")
    print("\n")
    print(f"ES EL TURNO DE {enemy_name.upper()}! ⚔️\n")

    input("✅ Pulsa Enter para comenzar el combate...")

    # --- BUCLE DE COMBATE ---
    while enemy_hp > 0 and squirtle_hp > 0:
        clear_screen()

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
        clear_screen()

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

        clear_screen()
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
            clear_screen()

        # --- Comprobar victoria del jugador ---
        if enemy_hp == 0:
            print(f"🎉🏆 ¡{SQUIRTLE_DATA['trainer'].upper()} HA GANADO EL COMBATE CONTRA {enemy_name.upper()}! 💦️⚔️")
            print("Insertar... 🎵 Música de victoria 🎵")
            input("✅ Enter para volver al mapa. ¡Enhorabuena! 🎉🏆")
            return squirtle_hp, "VICTORIA"

    return squirtle_hp, "ERROR"  # Nunca se debería llegar aquí.


# --- FUNCIONES AUXILIARES PARA REFACTORIZAR main() ---

def draw_game_state(
    my_position: List[int],
    tail: List[List[int]],
    squirtle_current_hp: int,
    squirtle_max_hp: int,
    bands_obtained: int,
    tail_length: int,
    obstacle_definition_local: List[List[str]],
    map_objects_local: List[List[Union[int, str]]],
) -> None:
    """Dibuja el mapa y el HUD (HP, Bandas, Puntuación)."""
    clear_screen()
    print("Bienvenido a Pokémon Snake.\n" + "+" + "-" * MAP_FRAME_WIDTH + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw: str = "  "

            # Obstáculos (Árboles 🌳)
            if obstacle_definition_local[coordinate_y][coordinate_x] == "#":
                char_to_draw = "🌳"

            # Dibujo del estadio.
            elif (
                coordinate_y == 17
                and 15 <= coordinate_x <= 25
                and obstacle_definition_local[coordinate_y][coordinate_x] == " "
            ):
                if coordinate_x == 20 and not PORTER_DEFEATED:
                    char_to_draw = "👑"
                elif coordinate_x == 15 or coordinate_x == 25:
                    char_to_draw = "🏟️"
                else:
                    char_to_draw = " ═"

            # Objetos/Enemigos en el mapa.
            is_object = False
            for data_name, obj_x, obj_y in map_objects_local:
                if obj_x == coordinate_x and obj_y == coordinate_y:
                    enemy_data = ENEMY_DATA_LOOKUP.get(data_name)
                    if enemy_data:
                        if enemy_data["name"] == STADIUM_PORTER_NAME:
                            char_to_draw = PORTER_EMOJI
                        elif enemy_data["name"] == BOSS_EEVEE_DATA["name"]:
                            char_to_draw = BOSS_EMOJI
                        else:
                            char_to_draw = ENEMY_GENERIC_EMOJI
                    else:
                        char_to_draw = ENEMY_GENERIC_EMOJI
                    is_object = True
                    break

            # Cola / Tail
            if not is_object:
                for i, tail_piece in enumerate(tail):
                    if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                        if i < len(defeated_enemies_list):
                            char_to_draw = defeated_enemies_list[i]
                        else:
                            char_to_draw = DEFAULT_TAIL_EMOJI
                        break

            # Jugador
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = PLAYER_EMOJI

            cell_width = wcswidth(char_to_draw)
            padding_needed = 2 - cell_width
            print(f"{char_to_draw}{' ' * padding_needed}", end="")

        print("|")

    print("+" + "-" * MAP_FRAME_WIDTH + "+")
    print(
        f"Puntuación: {tail_length} | HP: {squirtle_current_hp}/{squirtle_max_hp} | Bandas: {bands_obtained}"
    )


def get_object_at_position(map_objects_local: List[List[Union[int, str]]], position: List[int]):
    """Devuelve el objeto del mapa en `position` o None si no existe."""
    for obj in map_objects_local:
        data_name, obj_x, obj_y = obj
        if obj_x == position[POS_X] and obj_y == position[POS_Y]:
            return obj
    return None


def handle_interaction(
    object_to_interact_with: List[Union[int, str]],
    my_position: List[int],
    tail_length: int,
    tail: List[List[int]],
    squirtle_current_hp: int,
) -> Tuple[List[int], int, List[List[int]], int]:
    """Procesa la interacción (portero o combate) y devuelve el estado actualizado.

    Devuelve: (my_position, tail_length, tail, squirtle_current_hp)
    """
    global map_objects, BANDS_OBTAINED, PORTER_DEFEATED, defeated_enemies_list, obstacle_definition

    data_name_key = object_to_interact_with[0]
    enemy_to_fight = ENEMY_DATA_LOOKUP.get(data_name_key)
    if enemy_to_fight is None:
        return my_position, tail_length, tail, squirtle_current_hp

    # Portero no combativo
    if enemy_to_fight["name"] == STADIUM_PORTER_NAME:
        if object_to_interact_with in map_objects:
            map_objects.remove(object_to_interact_with)
        PORTER_DEFEATED = True
        print("¡Se oye el ruido de unos árboles moviéndose!")
        obstacle_definition[16][19] = " "
        obstacle_definition[16][20] = " "
        obstacle_definition[16][21] = " "
        input("✅ Enter...")
        return my_position, tail_length, tail, squirtle_current_hp

    # Combate
    squirtle_current_hp, battle_result = start_battle(squirtle_current_hp, enemy_to_fight)

    if battle_result == "VICTORIA":
        # Victoria final
        if enemy_to_fight["name"] == BOSS_EEVEE_DATA["name"]:
            clear_screen()
            print("🌟¡FELICIDADES, HAS DERROTADO A EEVEE OSCURO!🌟")
            print(f"¡{SQUIRTLE_DATA['trainer'].upper()} es ahora el CAMPEÓN DE LA LIGA POKÉMON SNAKE!")
            print(f"Puntuación final: {tail_length}")
            input("\n🎉 Pulsa Enter para cerrar el juego y celebrar la victoria. 🎉")
            os._exit(0)

        # Victoria normal
        if object_to_interact_with in map_objects:
            map_objects.remove(object_to_interact_with)
        defeated_enemies_list.append(enemy_to_fight.get("emoji", DEFAULT_TAIL_EMOJI))
        tail_length = len(defeated_enemies_list)
        HEAL_AMOUNT = 70
        squirtle_current_hp = min(squirtle_current_hp + HEAL_AMOUNT, SQUIRTLE_DATA["initial_hp"])
        if BANDS_OBTAINED < 2:
            BANDS_OBTAINED += 1

    elif battle_result == "DERROTA":
        clear_screen()
        if enemy_to_fight["name"] == BOSS_EEVEE_DATA["name"]:
            print("💀💀 GAME OVER 💀💀\n")
            print(f"¡Eevee Oscuro {BOSS_EMOJI} es sido demasiado poderoso!")
            input("\nPulsa Enter para reiniciar el juego...")
            # Resetear Juego (Posición y Caravana).
            my_position = [20, 18]
            tail_length = 0
            tail = []
            defeated_enemies_list.clear()
            squirtle_current_hp = SQUIRTLE_DATA["initial_hp"]
            BANDS_OBTAINED = 0
            PORTER_DEFEATED = False
            obstacle_definition = parse_obstacle_map(OBSTACLE_DEFINITION_RAW)
            generate_map_objects()
        else:
            print("💀 GAME OVER 💀\n")
            print(f"¡Has sido derrotado por {enemy_to_fight['name']}!")
            input("Enter para reintentarlo...")
            my_position = [20, 18]
            squirtle_current_hp = SQUIRTLE_DATA["initial_hp"]

    return my_position, tail_length, tail, squirtle_current_hp


def compute_new_position(direction: str, my_position: List[int]) -> Union[List[int], None]:
    """Calcula la nueva posición según la dirección (WASD) con wrap-around."""
    if direction == "w":
        return [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
    if direction == "s":
        return [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
    if direction == "a":
        return [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
    if direction == "d":
        return [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
    return None


def apply_movement(
    new_position: Union[List[int], None],
    my_position: List[int],
    tail: List[List[int]],
    tail_length: int,
) -> Tuple[List[int], List[List[int]], int]:
    """Aplica el movimiento si es válido y actualiza la cola/tail.

    Devuelve (my_position, tail, tail_length) actualizados.
    """
    global obstacle_definition, BANDS_OBTAINED

    if new_position is None:
        return my_position, tail, tail_length

    # Bloqueo del portero
    if check_porter_block(new_position, BANDS_OBTAINED):
        return my_position, tail, tail_length

    # Colisión con obstáculos (#)
    if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] == "#":
        return my_position, tail, tail_length

    # Movimiento válido
    tail.insert(0, my_position.copy())
    tail = tail[:tail_length]
    my_position = new_position
    return my_position, tail, tail_length


# --- BUCLE PRINCIPAL (REFACTORIZADO) ---

def main():
    # Variables de estado que cambian
    global obstacle_definition, BANDS_OBTAINED, map_objects, PORTER_DEFEATED, defeated_enemies_list

    # Inicialización de Variables de Estado.
    my_position: List[int] = [20, 18]  # [X, Y]
    tail_length: int = 0
    tail: List[List[int]] = []

    # Variables de Squirtle (inicializadas).
    squirtle_current_hp: int = SQUIRTLE_DATA["initial_hp"]

    # Pre-cálculos.
    obstacle_definition = parse_obstacle_map(OBSTACLE_DEFINITION_RAW)
    generate_map_objects()

    # Secuencia de Inicio (Arte, nombre, instrucciones)
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
    clear_screen()

    my_pokemon_trainer_name: str = input("🧑 ¿Cual es el nombre del entrenador Pokemon de hoy?\n\n")
    SQUIRTLE_DATA["trainer"] = my_pokemon_trainer_name

    clear_screen()
    print(f"🌟 ¡Bienvenido a la Liga Pokémon Snake, {my_pokemon_trainer_name}! 🌟")
    print(f"\nTu misión es guiar a Squirtle {PLAYER_EMOJI} a través del laberinto. (Con WASD de tu teclado).")
    print("El objetivo es obtener las 2 Bandas de Entrenador (⭐) y desafiar al Jefe Final (👑) en el Estadio.")
    print(f"\n🧑 ¡{my_pokemon_trainer_name} con su Squirtle comienzan esta aventura!💦\n")

    input("✅ Pulsa Enter para iniciar el mapa...")
    clear_screen()

    # Bucle principal: delega responsabilidades en helpers para mantener main simple.
    while True:
        draw_game_state(
            my_position,
            tail,
            squirtle_current_hp,
            SQUIRTLE_DATA["initial_hp"],
            BANDS_OBTAINED,
            tail_length,
            obstacle_definition,
            map_objects,
        )

        # Lectura de dirección y cálculo de nueva posición
        direction: str = readchar.readchar().lower()
        new_position: Union[List[int], None] = None

        # compute_new_position se encarga de calcular la nueva posición según la dirección.
        new_position = compute_new_position(direction, my_position)

        # Aplicar movimiento
        my_position, tail, tail_length = apply_movement(new_position, my_position, tail, tail_length)

        # Interacción con objetos
        object_to_interact_with = get_object_at_position(map_objects, my_position)
        if object_to_interact_with:
            my_position, tail_length, tail, squirtle_current_hp = handle_interaction(
                object_to_interact_with, my_position, tail_length, tail, squirtle_current_hp
            )


# Inicialización.
if __name__ == "__main__":
    main()
