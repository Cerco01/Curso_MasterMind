# file: tests/test_game_logic.py
import pytest

# (Anotación) Importamos las clases y constantes que necesitamos
from pokemon_snake import (
    ENEMY_DATA_LOOKUP,
    HEAL_AMOUNT_ON_VICTORY,  # Necesario para el test de batalla
    MAP_HEIGHT,
    MAP_WIDTH,
    REQUIRED_BANDS,  # Necesario para el test del portero
    SQUIRTLE_DATA,
    EnemyDataKey,
    GameLogic,
    GameState,
)

# --- INICIO FASE 1: Pruebas Unitarias (Movimiento) ---


def test_compute_new_position_move_up():
    logic = GameLogic()
    start_pos = [10, 10]
    new_pos = logic._compute_new_position("w", start_pos)
    # (Anotación) Verificamos que 'w' reste 1 a Y
    assert new_pos == [10, 9]


def test_compute_new_position_move_down():
    logic = GameLogic()
    start_pos = [10, 10]
    new_pos = logic._compute_new_position("s", start_pos)
    # (Anotación) Verificamos que 's' sume 1 a Y
    assert new_pos == [10, 11]


def test_compute_new_position_move_left():
    logic = GameLogic()
    start_pos = [10, 10]
    new_pos = logic._compute_new_position("a", start_pos)
    # (Anotación) Verificamos que 'a' reste 1 a X
    assert new_pos == [9, 10]


def test_compute_new_position_move_right():
    logic = GameLogic()
    start_pos = [10, 10]
    new_pos = logic._compute_new_position("d", start_pos)
    # (Anotación) Verificamos que 'd' sume 1 a X
    assert new_pos == [11, 10]


def test_compute_new_position_wrap_around_top():
    logic = GameLogic()
    start_pos = [20, 0]  # Borde superior
    new_pos = logic._compute_new_position("w", start_pos)
    # (Anotación) Verificamos el 'wrap' (teletransporte) superior
    assert new_pos == [20, MAP_HEIGHT - 1]  # Debería ser 19


def test_compute_new_position_wrap_around_bottom():
    logic = GameLogic()
    start_pos = [20, MAP_HEIGHT - 1]  # Borde inferior
    new_pos = logic._compute_new_position("s", start_pos)
    # (Anotación) Verificamos el 'wrap' inferior
    assert new_pos == [20, 0]


def test_compute_new_position_wrap_around_left():
    logic = GameLogic()
    start_pos = [0, 10]  # Borde izquierdo
    new_pos = logic._compute_new_position("a", start_pos)
    # (Anotación) Verificamos el 'wrap' izquierdo
    assert new_pos == [MAP_WIDTH - 1, 10]  # Debería ser 40


def test_compute_new_position_wrap_around_right():
    logic = GameLogic()
    start_pos = [MAP_WIDTH - 1, 10]  # Borde derecho
    new_pos = logic._compute_new_position("d", start_pos)
    # (Anotación) Verificamos el 'wrap' derecho
    assert new_pos == [0, 10]


def test_compute_new_position_invalid_key():
    logic = GameLogic()
    start_pos = [10, 10]
    new_pos = logic._compute_new_position("x", start_pos)  # 'x' no es válida
    # (Anotación) Verificamos que una tecla inválida devuelva None
    assert new_pos is None


# --- INICIO FASE 2: Pruebas de Integración Ligera (Fixtures) ---


@pytest.fixture
def clean_game_state():
    """
    (Anotación) Esta 'fixture' crea un GameState limpio y
    fresco para cada prueba que lo pida.
    """
    SQUIRTLE_DATA.trainer = "Test Trainer"
    # (Anotación) Eliminamos la línea 'gender_term' porque
    # no existe en tu Dataclass de PokemonData
    return GameState()


@pytest.fixture
def game_logic_instance():
    """(Anotación) Fixture que provee una instancia de GameLogic."""
    return GameLogic()


def test_update_state_moves_player(game_logic_instance, clean_game_state, mocker):
    """
    (Anotación) Prueba que update_state mueva correctamente al jugador
    cuando el movimiento es válido.
    """
    mocker.patch.object(game_logic_instance, "_get_object_at_position", return_value=None)

    start_pos = clean_game_state.my_position.copy()  # [20, 18]

    mock_renderer = mocker.MagicMock()
    game_logic_instance.update_state("a", clean_game_state, mock_renderer)  # Moverse izquierda

    # --- ESTA ES LA LÍNEA CORREGIDA ---
    assert clean_game_state.my_position == [start_pos[0] - 1, start_pos[1]]  # [19, 18]
    assert clean_game_state.tail == []


def test_update_state_hits_obstacle(game_logic_instance, clean_game_state, mocker):
    """
    (Anotación) Prueba que el jugador NO se mueva si
    intenta entrar en un obstáculo.
    """
    mocker.patch.object(game_logic_instance, "_get_object_at_position", return_value=None)

    # (Anotación) Forzamos una posición al lado de un muro conocido
    clean_game_state.my_position = [1, 1]
    start_pos = clean_game_state.my_position.copy()

    mock_renderer = mocker.MagicMock()
    game_logic_instance.update_state(
        "w", clean_game_state, mock_renderer
    )  # 'w' chocaría con '#' en [1, 0]

    # (Anotación) Verificamos que el jugador NO se movió
    assert clean_game_state.my_position == start_pos
    # (AnotACIÓN) Verificamos que la cola NO se actualizó
    assert clean_game_state.tail == []


