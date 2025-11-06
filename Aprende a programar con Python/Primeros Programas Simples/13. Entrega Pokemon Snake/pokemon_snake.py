import os
import random
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Tuple, Union

import readchar
from wcwidth import wcswidth

"""
===================================================================
== Pokémon Snake ==
===================================================================

Juego de Snake con temática Pokémon desarrollado en Python.

-------------------------------------------------------------------
NOTA PARA EL PROFESOR
-------------------------------------------------------------------

1. INSTALACIÓN DE DEPENDENCIAS
    Este script requiere librerías externas. Para instalarlas, ejecuta:
    pip install readchar wcwidth

2. ARQUITECTURA Y PRINCIPIOS DE DISEÑO
    El código está estructurado siguiendo principios de Programación
    Orientada a Objetos (POO) para mejorar su claridad y mantenimiento.

    Cada clase tiene una responsabilidad única (Principio de
    Responsabilidad Única - SOLID):
    - `GameState`: Almacena y gestiona todos los datos del juego.
    - `Renderer`: Se encarga exclusivamente de dibujar en pantalla.
    - `InputHandler`: Gestiona la entrada del teclado.
    - `GameLogic`: Contiene las reglas del juego y cómo se actualiza el estado.
    - `Game`: Orquesta todo, uniendo las demás clases en el bucle principal.

    Además, se han aplicado otros principios de diseño clave:
    - **SoC (Separación de Responsabilidades):** Aísla la lógica (GameLogic)
        del dibujado (Renderer) y el estado (GameState).
    - **DRY (No te repitas):** Centraliza los datos de Pokémon y enemigos
        en estructuras de datos para evitar duplicar información.
    - **KISS (Mantenlo simple):** Prioriza la claridad en algoritmos
        como el cálculo de movimiento del jugador.

3. NOTAS DE COMPATIBILIDAD
    - **Python**: Desarrollado y probado en Python 3.12 y 3.13.
    - **Terminal**: Para una visualización correcta, se recomienda ejecutar
        el script en una terminal nativa (como la Terminal de Windows o
        Terminal.app en macOS), ya que la terminal integrada de algunos
        IDEs puede desalinear el mapa.
    - **Emojis**: La apariencia de los emojis puede variar entre sistemas
        operativos.

4. VALIDACIÓN Y CALIDAD (PROCESO DE DESARROLLO)
    Como complemento al diseño POO (punto 2), la robustez y calidad
    del código fueron validadas rigurosamente en tres niveles:

    1. **Calidad de Estilo (Linter/Formatter):** El código ha pasado
        `ruff` (para formateo y linting), asegurando un estilo
        consistente y corrigiendo errores de formato (ej. E501).

    2. **Calidad de Tipado (Type-Checking):** El código ha pasado
        `mypy` (con la configuración de `pyproject.toml`),
        asegurando la consistencia de los tipos de datos.

    3. **Pruebas Funcionales (pytest):** Se utilizó una suite de `pytest`
        (no adjunta) para validar la lógica central. Esta cubrió:
        - **Pruebas Unitarias**: Movimiento y parsing del mapa.
        - **Pruebas de Integración**: Colisiones y reglas (ej. portero).
        - **Pruebas con Mocking**: Flujo de batalla completo.

===================================================================
"""


# --- ENUMERACIÓN PARA CLAVES DE DATOS ---
class EnemyDataKey(Enum):
    """Claves seguras para identificar datos de enemigos."""

    BULBASAUR = auto()
    CHARMANDER = auto()
    PORTERO = auto()
    BOSS_EEVEE = auto()


# --- CONSTANTES GLOBALES (CONVENCIONES) ---

# Posiciones y Mapa.
POS_X: int = 0
POS_Y: int = 1
MAP_WIDTH: int = 41
MAP_HEIGHT: int = 20
BAR_LENGTH: int = 20
MAP_FRAME_WIDTH: int = MAP_WIDTH * 2

