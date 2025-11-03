import os
import random
from typing import Dict, List, Tuple, Union, cast

import readchar
from wcwidth import wcswidth

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
POKEMON_CARAVAN_EMOJI
