import unittest
from unittest.mock import patch, Mock
# Asegúrate de importar las clases que quieres probar de tu archivo principal
from Pokemon_Snake_v01 import GameState, GameLogic, EnemyDataKey, FIXED_MAP_OBJECTS, MAP_WIDTH, MAP_HEIGHT, REQUIRED_BANDS, SQUIRTLE_DATA, PORTER_EMOJI, STADIUM_PORTER_NAME

class TestGameState(unittest.TestCase):
    """Pruebas para la clase GameState."""

    def setUp(self):
        """Configura una instancia de GameState para cada prueba."""
        self.game_state = GameState()

    def test_initial_state_values(self):
        """Verifica que los atributos de GameState se inicializan correctamente."""
        self.assertEqual(self.game_state.my_position, [20, 18])
        self.assertEqual(self.game_state.tail, [])
        self.assertEqual(self.game_state.tail_length, 0)
        self.assertEqual(self.game_state.squirtle_current_hp, SQUIRTLE_DATA.initial_hp)
        self.assertEqual(self.game_state.bands_obtained, 0)
        self.assertFalse(self.game_state.porter_defeated)
        self.assertIsInstance(self.game_state.map_objects, list)
        self.assertIsInstance(self.game_state.obstacle_definition, list)
        self.assertIsInstance(self.game_state.defeated_enemies_list, list)
        # Verifica que los objetos fijos del mapa se cargan
        self.assertGreater(len(self.game_state.map_objects), 0)

    def test_parse_obstacle_map(self):
        """Verifica que el mapa de obstáculos se parsea correctamente."""
        raw_map = "# #\n#  \n   "
        parsed_map = self.game_state._parse_obstacle_map(raw_map)

        # Construye el mapa esperado dinámicamente, rellenando cada fila hasta MAP_WIDTH
        expected_map = [
            list("# #".ljust(MAP_WIDTH)),
            list("#  ".ljust(MAP_WIDTH)),
            list("   ".ljust(MAP_WIDTH))
        ]

        self.assertEqual(parsed_map, expected_map)
        # Asegúrate de que el mapa parseado tiene la altura correcta (basado en el raw_map)
        self.assertEqual(len(parsed_map), len(raw_map.split('\n')))
        # Asegúrate de que cada fila del mapa parseado tiene el ancho correcto (MAP_WIDTH)
        self.assertEqual(len(parsed_map[0]), MAP_WIDTH)

    def test_reset_game(self):
        """Verifica que el juego se reinicia completamente."""
        self.game_state.my_position = [1, 1]
        self.game_state.squirtle_current_hp = 10
        self.game_state.bands_obtained = 1
        self.game_state.porter_defeated = True
        self.game_state.tail_length = 5
        self.game_state.defeated_enemies_list = ["E1", "E2"]

        self.game_state.reset_game()

        self.assertEqual(self.game_state.my_position, [20, 18])
        self.assertEqual(self.game_state.squirtle_current_hp, SQUIRTLE_DATA.initial_hp)
        self.assertEqual(self.game_state.bands_obtained, 0)
        self.assertFalse(self.game_state.porter_defeated)
        self.assertEqual(self.game_state.tail_length, 0)
        self.assertEqual(self.game_state.defeated_enemies_list, [])

    def test_reset_player_after_defeat(self):
        """Verifica que solo el jugador se reinicia tras una derrota."""
        self.game_state.my_position = [1, 1]
        self.game_state.squirtle_current_hp = 10
        self.game_state.bands_obtained = 1 # Esto no debería cambiar
        self.game_state.porter_defeated = True # Esto no debería cambiar

        self.game_state.reset_player_after_defeat()

        self.assertEqual(self.game_state.my_position, [20, 18])
        self.assertEqual(self.game_state.squirtle_current_hp, SQUIRTLE_DATA.initial_hp)
        self.assertEqual(self.game_state.bands_obtained, 1) # Se mantiene
        self.assertTrue(self.game_state.porter_defeated) # Se mantiene