# Reglas del Juego.
REQUIRED_BANDS: int = 2
HEAL_AMOUNT_ON_VICTORY: int = 70

# Estética y Emotes.
PLAYER_EMOJI: str = "🐢"
PORTER_EMOJI: str = "🙎‍♂️"
BOSS_EMOJI: str = "🌟"
ENEMY_GENERIC_EMOJI: str = "⭐"
DEFAULT_TAIL_EMOJI: str = "⚪"

# Mapa de selección de ataques del jugador.
ATTACK_CHOICE_MAP: Dict[str, str] = {"P": "tackle", "A": "water_gun", "B": "bubble"}

# Mapa de emojis para objetos especiales del mapa.
SPECIAL_EMOJI_MAP: Dict[EnemyDataKey, str] = {
    EnemyDataKey.PORTERO: PORTER_EMOJI,
    EnemyDataKey.BOSS_EEVEE: BOSS_EMOJI,
}


# --- ESTRUCTURAS DE DATOS (DATACLASSES) ---


@dataclass
class PokemonData:
    """Estructura para almacenar los datos de un Pokémon o personaje."""

    name: str
    initial_hp: int
    attacks: Dict[str, int] = field(default_factory=dict)
    attack_names_es: Dict[str, str] = field(default_factory=dict)
    trainer: str = ""
    emoji: str = ""
    turn_text: str = ""
    turn_emotes: str = ""
    player_turn_emotes: str = ""  # Específico para el jugador


# Datos de Squirtle (Jugador).
SQUIRTLE_DATA = PokemonData(
    name="Squirtle",
    trainer="Trainer Name Placeholder",  # Se actualiza con el input
    turn_text="⚔️'¡Turno de Squirtle!'💦\n",
    player_turn_emotes="🔻" * 13 + "\n",
    initial_hp=80,
    attacks={"tackle": 11, "water_gun": 13, "bubble": 9},
    attack_names_es={"tackle": "Placaje", "water_gun": "Pistola Agua", "bubble": "Burbuja"},
)

# Datos de los Enemigos Fijos.
BULBASAUR_DATA = PokemonData(
    name="Bulbasaur",
    trainer="Erika",
    emoji="🌿",
    turn_text="🌿'¡Turno de Bulbasaur!'🌿\n",
    turn_emotes="🔹" * 12 + "\n",
    initial_hp=70,
    attacks={"tackle": 8, "vine_whip": 9, "leech_seed": 7},
    attack_names_es={"tackle": "Placaje", "vine_whip": "Látigo Cepa", "leech_seed": "Drenadoras"},
)

CHARMANDER_DATA = PokemonData(
    name="Charmander",
    trainer="Blaine",
    emoji="🔥",
    turn_text="🔥'¡Turno de Charmander!'🔥\n",
    turn_emotes="🔹" * 12 + "\n",
    initial_hp=70,
    attacks={
        "scratch": 7,
        "ember": 10,
        "fire_spin": 8,
    },
    attack_names_es={"scratch": "Arañazo", "ember": "Ascuas", "fire_spin": "Giro Fuego"},
)

BOSS_EEVEE_DATA = PokemonData(
    name="Eevee Oscuro",
    trainer="Gary",
    emoji=BOSS_EMOJI,
    turn_text="💀'¡Turno de Eevee Oscuro!'🌟\n",
    turn_emotes="🔥" * 15 + "\n",
    initial_hp=90,
    attacks={"shadow_ball": 9, "quick_attack": 10, "dark_pulse": 7},
    attack_names_es={
        "shadow_ball": "Bola Sombra",
        "quick_attack": "Ataque Rápido",
        "dark_pulse": "Pulso Oscuro",
    },
)

# Datos del portero.
STADIUM_PORTER_NAME: str = "Bruno"
PORTER_DATA = PokemonData(name=STADIUM_PORTER_NAME, initial_hp=0)


