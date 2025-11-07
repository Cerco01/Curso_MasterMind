from pokemon_snake import GameConstants, GameState


def test_parse_obstacle_map_dimensions_and_padding():
    """
    (Anotación) Prueba que el parser del mapa maneje bien las filas
    de diferentes longitudes y aplique el padding correcto.
    """
    # (Anotación) Creamos un mapa de prueba simple y pequeño
    raw_test_map = "# \n #\n##"

    # (Anotación) Accedemos al método estático (no necesitamos instancia)
    parsed_map = GameState._parse_obstacle_map(raw_test_map)

    # (Anotación) Verificación 1: Dimensiones
    assert len(parsed_map) == 3  # Debe tener 3 filas
    assert len(parsed_map[0]) == GameConstants.MAP_WIDTH  # Cada fila debe rellenarse
    assert len(parsed_map[1]) == GameConstants.MAP_WIDTH
    assert len(parsed_map[2]) == GameConstants.MAP_WIDTH

    # (Anotación) Verificación 2: Contenido
    assert parsed_map[0][0] == "#"
    assert parsed_map[0][1] == " "
    assert parsed_map[0][2] == " "  # Padding

    assert parsed_map[1][0] == " "  # Manejo de 'rstrip'
    assert parsed_map[1][1] == "#"
    assert parsed_map[1][2] == " "  # Padding

    assert parsed_map[2][0] == "#"
    assert parsed_map[2][1] == "#"
    assert parsed_map[2][2] == " "  # Padding