def test_porter_blocks_if_not_enough_bands(game_logic_instance, clean_game_state, mocker):
    """
    (Anotación) Prueba que el portero bloquee el paso si no
    tenemos las bandas.
    """
    # (Anotación) Mockeamos 'clear_screen' e 'input'
    mocker.patch("pokemon_snake.clear_screen")
    mocker.patch("builtins.input")  # 'builtins.input' es la ruta para el input global
    mocker.patch.object(game_logic_instance, "_get_object_at_position", return_value=None)

    porter_pos = game_logic_instance.porter_position  # [20, 17]
    # (Anotación) Nos colocamos justo debajo del portero
    player_start_pos = [porter_pos[0], porter_pos[1] + 1]  # [20, 18]
    clean_game_state.my_position = player_start_pos

    # (Anotación) No tenemos bandas (bands_obtained == 0)
    assert clean_game_state.bands_obtained == 0
    assert clean_game_state.bands_obtained < REQUIRED_BANDS

    mock_renderer = mocker.MagicMock()
    game_logic_instance.update_state("w", clean_game_state, mock_renderer)

    # (Anotación) Verificamos que NO nos movimos
    assert clean_game_state.my_position == player_start_pos


# --- FIN FASE 2 ---

# --- INICIO FASE 3: Pruebas de Integración Avanzada (Mocking) ---


def test_battle_player_wins(game_logic_instance, clean_game_state, mocker):
    """
    (Anotación) Prueba un flujo de batalla completo donde el jugador gana.
    Usamos 'mocker' para controlar todo lo aleatorio y el input.
    """
    # (Anotación) Datos de prueba
    bulbasaur_data = ENEMY_DATA_LOOKUP[EnemyDataKey.BULBASAUR]
    object_ref = (EnemyDataKey.BULBASAUR, 5, 1)  # Posición ficticia
    initial_hp = clean_game_state.squirtle_current_hp  # 80

    # --- MOCKING (SIMULACIÓN) ---

    # (Anotación) 1. Simulamos que el jugador SIEMPRE elige 'P' (Placaje)
    mocker.patch.object(game_logic_instance, "_get_player_attack_choice", return_value="P")

    # (Anotación) 2. Simulamos que NADIE esquiva (random.randint siempre da 10)
    mocker.patch("pokemon_snake.random.randint", return_value=10)

    # (Anotación) 3. Simulamos que el enemigo SIEMPRE usa su primer ataque ('tackle', 8 daño)
    mocker.patch("pokemon_snake.random.choice", return_value=("tackle", 8))

    # (Anotación) 4. Simulamos 'input()' para que la prueba no se pause
    mocker.patch("builtins.input", return_value="")

    # (Anotación) 5. Simulamos 'clear_screen' para que no haga nada
    mocker.patch("pokemon_snake.clear_screen")

    # (Anotación) 6. Creamos un Mock para el Renderer y su método público
    mock_renderer = mocker.MagicMock()
    mocker.patch.object(mock_renderer, "render_hp_bars")

    # --- EJECUCIÓN ---

    # (Anotación) Ejecutamos la batalla. Tu código _start_battle
    # (necesita el 'data_key' y el 'renderer', así que los añadimos)
    game_logic_instance._start_battle(
        clean_game_state,
        bulbasaur_data,
        object_ref,
        EnemyDataKey.BULBASAUR,  # <--- Argumento necesario
        mock_renderer,  # <--- Argumento necesario
    )

    # --- VERIFICACIÓN ---

    # (Anotación) ¿Ganamos la banda?
    assert clean_game_state.bands_obtained == 1

    # (Anotación) ¿Se curó Squirtle?
    # HP inicial = 80
    # Daño enemigo = 8
    # HP al final de batalla (antes de curar) = 72
    # Curación = 70
    # HP final (después de curar) = min(72 + 70, 80) = 80
    expected_hp_after_battle = initial_hp - 8  # 72
    expected_hp_after_healing = min(
        expected_hp_after_battle + HEAL_AMOUNT_ON_VICTORY, SQUIRTLE_DATA.initial_hp
    )  # min(142, 80)

    assert clean_game_state.squirtle_current_hp == expected_hp_after_healing

    # (Anotación) ¿Se añadió el emoji a la cola?
    assert len(clean_game_state.defeated_enemies_list) == 1
    assert clean_game_state.defeated_enemies_list[0] == bulbasaur_data.emoji  # '🌿'

    # (Anotación) ¿Se actualizó la longitud de la cola?
    assert clean_game_state.tail_length == 1

    # (Anotación) ¿Se eliminó a Bulbasaur del mapa?
    assert object_ref not in clean_game_state.map_objects


# --- FIN FASE 3 ---