# Mapa de datos de enemigos por clave Enum.
ENEMY_DATA_LOOKUP: Dict[EnemyDataKey, PokemonData] = {
    EnemyDataKey.BULBASAUR: BULBASAUR_DATA,
    EnemyDataKey.CHARMANDER: CHARMANDER_DATA,
    EnemyDataKey.PORTERO: PORTER_DATA,
    EnemyDataKey.BOSS_EEVEE: BOSS_EEVEE_DATA,
}


# Objetos fijos en el mapa (clave de datos Enum, posición X, posición Y).
FIXED_MAP_OBJECTS: List[Tuple[EnemyDataKey, int, int]] = [
    (EnemyDataKey.BULBASAUR, 5, 1),
    (EnemyDataKey.CHARMANDER, 35, 1),
    (EnemyDataKey.PORTERO, 20, 17),
    (EnemyDataKey.BOSS_EEVEE, 20, 15),
]


# --- CLASE DE ESTADO DEL JUEGO ---
class GameState:
    """Encapsula todo el estado mutable del juego."""

    # Definición del mapa de obstáculos (# --> árboles).
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

    def __init__(self):
        """Inicializa todos los atributos para un nuevo estado de juego."""
        self.my_position: List[int] = [20, 18]
        self.tail: List[List[int]] = []
        self.tail_length: int = 0
        self.squirtle_current_hp: int = SQUIRTLE_DATA.initial_hp
        self.bands_obtained: int = 0
        self.porter_defeated: bool = False
        self.map_objects: List[Tuple[EnemyDataKey, int, int]] = []
        self.obstacle_definition: List[List[str]] = self._parse_obstacle_map(
            self.OBSTACLE_DEFINITION_RAW
        )
        self.defeated_enemies_list: List[str] = []  # Añade esta línea

        # Inicializa los objetos del mapa
        self.generate_map_objects()

    @staticmethod
    def _parse_obstacle_map(raw_map: str) -> List[List[str]]:
        """Convierte la cadena de texto del mapa en una lista 2D para la lógica de colisión."""
        temp_map = raw_map.split("\n")
        parsed_map = []
        for row in temp_map:
            clean_row: str = row.rstrip()
            truncated_row: str = clean_row[:MAP_WIDTH]
            padded_row: str = truncated_row.ljust(MAP_WIDTH)
            parsed_map.append(list(padded_row))
        return parsed_map

    def generate_map_objects(self) -> None:
        """Carga los datos de los entrenadores al mapa de objetos activos."""
        self.map_objects.clear()
        for obj_data in FIXED_MAP_OBJECTS:
            self.map_objects.append(obj_data)

    def reset_game(self) -> None:
        """Reinicia el estado del juego a sus valores iniciales."""
        self.my_position = [20, 18]
        self.tail = []
        self.tail_length = 0
        self.squirtle_current_hp = SQUIRTLE_DATA.initial_hp
        self.bands_obtained = 0
        self.porter_defeated = False
        self.map_objects = []
        self.defeated_enemies_list = []

        # Vuelve a generar los objetos del mapa
        self.generate_map_objects()

    def reset_player_after_defeat(self) -> None:
        """Reinicia solo la posición y la vida del jugador tras una derrota normal."""
        self.my_position = [20, 18]
        self.squirtle_current_hp = SQUIRTLE_DATA.initial_hp


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
                char_width = wcswidth(self._get_cell_char(coordinate_x, coordinate_y, game_state))
                padding = " " * (2 - char_width)
                print(self._get_cell_char(coordinate_x, coordinate_y, game_state) + padding, end="")
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
        if char:
            return char

        char = self._get_stadium_char(position, game_state)
        if char:
            return char

        char = self._get_map_object_char(position, game_state)
        if char:
            return char

        char = self._get_tail_char(position, game_state)
        if char:
            return char

        if position == game_state.my_position:
            return PLAYER_EMOJI

        return " "  # Celda vacía

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
        is_in_obstacle_map = game_state.obstacle_definition[y][x] == " "
        is_stadium_zone = y == 17 and 15 <= x <= 25 and is_in_obstacle_map
        if not is_stadium_zone:
            return None
        if x == 20 and not game_state.porter_defeated:
            return "👑"
        if x == 15 or x == 25:
            return "🏟️"
        return "═"

    @staticmethod
    def _get_map_object_char(position: List[int], game_state: GameState) -> Union[str, None]:
        """Devuelve el carácter de un objeto del mapa si corresponde."""
        x, y = position
        for data_key, obj_x, obj_y in game_state.map_objects:
            if obj_x == x and obj_y == y:
                # Usa el mapa de emojis para los especiales, o el genérico si no está.
                return SPECIAL_EMOJI_MAP.get(data_key, ENEMY_GENERIC_EMOJI)
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

    @staticmethod
    def render_hp_bars(
        player_name: str,
        player_hp: int,
        player_max_hp: int,
        enemy_name: str,
        enemy_hp: int,
        enemy_max_hp: int,
    ) -> None:
        """Dibuja las barras de vida para ambos combatientes."""
        player_hp_bars = int(player_hp * BAR_LENGTH / player_max_hp)
        enemy_hp_bars = int(enemy_hp * BAR_LENGTH / enemy_max_hp)

        enemy_bar = f"[{'🔶' * enemy_hp_bars}{'🔸' * (BAR_LENGTH - enemy_hp_bars)}]"
        player_bar = f"[{'🔷' * player_hp_bars}{'🔹' * (BAR_LENGTH - player_hp_bars)}]"

        print(f"La vida de {enemy_name} es de {enemy_bar} ({enemy_hp}/{enemy_max_hp})hp.")
        print(f"La vida de {player_name} es de {player_bar} ({player_hp}/{player_max_hp})hp. \n")


