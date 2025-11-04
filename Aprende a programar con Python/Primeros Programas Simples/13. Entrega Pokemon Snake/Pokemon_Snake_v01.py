import os
import random
import readchar
from typing import List, Dict, Union
from wcwidth import wcswidth

"""
===================================================================
== NOTA PARA EL CORRECTOR / EJECUCIÓN ==
===================================================================

Este script requiere TRES (3) librerías externas para funcionar.

Asegúrese de instalarlas antes de ejecutar (se recomienda un venv):

    pip install readchar wcwidth

-------------------------------------------------------------------
== NOTA SOBRE LA EVOLUCIÓN DEL CÓDIGO ==

La concepción inicial de este proyecto fue un script sencillo, sin
una estructura formal. Sin embargo, a lo largo de la semana, mi interés
por aplicar nuevas técnicas me llevó a una rápida evolución del código.
Comencé introduciendo funciones para organizar la lógica, pero a medida
que el juego crecía en funcionalidades, la gestión del estado se volvió
cada vez más compleja y difícil de mantener.

Para solucionar este desafío, investigué y decidí aplicar los principios de
la Programación Orientada a Objetos (POO). He reestructurado el código en
varias clases, cada una con una responsabilidad única. Esta decisión está
directamente inspirada en el Principio de Responsabilidad Única (la "S"
de SOLID), un conjunto de reglas de diseño que estoy estudiando para
mejorar la calidad del software:

- `GameState`: Almacena y gestiona todos los datos del juego.
- `Renderer`: Se encarga exclusivamente de dibujar en pantalla.
- `InputHandler`: Gestiona la entrada del teclado.
- `GameLogic`: Contiene las reglas del juego y cómo se actualiza el estado.
- `Game`: Orquesta todo, uniendo las demás clases en el bucle principal.

Además, me apoyé en las advertencias del IDE para refactorizar y simplificar
funciones complejas, aplicando buenas prácticas como `@staticmethod`.

Mi objetivo ha sido aprender a escribir un código más limpio y mantenible.
De forma paralela, estoy aprendiendo a usar un conjunto de herramientas y
metodologías para mejorar mi flujo de trabajo: `git` para el control de
versiones, `agents.md` para la planificación y los principios SOLID para
guiar el diseño, como parte de mi proceso de mejora continua.
-------------------------------------------------------------------
NOTAS DE COMPATIBILIDAD:

1.  Versión de Python:
    Desarrollado y probado en Python 3.12 y 3.13.

2.  Limpieza de Pantalla (cls/clear):
    Trabajo en Windows y macOS, por lo que he implementado una función
    `clear_screen()` que funciona en ambos sistemas operativos
    sin necesidad de modificaciones.

3.  Visualización en Terminal y Emojis:
    El mapa puede verse desalineado en la terminal integrada de algunos
    IDEs. Para una visualización correcta, se recomienda ejecutar el
    script en una terminal nativa (como la Terminal de Windows).
    Asimismo, la apariencia de los emojis puede variar entre Windows y
    macOS debido a las diferencias en las fuentes de cada sistema.

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
PLAYER_EMOJI: str = "🐢"
PORTER_EMOJI: str = "🙎‍♂️"
BOSS_EMOJI: str = "🌟"
ENEMY_GENERIC_EMOJI: str = "⭐"
DEFAULT_TAIL_EMOJI: str = "⚪"


# --- ESTRUCTURAS DE DATOS ---


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


# Datos del portero.
STADIUM_PORTER_NAME: str = "Bruno"
PORTER_DATA: Dict[str, Union[str, int, Dict]] = {"name": STADIUM_PORTER_NAME, "initial_hp": 0, "attacks": {}}


# Mapa de datos de enemigos por clave.
ENEMY_DATA_LOOKUP: Dict[str, Dict] = {
    "BULBASAUR_DATA": BULBASAUR_DATA,
    "CHARMANDER_DATA": CHARMANDER_DATA,
    "PORTERO_DATA": PORTER_DATA,
    "BOSS_EEVEE_DATA": BOSS_EEVEE_DATA
}


# Objetos fijos en el mapa (posición X, posición Y, clave de datos).
FIXED_MAP_OBJECTS: List[List[Union[int, str]]] = [
    [5, 1, "BULBASAUR_DATA"],
    [35, 1, "CHARMANDER_DATA"],
    [20, 17, "PORTERO_DATA"],
    [20, 15, "BOSS_EEVEE_DATA"]
]


# Definición del mapa de obstáculos (árboles).
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


# --- CLASE DE ESTADO DEL JUEGO ---
class GameState:
    """Encapsula todo el estado mutable del juego."""
    def __init__(self):
        """Inicializa todos los atributos para un nuevo estado de juego."""
        self.my_position: List[int] = [20, 18]
        self.tail: List[List[int]] = []
        self.tail_length: int = 0
        self.squirtle_current_hp: int = SQUIRTLE_DATA["initial_hp"]
        self.bands_obtained: int = 0
        self.porter_defeated: bool = False
        self.defeated_enemies_list: List[str] = []
        self.map_objects: List[List[Union[int, str]]] = []
        self.obstacle_definition: List[List[str]] = parse_obstacle_map(OBSTACLE_DEFINITION_RAW)

        # Inicializa los objetos del mapa
        self.generate_map_objects()

    def generate_map_objects(self) -> None:
        """Carga los datos de los entrenadores al mapa de objetos activos."""
        self.map_objects.clear()
        for obj_data in FIXED_MAP_OBJECTS:
            self.map_objects.append([obj_data[2], obj_data[POS_X], obj_data[POS_Y]])

    def reset_game(self) -> None:
        """Reinicia el estado del juego a sus valores iniciales."""
        self.__init__()

    def reset_player_after_defeat(self) -> None:
        """Reinicia solo la posición y la vida del jugador tras una derrota normal."""
        self.my_position = [20, 18]
        self.squirtle_current_hp = SQUIRTLE_DATA["initial_hp"]


# --- CLASE DE GESTIÓN DE ENTRADA ---
class InputHandler:
    """Gestiona la entrada del usuario."""
    @staticmethod
    def get_direction() -> str:
        """Lee un carácter del teclado y lo devuelve en minúsculas."""
        return readchar.readchar().lower()


# --- CLASE DE RENDERIZADO ---
class Renderer:
    """Gestiona todo el dibujado en la pantalla."""

    def render(self, game_state: GameState) -> None:
        """Dibuja el estado actual del juego: mapa, jugador, objetos, etc."""
        clear_screen()
        print("Bienvenido a Pokémon Snake.\n", end="")
        self._draw_border()

        for coordinate_y in range(MAP_HEIGHT):
            print("|", end="")
            for coordinate_x in range(MAP_WIDTH):
                char_to_draw = self._get_cell_char(
                    coordinate_x,
                    coordinate_y,
                    game_state,
                )
                cell_width = wcswidth(char_to_draw)
                padding_needed = 2 - cell_width
                print(f"{char_to_draw}{' ' * padding_needed}", end="")
            print("|")

        self._draw_border()

    @staticmethod
    def _draw_border() -> None:
        """Dibuja la línea de borde superior/inferior."""
        print("+" + "-" * MAP_FRAME_WIDTH + "+")

    def _get_cell_char(self, x: int, y: int, game_state: GameState) -> str:
        """Decide qué carácter dibujar en la celda delegando a métodos auxiliares."""
        position = [x, y]

        # Las comprobaciones se hacen en orden de prioridad de dibujado.
        char = self._get_obstacle_char(position, game_state)
        if char: return char

        char = self._get_stadium_char(position, game_state)
        if char: return char

        char = self._get_map_object_char(position, game_state)
        if char: return char

        char = self._get_tail_char(position, game_state)
        if char: return char

        if position == game_state.my_position:
            return PLAYER_EMOJI

        return "  "  # Celda vacía

    @staticmethod
    def _get_obstacle_char(position: List[int], game_state: GameState) -> Union[str, None]:
        """Devuelve el carácter de obstáculo si corresponde."""
        if game_state.obstacle_definition[position[POS_Y]][position[POS_X]] == "#":
            return "🌳"
        return None

    @staticmethod
    def _get_stadium_char(position: List[int], game_state: GameState) -> Union[str, None]:
        """Devuelve el carácter de la zona del estadio si corresponde."""
        x, y = position
        is_stadium_zone = (y == 17 and 15 <= x <= 25 and game_state.obstacle_definition[y][x] == " ")
        if not is_stadium_zone:
            return None

        if x == 20 and not game_state.porter_defeated:
            return "👑"
        if x == 15 or x == 25:
            return "🏟️"
        return " ═"

    @staticmethod
    def _get_map_object_char(position: List[int], game_state: GameState) -> Union[str, None]:
        """Devuelve el carácter de un objeto del mapa si corresponde."""
        x, y = position
        for data_name, obj_x, obj_y in game_state.map_objects:
            if obj_x != x or obj_y != y:
                continue

            # Objeto encontrado, ahora se determina el emoji.
            enemy_data = ENEMY_DATA_LOOKUP.get(data_name)
            if not enemy_data:
                return ENEMY_GENERIC_EMOJI

            name = enemy_data.get("name", "")
            special_emojis = {
                STADIUM_PORTER_NAME: PORTER_EMOJI,
                BOSS_EEVEE_DATA["name"]: BOSS_EMOJI
            }
            return special_emojis.get(name, ENEMY_GENERIC_EMOJI)

        return None

    @staticmethod
    def _get_tail_char(position: List[int], game_state: GameState) -> Union[str, None]:
        """Devuelve el carácter de la cola si corresponde."""
        x, y = position
        for i, tail_piece in enumerate(game_state.tail):
            if tail_piece[POS_X] == x and tail_piece[POS_Y] == y:
                if i < len(game_state.defeated_enemies_list):
                    return game_state.defeated_enemies_list[i]
                return DEFAULT_TAIL_EMOJI
        return None


# --- CLASE DE LÓGICA DEL JUEGO ---
class GameLogic:
    """Gestiona las reglas y la actualización del estado del juego."""
    def update_state(self, direction: str, game_state: GameState) -> None:
        """
        Actualiza el estado del juego basado en la dirección y las reglas.

        Calcula la nueva posición, valida el movimiento contra obstáculos y el portero,
        y gestiona las interacciones con objetos en el mapa.
        """
        # Calcula la nueva posición.
        new_position = self._compute_new_position(direction, game_state.my_position)

        # Valida y aplica el movimiento.
        if new_position:
            is_obstacle = game_state.obstacle_definition[new_position[POS_Y]][new_position[POS_X]] == "#"

            if self._is_blocked_by_porter(new_position, game_state):
                # Crea un estado temporal solo para el diálogo de bloqueo.
                temp_state = GameState()
                temp_state.my_position = new_position
                temp_state.bands_obtained = game_state.bands_obtained
                handle_porter_interaction(temp_state)
            elif not is_obstacle:
                self._apply_movement(new_position, game_state)

        # Gestiona interacciones en la posición actual.
        handle_porter_interaction(game_state)
        object_to_interact_with = get_object_at_position(game_state.map_objects, game_state.my_position)
        if object_to_interact_with:
            handle_interaction(object_to_interact_with, game_state)

    @staticmethod
    def _compute_new_position(direction: str, my_position: List[int]) -> Union[List[int], None]:
        """Calcula la nueva posición (WASD) con wrap-around."""
        if direction == "w":
            return [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
        if direction == "s":
            return [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
        if direction == "a":
            return [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
        if direction == "d":
            return [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
        return None

    @staticmethod
    def _apply_movement(new_position: List[int], game_state: GameState) -> None:
        """Aplica el movimiento al estado del juego."""
        game_state.tail.insert(0, game_state.my_position.copy())
        game_state.tail = game_state.tail[:game_state.tail_length]
        game_state.my_position = new_position

    @staticmethod
    def _is_blocked_by_porter(new_position: List[int], game_state: GameState) -> bool:
        """Verifica si el movimiento está bloqueado por el portero."""
        porter_position: List[int] = [20, 17]
        return new_position == porter_position and game_state.bands_obtained < 2


# --- CLASE PRINCIPAL DEL JUEGO ---
class Game:
    """Gestiona el flujo principal del juego (bucle, estado, etc.)."""
    def __init__(self, game_state: GameState, input_handler: InputHandler, renderer: Renderer, game_logic: GameLogic):
        """
        Inicializa el coordinador del juego con sus dependencias.

        Args:
            game_state: El objeto que contiene el estado del juego.
            input_handler: El objeto que gestiona la entrada del usuario.
            renderer: El objeto que se encarga de dibujar en pantalla.
            game_logic: El objeto que contiene las reglas del juego.
        """
        self.game_state = game_state
        self.input_handler = input_handler
        self.renderer = renderer
        self.game_logic = game_logic

    def run(self):
        """Inicia y mantiene el bucle principal del juego."""
        while True:
            self.draw()
            direction = self.input_handler.get_direction()
            self.update(direction)

    def draw(self):
        """Delega el dibujado de todos los componentes al renderizador."""
        self.renderer.render(self.game_state)

    def update(self, direction: str):
        """Delega la actualización del estado del juego al manejador de lógica."""
        self.game_logic.update_state(direction, self.game_state)


# --- FUNCIÓN PARA LIMPIAR LA TERMINAL EN MAC(posix) Y WINDOWS(nt) ---
def clear_screen():
    """Limpia la pantalla de la terminal, compatible con Windows y macOS/Linux."""
    
    # Para Windows (NT)
    if os.name == 'nt':
        _ = os.system('cls')
    
    # Para macOS y Linux (POSIX)
    else:
        _ = os.system('clear')

    # Usamos '_ = os.system(...)' para asignar el resultado (que suele ser 0)
    # y evitar que a veces se imprima en la terminal.


# --- FUNCIONES PARA CONVERTIR EL STR DEL MAPA A 2D ---
def parse_obstacle_map(raw_map: str) -> List[List[str]]:
    """Convierte la cadena de texto del mapa en una lista 2D para la lógica de colisión."""
    temp_map = raw_map.split("\n")
    parsed_map = []
    for row in temp_map:
        # Limpia espacios en blanco al final de la línea.
        clean_row: str = row.rstrip()

        # Corta la línea a MAP_WIDTH (por si se pasa).
        truncated_row: str = clean_row[:MAP_WIDTH]

        # Rellena la línea a MAP_WIDTH (por si es corta).
        padded_row: str = truncated_row.ljust(MAP_WIDTH)

        # Añade la lista de caracteres (SIEMPRE de 41).
        parsed_map.append(list(padded_row))
    return parsed_map


# --- FUNCIÓN DE GESTIÓN DE INTERACCIÓN CON EL PORTERO ---
def handle_porter_interaction(game_state: GameState) -> None:
    """Gestiona la interacción y el diálogo con el portero."""
    porter_position: List[int] = [20, 17]

    # Cláusula de guarda: No hacer nada si no estamos en la posición del portero.
    if game_state.my_position != porter_position:
        return

    # Caso 1: El jugador no tiene suficientes bandas.
    if game_state.bands_obtained < 2:
        clear_screen()
        print(f"{PORTER_EMOJI} {STADIUM_PORTER_NAME} (Guardián):")
        print("¡Alto ahí! Necesitas obtener las 2 Bandas de Entrenador para entrar al Estadio.")
        input("\n✅ Enter para continuar...")
        return

    # Caso 2: El jugador puede pasar y el portero aún no ha sido "derrotado".
    if not game_state.porter_defeated:
        clear_screen()
        print(f"{PORTER_EMOJI} {STADIUM_PORTER_NAME}: ¡Adelante, eres digno de enfrentarte a Eevee Oscuro!\n"
              f"¡Se oye el ruido de unos árboles moviéndose!")
        input("\n✅ Enter para entrar al Estadio...")
        # Lógica para eliminar al portero y abrir paso
        for obj in game_state.map_objects:
            if obj[0] == "PORTERO_DATA":
                game_state.map_objects.remove(obj)
                break
        game_state.porter_defeated = True
        game_state.obstacle_definition[16][19] = " "
        game_state.obstacle_definition[16][20] = " "
        game_state.obstacle_definition[16][21] = " "


# --- FUNCIÓN DE BARRAS DE VIDA ---
def render_hp_bars(
    player_name: str,
    player_hp: int,
    player_max_hp: int,
    enemy_name: str,
    enemy_hp: int,
    enemy_max_hp: int,
) -> None:
    """Dibuja las barras de vida para ambos combatientes en la consola."""
    player_hp_bars = int(player_hp * BAR_LENGTH / player_max_hp)
    enemy_hp_bars = int(enemy_hp * BAR_LENGTH / enemy_max_hp)

    print(
        f"La vida de {enemy_name} es de [{'🔶' * enemy_hp_bars}{'🔸' * (BAR_LENGTH - enemy_hp_bars)}]"
        f"({enemy_hp}/{enemy_max_hp})hp."
    )
    print(
        f"La vida de {player_name} es de [{'🔷' * player_hp_bars}{'🔹' * (BAR_LENGTH - player_hp_bars)}]"
        f"({player_hp}/{player_max_hp})hp. \n"
    )


# --- FUNCIÓN DE PANTALLA DE PRESENTACIÓN DEL COMBATE ---
def present_battle(squirtle_data: Dict, enemy_data: Dict) -> None:
    """Muestra la pantalla de presentación del combate."""
    enemy_name = enemy_data["name"]
    enemy_emoji = enemy_data.get("emoji", ENEMY_GENERIC_EMOJI)
    clear_screen()
    print(("⚔️" * 18) + "¡UN COMBATE ESTÁ A PUNTO DE COMENZAR!" + ("⚔️" * 18))
    print(f"{squirtle_data['trainer']} saca a {squirtle_data['name']} {PLAYER_EMOJI}\n                VS\n")
    print(f"  {enemy_data['trainer']} saca a {enemy_name} {enemy_emoji}\nES EL TURNO DE {enemy_name.upper()}! ⚔️\n"
          f"✅ Pulsa Enter para comenzar el combate...")
    input()


# --- FUNCIÓN PARA EL INPUT DEL TURNO DE ATAQUE DEL USUARIO ---
def get_player_attack_choice(squirtle_data: Dict) -> str:
    """Muestra las opciones y gestiona la entrada del usuario para el ataque."""
    print(
        squirtle_data["player_turn_emotes"] + squirtle_data["turn_text"] + squirtle_data["player_turn_emotes"] +
        "🤜 [P]lacaje.\n💦 Pistola [A]gua.\n🫧 [B]urbuja.\n 🤷[N]o hacer nada.\n" + squirtle_data["player_turn_emotes"]
    )

    choice = ""
    while choice not in ["P", "A", "B", "N"]:
        choice = input("Introduce la letra del ataque (🤜[P], 💦[A], 🫧[B] o 🤷[N]): ").strip().upper()
        if choice not in ["P", "A", "B", "N"]:
            print("\nOpción no válida. Solo se admite P, B, A o N.\n")
    return choice


# --- FUNCIÓN PARA EL TURNO DEL ENEMIGO ---
def execute_enemy_turn(squirtle_hp: int, enemy_data: Dict) -> int:
    """Ejecuta la lógica del turno del enemigo y devuelve la nueva vida de Squirtle."""
    clear_screen()
    print(enemy_data["turn_emotes"] + enemy_data["turn_text"] + enemy_data["turn_emotes"])

    enemy_name = enemy_data["name"]
    enemy_attacks_items = list(enemy_data["attacks"].items())
    attack_name_key, enemy_damage = random.choice(enemy_attacks_items)
    attack_name_es = enemy_data["attack_names_es"].get(attack_name_key, attack_name_key)

    if random.randint(1, 10) == 1:
        print(f"\n🌀Pero... ¡¡¡SQUIRTLE ESQUIVÓ EL ATAQUE DE {enemy_name.upper()}!!!💨\n")
    else:
        print(f"¡{enemy_name} usa {attack_name_es.upper()}! Recibes {enemy_damage} de daño.\n")
        squirtle_hp -= enemy_damage
        squirtle_hp = max(squirtle_hp, 0)
        if squirtle_hp > 0:
            print(f"¡Squirtle💦 ha recibido daño, pero sigue con {squirtle_hp}hp!\n")

    return squirtle_hp


# --- FUNCIÓN PARA EL TURNO DEL JUGADOR ---
def execute_player_turn(enemy_hp: int, squirtle_data: Dict, enemy_data: Dict) -> int:
    """Ejecuta la lógica del turno del jugador y devuelve la nueva vida del enemigo."""
    clear_screen()

    attack_choice = get_player_attack_choice(squirtle_data)

    clear_screen()
    print(squirtle_data["player_turn_emotes"] + squirtle_data["turn_text"] + squirtle_data["player_turn_emotes"])

    enemy_name = enemy_data["name"]
    damage_to_enemy = 0

    if random.randint(1, 10) == 1 and attack_choice != "N":
        print(f"🌀 ¡¡¡{enemy_name.upper()} ESQUIVÓ EL ATAQUE!!!💨\n")
    else:
        if attack_choice == "P":
            print("¡Squirtle usa Placaje! 🤜💥\n")
            damage_to_enemy = squirtle_data["attacks"]["tackle"]
        elif attack_choice == "A":
            print("¡Squirtle usa Pistola Agua! 💦💦💦\n")
            damage_to_enemy = squirtle_data["attacks"]["water_gun"]
        elif attack_choice == "B":
            print("¡Squirtle usa Burbuja! 🫧🫧🫧\n")
            damage_to_enemy = squirtle_data["attacks"]["bubble"]
        elif attack_choice == "N":
            print(f"🤷 ¡{squirtle_data['trainer']} decide no hacer nada! 🤷\n")

        if damage_to_enemy > 0:
            enemy_hp -= damage_to_enemy
            enemy_hp = max(enemy_hp, 0)
            print(f"¡{enemy_name} ha recibido {damage_to_enemy} de daño y le quedan {enemy_hp}hp!\n")

    return enemy_hp


# --- FUNCIÓN DE COMBATE ---
def start_battle(
    game_state: GameState,
    enemy_data: Dict,
    object_ref: List[Union[int, str]]
) -> None:
    """
    Ejecuta el bucle de combate y procesa el resultado (victoria/derrota)
    modificando directamente el game_state.
    """
    # Inicialización de estado del combate
    squirtle_hp = game_state.squirtle_current_hp
    squirtle_initial_hp = SQUIRTLE_DATA["initial_hp"]
    enemy_hp = enemy_data["initial_hp"]
    enemy_initial_hp = enemy_data["initial_hp"]
    enemy_name = enemy_data["name"]

    # Pantalla de presentación.
    present_battle(SQUIRTLE_DATA, enemy_data)

    # Bucle principal del combate
    while squirtle_hp > 0 and enemy_hp > 0:
        # --- Turno del Enemigo ---
        squirtle_hp = execute_enemy_turn(squirtle_hp, enemy_data)
        render_hp_bars(
            SQUIRTLE_DATA["name"], squirtle_hp, squirtle_initial_hp,
            enemy_name, enemy_hp, enemy_initial_hp
        )

        if squirtle_hp <= 0:
            print(f"💀 ¡{enemy_name.upper()} HA GANADO EL COMBATE! 💀\n")
            input("🔁 Enter para continuar...")
            game_state.squirtle_current_hp = 0
            process_defeat(game_state, enemy_data)
            return  # Salir de la función de batalla

        input("✅ Enter...")

        # --- Turno del Jugador ---
        enemy_hp = execute_player_turn(enemy_hp, SQUIRTLE_DATA, enemy_data)
        render_hp_bars(
            SQUIRTLE_DATA["name"], squirtle_hp, squirtle_initial_hp,
            enemy_name, enemy_hp, enemy_initial_hp
        )

        if enemy_hp <= 0:
            print(f"🎉🏆 ¡{SQUIRTLE_DATA['trainer'].upper()} HA GANADO EL COMBATE CONTRA {enemy_name.upper()}! 💦️⚔️")
            print("Insertar... 🎵 Música de victoria 🎵")
            input("✅ Enter para volver al mapa. ¡Enhorabuena! 🎉🏆")
            game_state.squirtle_current_hp = squirtle_hp
            process_victory(game_state, enemy_data, object_ref)
            return  # Salir de la función de batalla

        input("\n✅ Enter...")


# --- FUNCIÓN PARA OBTENER UN OBJETO EN UNA POSICIÓN DADA ---
def get_object_at_position(map_objects_local: List[List[Union[int, str]]], position: List[int]):
    """
    Busca un objeto en la lista de objetos del mapa que coincida con la posición dada.

    Args:
        map_objects_local: La lista de objetos activos en el mapa.
        position: La posición [x, y] a comprobar.

    Returns:
        El objeto encontrado o None si no hay ninguno en esa posición.
    """
    for obj in map_objects_local:
        _, obj_x, obj_y = obj
        if obj_x == position[POS_X] and obj_y == position[POS_Y]:
            return obj
    return None


# --- FUNCIONES PARA PROCESAR RESULTADOS DE BATALLA ---
def handle_normal_victory(
    game_state: GameState,
    enemy_data: Dict,
    object_ref: List[Union[int, str]]
) -> None:
    """Actualiza el estado del juego tras una victoria contra un enemigo normal."""
    if object_ref in game_state.map_objects:
        game_state.map_objects.remove(object_ref)
    game_state.defeated_enemies_list.append(enemy_data.get("emoji", DEFAULT_TAIL_EMOJI))
    game_state.tail_length = len(game_state.defeated_enemies_list)
    heal_amount = 70
    game_state.squirtle_current_hp = min(game_state.squirtle_current_hp + heal_amount, SQUIRTLE_DATA["initial_hp"])
    if game_state.bands_obtained < 2:
        game_state.bands_obtained += 1

def handle_final_victory() -> None:
    """Muestra el mensaje de victoria final y cierra el juego."""
    clear_screen()
    print("🌟¡FELICIDADES, HAS DERROTADO A EEVEE OSCURO!🌟")
    print(f"¡{SQUIRTLE_DATA['trainer'].upper()} es ahora el CAMPEÓN DE LA LIGA POKÉMON SNAKE!")
    input("\n🎉 Pulsa Enter para cerrar el juego y celebrar la victoria. 🎉")
    os._exit(0)

def handle_normal_defeat(game_state: GameState, enemy_data: Dict) -> None:
    """Reinicia al jugador tras una derrota contra un enemigo normal."""
    print("💀 GAME OVER 💀\n")
    print(f"¡Has sido derrotado por {enemy_data['name']}!")
    input("Enter para reintentarlo...")
    game_state.reset_player_after_defeat()

def handle_final_defeat(game_state: GameState) -> None:
    """Muestra el mensaje de game over y reinicia el juego completo."""
    print("💀💀 GAME OVER 💀💀\n")
    print(f"¡Eevee Oscuro {BOSS_EMOJI} ha sido demasiado poderoso!")
    input("\nPulsa Enter para reiniciar el juego...")
    game_state.reset_game()


# --- FUNCIÓN PARA PROCESAR VICTORIA ---
def process_victory(
    game_state: GameState,
    enemy_data: Dict,
    object_ref: List[Union[int, str]]
) -> None:
    """Distribuye la lógica de victoria al manejador correspondiente."""
    if enemy_data["name"] == BOSS_EEVEE_DATA["name"]:
        handle_final_victory()
    else:
        handle_normal_victory(game_state, enemy_data, object_ref)


def process_defeat(game_state: GameState, enemy_data: Dict) -> None:
    """Distribuye la lógica de derrota al manejador correspondiente."""
    clear_screen()
    if enemy_data["name"] == BOSS_EEVEE_DATA["name"]:
        handle_final_defeat(game_state)
    else:
        handle_normal_defeat(game_state, enemy_data)


# --- FUNCIÓN PARA LA INTERACCIÓN CON OBJETOS. ---
def handle_interaction(
    object_to_interact_with: List[Union[int, str]],
    game_state: GameState,
) -> None:
    """Gestiona la interacción con objetos, delegando la lógica a otras funciones."""
    data_name_key = object_to_interact_with[0]
    enemy_to_fight = ENEMY_DATA_LOOKUP.get(data_name_key)
    if enemy_to_fight is None:
        return

    # Portero no combativo
    if enemy_to_fight["name"] == STADIUM_PORTER_NAME:
        if object_to_interact_with in game_state.map_objects:
            game_state.map_objects.remove(object_to_interact_with)
        game_state.porter_defeated = True
        game_state.obstacle_definition[16][19] = " "
        game_state.obstacle_definition[16][20] = " "
        game_state.obstacle_definition[16][21] = " "
        input("✅ Enter...")
        return

    # Iniciar combate para cualquier otro objeto
    start_battle(game_state, enemy_to_fight, object_to_interact_with)


# --- BUCLE PRINCIPAL. ---
def main():
    """
    Punto de entrada principal del juego.

    Muestra la introducción, solicita el nombre del entrenador,
    configura las dependencias (estado, entrada, renderizador, lógica)
    e inicia el bucle principal del juego.
    """
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

    # Crea las dependencias.
    initial_game_state = GameState()
    input_handler = InputHandler()
    renderer = Renderer()
    game_logic = GameLogic()

    # Inyecta las dependencias en una nueva instancia del juego y lo ejecuta.
    game = Game(initial_game_state, input_handler, renderer, game_logic)
    game.run()


# Inicialización.
if __name__ == "__main__":
    main()
