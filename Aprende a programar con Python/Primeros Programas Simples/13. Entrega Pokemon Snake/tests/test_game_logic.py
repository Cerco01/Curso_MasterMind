import pytest
from pokemon_snake import (
    EnemyDataKey,
    GameConstants,  # Nueva clase
    GameLogic,
    GameState,
    PokemonLibrary,  # Nueva clase
)

# --- INICIO FASE 1: Pruebas Unitarias ---


def test_compute_new_position_move_up():
    logic = GameLogic()
    start_pos = [10, 10]
    new_pos = logic._compute_new_position("w", start_pos)
    assert new_pos == [10, 9]


def test_compute_new_position_move_down():
    logic = GameLogic()
    start_pos = [10, 10]
    new_pos = logic._compute_new_position("s", start_pos)
    assert new_pos == [10, 11]


def test_compute_new_position_move_left():
    logic = GameLogic()
    start_pos = [10, 10]
    new_pos = logic._compute_new_position("a", start_pos)
    assert new_pos == [9, 10]


def test_compute_new_position_move_right():
    logic = GameLogic()
    start_pos = [10, 10]
    new_pos = logic._compute_new_position("d", start_pos)
    assert new_pos == [11, 10]


def test_compute_new_position_wrap_around_top():
    logic = GameLogic()
    start_pos = [20, 0]  # Borde superior
    new_pos = logic._compute_new_position("w", start_pos)
    assert new_pos == [20, GameConstants.MAP_HEIGHT - 1]


def test_compute_new_position_wrap_around_bottom():
    logic = GameLogic()
    start_pos = [20, GameConstants.MAP_HEIGHT - 1]  # Borde inferior
    new_pos = logic._compute_new_position("s", start_pos)
    assert new_pos == [20, 0]


def test_compute_new_position_wrap_around_left():
    logic = GameLogic()
    start_pos = [0, 10]  # Borde izquierdo
    new_pos = logic._compute_new_position("a", start_pos)
    assert new_pos == [GameConstants.MAP_WIDTH - 1, 10]


def test_compute_new_position_wrap_around_right():
    logic = GameLogic()
    start_pos = [GameConstants.MAP_WIDTH - 1, 10]  # Borde derecho
    new_pos = logic._compute_new_position("d", start_pos)
    assert new_pos == [0, 10]


def test_compute_new_position_invalid_key():
    logic = GameLogic()
    start_pos = [10, 10]
    new_pos = logic._compute_new_position("x", start_pos)  # 'x' no es válida
    assert new_pos is None


# --- INICIO FASE 2: Pruebas de Integración Ligera (Fixtures) ---


@pytest.fixture
def clean_game_state():
    """(Anotación) Crea un GameState limpio para cada prueba."""
    PokemonLibrary.PIKACHU.trainer = "Test Trainer"
    return GameState()


@pytest.fixture
def game_logic_instance():
    """(Anotación) Fixture que provee una instancia de GameLogic."""
    return GameLogic()


def test_update_state_moves_player(game_logic_instance, clean_game_state, mocker):
    """(Anotación) Prueba que update_state mueva correctamente al jugador."""
    mocker.patch.object(game_logic_instance, "_get_object_at_position", return_value=None)
    start_pos = clean_game_state.my_position.copy()  # [20, 18]
    mock_renderer = mocker.MagicMock()
    game_logic_instance.update_state("a", clean_game_state, mock_renderer)  # Moverse izquierda
    assert clean_game_state.my_position == [start_pos[0] - 1, start_pos[1]]  # [19, 18]
    assert clean_game_state.tail == []


def test_update_state_hits_obstacle(game_logic_instance, clean_game_state, mocker):
    """(Anotación) Prueba que el jugador NO se mueva si choca."""
    mocker.patch.object(game_logic_instance, "_get_object_at_position", return_value=None)
    clean_game_state.my_position = [1, 1]
    start_pos = clean_game_state.my_position.copy()
    mock_renderer = mocker.MagicMock()
    game_logic_instance.update_state("w", clean_game_state, mock_renderer)
    assert clean_game_state.my_position == start_pos
    assert clean_game_state.tail == []


def test_porter_blocks_if_not_enough_bands(game_logic_instance, clean_game_state, mocker):
    """(Anotación) Prueba que el portero bloquee el paso."""
    mocker.patch("pokemon_snake.clear_screen")
    mocker.patch("builtins.input")
    mocker.patch.object(game_logic_instance, "_get_object_at_position", return_value=None)

    porter_pos = game_logic_instance.porter_position  # [20, 17]
    player_start_pos = [porter_pos[0], porter_pos[1] + 1]  # [20, 18]
    clean_game_state.my_position = player_start_pos

    assert clean_game_state.bands_obtained == 0
    assert clean_game_state.bands_obtained < GameConstants.REQUIRED_BANDS

    mock_renderer = mocker.MagicMock()
    game_logic_instance.update_state("w", clean_game_state, mock_renderer)
    assert clean_game_state.my_position == player_start_pos


# --- FIN FASE 2 ---

# --- INICIO FASE 3: Pruebas de Integración Avanzada (Mocking) ---


def test_battle_player_wins(game_logic_instance, clean_game_state, mocker):
    """(Anotación) Prueba un flujo de batalla completo donde el jugador (Pikachu) gana."""
    bulbasaur_data = PokemonLibrary.ENEMY_LOOKUP[EnemyDataKey.BULBASAUR]
    object_ref = (EnemyDataKey.BULBASAUR, 5, 1)
    initial_hp = clean_game_state.player_current_hp  # 75

    # --- MOCKING (SIMULACIÓN) ---
    mocker.patch.object(game_logic_instance, "_get_player_attack_choice", return_value="A")
    mocker.patch("pokemon_snake.random.randint", return_value=10)
    mocker.patch("pokemon_snake.random.choice", return_value=("tackle", 8))
    mocker.patch("builtins.input", return_value="")
    mocker.patch("pokemon_snake.clear_screen")

    mock_renderer = mocker.MagicMock()
    mocker.patch.object(mock_renderer, "render_hp_bars")

    # --- EJECUCIÓN ---
    game_logic_instance._start_battle(
        clean_game_state,
        bulbasaur_data,
        object_ref,
        EnemyDataKey.BULBASAUR,
        mock_renderer,
    )

    # --- VERIFICACIÓN ---
    assert clean_game_state.bands_obtained == 1

    expected_hp_after_battle = initial_hp - 8  # 67
    expected_hp_after_healing = min(
        expected_hp_after_battle + GameConstants.HEAL_AMOUNT_ON_VICTORY,
        PokemonLibrary.PIKACHU.initial_hp,
    )  # min(137, 75)

    assert clean_game_state.player_current_hp == expected_hp_after_healing

    assert len(clean_game_state.defeated_enemies_list) == 1
    assert clean_game_state.defeated_enemies_list[0] == bulbasaur_data.emoji
    assert clean_game_state.tail_length == 1
    assert object_ref not in clean_game_state.map_objects


# --- FIN FASE 3 ---