# --- CLASE DE LÓGICA DEL JUEGO ---
class GameLogic:
    """
    Contiene todas las reglas del juego, incluyendo la lógica
    de movimiento, interacciones y combate.
    """

    def __init__(self):
        """Inicializa la lógica del juego y pre-calcula valores necesarios."""
        self.porter_position: List[int] = self._find_porter_position()

    @staticmethod
    def _find_porter_position() -> List[int]:
        """Encuentra la posición del portero a partir de la lista de objetos fijos."""
        for key, x, y in FIXED_MAP_OBJECTS:
            if key == EnemyDataKey.PORTERO:
                return [x, y]
        return [-1, -1]  # Devuelve una posición inválida si no se encuentra.

    def update_state(self, direction: str, game_state: GameState, renderer: Renderer) -> None:
        """
        Actualiza el estado del juego basado en la dirección y las reglas.

        Calcula la nueva posición, valida el movimiento contra obstáculos y el portero,
        y gestiona las interacciones con objetos en el mapa.
        """
        new_position = self._compute_new_position(direction, game_state.my_position)

        if new_position:
            is_obstacle = (
                game_state.obstacle_definition[new_position[POS_Y]][new_position[POS_X]] == "#"
            )

            if self._is_blocked_by_porter(new_position, game_state):
                # No te muevas si el portero te bloquea
                pass
            elif not is_obstacle:
                self._apply_movement(new_position, game_state)

        object_to_interact_with = self._get_object_at_position(
            game_state.map_objects, game_state.my_position
        )
        if object_to_interact_with:
            self._handle_interaction(object_to_interact_with, game_state, renderer)

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
        game_state.tail = game_state.tail[: game_state.tail_length]
        game_state.my_position = new_position

    def _is_blocked_by_porter(self, new_position: List[int], game_state: GameState) -> bool:
        """
        Verifica si el movimiento está bloqueado por el portero.
        Si el jugador no tiene las bandas, muestra un mensaje y bloquea el paso.
        """
        if new_position == self.porter_position and game_state.bands_obtained < REQUIRED_BANDS:
            clear_screen()
            print(f"{PORTER_EMOJI} {STADIUM_PORTER_NAME} (Guardián):")
            print(
                f"¡Alto ahí! Necesitas obtener las {REQUIRED_BANDS} Bandas "
                f"de Entrenador para entrar al Estadio."
            )
            input("\n✅ Pulsa Enter para continuar...")
            return True
        return False

    # --- MÉTODOS DE LÓGICA DE INTERACCIÓN Y COMBATE ---

    def _handle_porter_interaction(self, game_state: GameState) -> None:
        """Gestiona la interacción y el diálogo con el portero."""
        if game_state.my_position != self.porter_position:
            return

        # Solo procedemos si las bandas están obtenidas y el portero no ha sido derrotado.
        if game_state.bands_obtained >= REQUIRED_BANDS and not game_state.porter_defeated:
            clear_screen()
            print(
                f"{PORTER_EMOJI} {STADIUM_PORTER_NAME}: ¡Adelante, eres digno de "
                f"enfrentarte a Eevee Oscuro!\n"
                "¡Mucha suerte, la necesitarás!"
            )
            input("\n✅ Pulsa Enter para entrar al Estadio...")

            # Elimina al portero del mapa de una forma más directa.
            game_state.map_objects = [
                obj for obj in game_state.map_objects if obj[0] != EnemyDataKey.PORTERO
            ]

            game_state.porter_defeated = True
            # Abre el camino en el mapa de obstáculos.
            game_state.obstacle_definition[16][19] = " "
            game_state.obstacle_definition[16][20] = " "
            game_state.obstacle_definition[16][21] = " "

    @staticmethod
    def _present_battle(squirtle_data: PokemonData, enemy_data: PokemonData) -> None:
        """Muestra la pantalla de presentación del combate."""
        clear_screen()
        print("⚔️" * 18)
        print("¡UN COMBATE ESTÁ A PUNTO DE COMENZAR!")
        print("⚔️" * 18)
        print(
            f"{squirtle_data.trainer} saca a {squirtle_data.name} {PLAYER_EMOJI}\n"
            f"                VS\n"
        )
        print(
            f"{enemy_data.trainer} saca a {enemy_data.name} {enemy_data.emoji}\n"
            f"ES EL TURNO DE {enemy_data.name.upper()}! ⚔️\n"
            f"✅ Pulsa Enter para comenzar el combate..."
        )
        input()

    @staticmethod
    def _get_player_attack_choice(squirtle_data: PokemonData) -> str:
        """Muestra las opciones y gestiona la entrada del usuario para el ataque."""
        print(
            squirtle_data.player_turn_emotes
            + squirtle_data.turn_text
            + squirtle_data.player_turn_emotes
            + "🤜 [P]lacaje.\n💦 Pistola [A]gua.\n🫧 [B]urbuja.\n 🤷[N]o hacer nada.\n"
            + squirtle_data.player_turn_emotes
        )
        choice = ""
        while choice not in ["P", "A", "B", "N"]:
            choice = (
                input("Introduce la letra del ataque (🤜[P], 💦[A], 🫧[B] o 🤷[N]): ")
                .strip()
                .upper()
            )
            if choice not in ["P", "A", "B", "N"]:
                print("Opción no válida. Por favor, elige una de las letras indicadas.")
        return choice

    @staticmethod
    def _execute_enemy_turn(squirtle_hp: int, enemy_data: PokemonData) -> int:
        """Ejecuta la lógica del turno del enemigo."""
        clear_screen()
        print(enemy_data.turn_emotes + "\n" + enemy_data.turn_text + "\n" + enemy_data.turn_emotes)
        attack_name_key, enemy_damage = random.choice(list(enemy_data.attacks.items()))
        attack_name_es = enemy_data.attack_names_es.get(attack_name_key, attack_name_key)
        if random.randint(1, 10) == 1:
            print(f"\n🌀Pero... ¡¡¡SQUIRTLE ESQUIVÓ EL ATAQUE DE {enemy_data.name.upper()}!!!💨\n")
        else:
            print(
                f"¡{enemy_data.name} usa {attack_name_es.upper()}! "
                f"Recibes {enemy_damage} de daño.\n"
            )
            squirtle_hp -= enemy_damage
            squirtle_hp = max(squirtle_hp, 0)
        return squirtle_hp

    def _execute_player_turn(
        self, enemy_hp: int, squirtle_data: PokemonData, enemy_data: PokemonData
    ) -> int:
        """Ejecuta la lógica del turno del jugador."""
        clear_screen()
        attack_choice = self._get_player_attack_choice(squirtle_data)
        clear_screen()
        print(
            squirtle_data.player_turn_emotes
            + "\n"
            + squirtle_data.turn_text
            + "\n"
            + squirtle_data.player_turn_emotes
        )

        # Si el enemigo esquiva, termina el turno antes de calcular el daño.
        if random.randint(1, 10) == 1 and attack_choice != "N":
            print(f"🌀 ¡¡¡{enemy_data.name.upper()} ESQUIVÓ EL ATAQUE!!!💨\n")
            return enemy_hp

        damage_to_enemy = 0
        if attack_choice in ATTACK_CHOICE_MAP:
            attack_key = ATTACK_CHOICE_MAP[attack_choice]
            damage_to_enemy = squirtle_data.attacks.get(attack_key, 0)
        elif attack_choice == "N":
            print("¡Squirtle no hace nada! 🤷\n")

        if damage_to_enemy > 0:
            enemy_hp -= damage_to_enemy
            enemy_hp = max(enemy_hp, 0)
            print(f"¡Squirtle ataca! {enemy_data.name} recibe {damage_to_enemy} de daño.\n")

        return enemy_hp

    def _start_battle(
        self,
        game_state: GameState,
        enemy_data: PokemonData,
        object_ref: Tuple[EnemyDataKey, int, int],
        data_key: EnemyDataKey,
        renderer: Renderer,
    ) -> None:
        """Ejecuta el bucle de combate y procesa el resultado."""
        squirtle_hp = game_state.squirtle_current_hp
        enemy_hp = enemy_data.initial_hp
        self._present_battle(SQUIRTLE_DATA, enemy_data)
        while squirtle_hp > 0 and enemy_hp > 0:
            squirtle_hp = self._execute_enemy_turn(squirtle_hp, enemy_data)
            renderer.render_hp_bars(
                SQUIRTLE_DATA.name,
                squirtle_hp,
                SQUIRTLE_DATA.initial_hp,
                enemy_data.name,
                enemy_hp,
                enemy_data.initial_hp,
            )
            if squirtle_hp <= 0:
                break
            input("✅ Enter...")
            enemy_hp = self._execute_player_turn(enemy_hp, SQUIRTLE_DATA, enemy_data)
            renderer.render_hp_bars(
                SQUIRTLE_DATA.name,
                squirtle_hp,
                SQUIRTLE_DATA.initial_hp,
                enemy_data.name,
                enemy_hp,
                enemy_data.initial_hp,
            )
            if enemy_hp <= 0:
                break
            input("\n✅ Enter...")

        game_state.squirtle_current_hp = squirtle_hp
        if squirtle_hp > 0:
            self._process_victory(game_state, enemy_data, object_ref, data_key)
        else:
            self._process_defeat(game_state, enemy_data, data_key)

    @staticmethod
    def _get_object_at_position(
        map_objects_local: List[Tuple[EnemyDataKey, int, int]], position: List[int]
    ) -> Union[Tuple[EnemyDataKey, int, int], None]:
        """Busca un objeto en la lista que coincida con la posición dada."""
        for obj in map_objects_local:
            _, obj_x, obj_y = obj
            if obj_x == position[POS_X] and obj_y == position[POS_Y]:
                return obj
        return None

    @staticmethod
    def _handle_normal_victory(
        game_state: GameState, enemy_data: PokemonData, object_ref: Tuple[EnemyDataKey, int, int]
    ) -> None:
        """Actualiza el estado tras una victoria normal y muestra el mensaje de victoria."""
        clear_screen()
        print(f"🎉 ¡VICTORIA! Has derrotado a {enemy_data.name} ({enemy_data.trainer}) 🎉\n")

        if object_ref in game_state.map_objects:
            game_state.map_objects.remove(object_ref)

        # Añade el emoji del enemigo derrotado a la cola y actualiza su longitud.
        defeated_emoji = enemy_data.emoji or DEFAULT_TAIL_EMOJI
        game_state.defeated_enemies_list.append(defeated_emoji)
        game_state.tail_length = len(game_state.defeated_enemies_list)
        print(f"¡{enemy_data.name} se une a tu equipo como parte de tu cola! {defeated_emoji}\n")

        # Cura al jugador.
        new_hp = game_state.squirtle_current_hp + HEAL_AMOUNT_ON_VICTORY
        game_state.squirtle_current_hp = min(new_hp, SQUIRTLE_DATA.initial_hp)
        print(
            f"Squirtle recupera {HEAL_AMOUNT_ON_VICTORY} HP. Ahora tiene "
            f"{game_state.squirtle_current_hp}/{SQUIRTLE_DATA.initial_hp} HP.\n"
        )

        # Otorga bandas.
        if game_state.bands_obtained < REQUIRED_BANDS:
            game_state.bands_obtained += 1
            print(
                f"¡Has obtenido una Banda de Entrenador! Total: "
                f"{game_state.bands_obtained}/{REQUIRED_BANDS} 🏅\n"
            )
        else:
            print("Ya tienes todas las Bandas de Entrenador necesarias.\n")

        input("✅ Pulsa Enter para volver al mapa...")

    @staticmethod
    def _handle_final_victory() -> None:
        """Muestra el mensaje de victoria final y cierra el juego."""
        clear_screen()
        print("🌟¡FELICIDADES, HAS DERROTADO A EEVEE OSCURO!🌟")
        print(f"¡{SQUIRTLE_DATA.trainer.upper()} es ahora el CAMPEÓN DE LA LIGA POKÉMON SNAKE!")
        input("\n🎉 Pulsa Enter para cerrar el juego y celebrar la victoria. 🎉")
        os._exit(0)

    @staticmethod
    def _handle_normal_defeat(game_state: GameState, enemy_data: PokemonData) -> None:
        """Reinicia al jugador tras una derrota normal."""
        print("💀 GAME OVER 💀\n")
        print(f"¡Has sido derrotado por {enemy_data.name}!")
        input("Enter para reintentarlo...")
        game_state.reset_player_after_defeat()

    @staticmethod
    def _handle_final_defeat(game_state: GameState) -> None:
        """Muestra el mensaje de game over y reinicia el juego completo."""
        print("💀💀 GAME OVER 💀💀\n")
        print(f"¡Eevee Oscuro {BOSS_EMOJI} ha sido demasiado poderoso!")
        input("\nPulsa Enter para reiniciar el juego...")
        game_state.reset_game()

    def _process_victory(
        self,
        game_state: GameState,
        enemy_data: PokemonData,
        object_ref: Tuple[EnemyDataKey, int, int],
        data_key: EnemyDataKey,
    ) -> None:
        """Distribuye la lógica de victoria."""
        if data_key == EnemyDataKey.BOSS_EEVEE:
            self._handle_final_victory()
        else:
            self._handle_normal_victory(game_state, enemy_data, object_ref)

    def _process_defeat(
        self, game_state: GameState, enemy_data: PokemonData, data_key: EnemyDataKey
    ) -> None:
        """Distribuye la lógica de derrota."""
        clear_screen()
        if data_key == EnemyDataKey.BOSS_EEVEE:
            self._handle_final_defeat(game_state)
        else:
            self._handle_normal_defeat(game_state, enemy_data)

    def _handle_interaction(
        self,
        object_to_interact_with: Tuple[EnemyDataKey, int, int],
        game_state: GameState,
        renderer: Renderer,
    ) -> None:
        """Gestiona la interacción con objetos."""
        data_key = object_to_interact_with[0]

        # Comprueba si la interacción es con el portero usando su clave Enum.
        if data_key == EnemyDataKey.PORTERO:
            self._handle_porter_interaction(game_state)
            return

        enemy_to_fight = ENEMY_DATA_LOOKUP.get(data_key)
        if enemy_to_fight:
            self._start_battle(
                game_state, enemy_to_fight, object_to_interact_with, data_key, renderer
            )