class TestGameLogicMovement(unittest.TestCase):
    """Pruebas para la lógica de movimiento y colisiones en GameLogic."""

    def setUp(self):
        """Configura una instancia de GameLogic y GameState para cada prueba."""
        self.game_logic = GameLogic()
        self.game_state = GameState()
        # Asegúrate de que la posición del portero esté definida para las pruebas
        self.porter_pos = self.game_logic._find_porter_position()
        if self.porter_pos == [-1, -1]:
            # Si no se encuentra, añade una posición de portero mock para la prueba
            self.porter_pos = [20, 17]
            FIXED_MAP_OBJECTS.append((EnemyDataKey.PORTERO, 20, 17))
            self.game_logic.porter_position = self.porter_pos


    def test_compute_new_position_up(self):
        """Verifica el movimiento hacia arriba (W) con wrap-around."""
        self.game_state.my_position = [10, 5]
        new_pos = self.game_logic._compute_new_position("w", self.game_state.my_position)
        self.assertEqual(new_pos, [10, 4])

        self.game_state.my_position = [10, 0] # Borde superior
        new_pos = self.game_logic._compute_new_position("w", self.game_state.my_position)
        self.assertEqual(new_pos, [10, MAP_HEIGHT - 1]) # Wrap-around

    def test_compute_new_position_down(self):
        """Verifica el movimiento hacia abajo (S) con wrap-around."""
        self.game_state.my_position = [10, 5]
        new_pos = self.game_logic._compute_new_position("s", self.game_state.my_position)
        self.assertEqual(new_pos, [10, 6])

        self.game_state.my_position = [10, MAP_HEIGHT - 1] # Borde inferior
        new_pos = self.game_logic._compute_new_position("s", self.game_state.my_position)
        self.assertEqual(new_pos, [10, 0]) # Wrap-around

    def test_compute_new_position_left(self):
        """Verifica el movimiento hacia la izquierda (A) con wrap-around."""
        self.game_state.my_position = [10, 5]
        new_pos = self.game_logic._compute_new_position("a", self.game_state.my_position)
        self.assertEqual(new_pos, [9, 5])

        self.game_state.my_position = [0, 5] # Borde izquierdo
        new_pos = self.game_logic._compute_new_position("a", self.game_state.my_position)
        self.assertEqual(new_pos, [MAP_WIDTH - 1, 5]) # Wrap-around

    def test_compute_new_position_right(self):
        """Verifica el movimiento hacia la derecha (D) con wrap-around."""
        self.game_state.my_position = [10, 5]
        new_pos = self.game_logic._compute_new_position("d", self.game_state.my_position)
        self.assertEqual(new_pos, [11, 5])

        self.game_state.my_position = [MAP_WIDTH - 1, 5] # Borde derecho
        new_pos = self.game_logic._compute_new_position("d", self.game_state.my_position)
        self.assertEqual(new_pos, [0, 5]) # Wrap-around

    def test_compute_new_position_invalid(self):
        """Verifica que una dirección inválida devuelve None."""
        self.game_state.my_position = [10, 5]
        new_pos = self.game_logic._compute_new_position("x", self.game_state.my_position)
        self.assertIsNone(new_pos)

    @patch('builtins.print')
    @patch('builtins.input', return_value='')
    def test_is_blocked_by_porter_without_bands(self, mock_input, mock_print):
        """Verifica que el jugador es bloqueado por el portero sin suficientes bandas."""
        self.game_state.bands_obtained = REQUIRED_BANDS - 1 # Menos de las requeridas
        is_blocked = self.game_logic._is_blocked_by_porter(self.porter_pos, self.game_state)
        self.assertTrue(is_blocked)
        mock_print.assert_called_with(f"¡Alto ahí! Necesitas obtener las {REQUIRED_BANDS} bandas de Entrenador/a para entrar al Estadio.")
        mock_input.assert_called_once()

    @patch('builtins.print')
    @patch('builtins.input', return_value='')
    def test_is_not_blocked_by_porter_with_bands(self, mock_input, mock_print):
        """Verifica que el jugador no es bloqueado por el portero con suficientes bandas."""
        self.game_state.bands_obtained = REQUIRED_BANDS # Suficientes bandas
        is_blocked = self.game_logic._is_blocked_by_porter(self.porter_pos, self.game_state)
        self.assertFalse(is_blocked)
        mock_print.assert_not_called()
        mock_input.assert_not_called()

    def test_is_not_blocked_by_porter_at_different_position(self):
        """Verifica que el jugador no es bloqueado si no está en la posición del portero."""
        self.game_state.bands_obtained = 0 # No importa las bandas si no está en la posición
        different_pos = [self.porter_pos[0] + 1, self.porter_pos[1]]
        is_blocked = self.game_logic._is_blocked_by_porter(different_pos, self.game_state)
        self.assertFalse(is_blocked)


if __name__ == '__main__':
    unittest.main()