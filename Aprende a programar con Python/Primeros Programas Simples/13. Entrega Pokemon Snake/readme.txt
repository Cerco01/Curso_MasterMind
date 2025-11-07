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
    - `Game`: Orquesta el conjunto, uniendo las demás clases en el bucle principal.

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