# --- CLASE PRINCIPAL DEL JUEGO ---
class Game:
    """Gestiona el flujo principal del juego (bucle, estado, etc.)."""

    def __init__(
        self,
        game_state: GameState,
        input_handler: InputHandler,
        renderer: Renderer,
        game_logic: GameLogic,
    ):
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
        self.game_logic.update_state(direction, self.game_state, self.renderer)


# --- FUNCIÓN DE UTILIDAD: LIMPIAR PANTALLA ---
def clear_screen():
    """Limpia la pantalla de la terminal, compatible con Windows y macOS/Linux."""
    # Para Windows.
    if os.name == "nt":
        _ = os.system("cls")
    # Para macOS y Linux.
    else:
        _ = os.system("clear")


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
    SQUIRTLE_DATA.trainer = my_pokemon_trainer_name

    # Pregunta por el género del entrenador y determina el artículo y el término
    gender_choice: str = ""
    trainer_article: str = ""
    trainer_gender_term: str = ""
    use_neutral_phrasing: bool = False  # Nuevo flag para la frase neutra

    while gender_choice not in ["h", "m", "a"]:
        gender_choice = (
            input("¿Eres 'h' (hombre), 'm' (mujer) o 'a' (prefiero no decirlo)? ").strip().lower()
        )
        if gender_choice == "h":
            trainer_article = "El"
            trainer_gender_term = "entrenador"
        elif gender_choice == "m":
            trainer_article = "La"
            trainer_gender_term = "entrenadora"
        elif gender_choice == "a":
            use_neutral_phrasing = True  # Activa el flag para la frase neutra.
        else:
            print("Opción no válida. Por favor, escribe 'h', 'm' o 'a'.")

    clear_screen()
    print(f"🌟 ¡Bienvenido a la Liga Pokémon Snake, {my_pokemon_trainer_name}! 🌟")
    print(
        f"\nTu misión es guiar a Squirtle {PLAYER_EMOJI} a través del laberinto."
        f"(Con WASD de tu teclado)."
    )
    print(
        f"El objetivo es obtener las"
        f" {REQUIRED_BANDS} Bandas de Entrenador (⭐) y desafiar al Jefe Final (👑) en el Estadio."
    )

    # Usa el artículo y el término de género seleccionados, o una frase neutra.
    if use_neutral_phrasing:
        print(f"\n🧑 ¡{my_pokemon_trainer_name} y su Squirtle comienzan esta aventura!💦\n")
    else:
        print(
            f"\n🧑 ¡{trainer_article} {trainer_gender_term} {my_pokemon_trainer_name} "
            f"con su Squirtle comienzan esta aventura!💦\n"
        )

    input("✅ Pulsa Enter para iniciar el mapa...")
    clear_screen()

    # Crea las dependencias.
    initial_game_state = GameState()
    input_handler = InputHandler()
    renderer = Renderer()
    game_logic = GameLogic()  # Se instancia la clase.

    # Inyecta las dependencias en una nueva instancia del juego y lo ejecuta.
    game = Game(initial_game_state, input_handler, renderer, game_logic)
    game.run()


# Inicialización.
if __name__ == "__main__":
    main()
