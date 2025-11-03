# Curso MasterMind – Proyectos Python

Este repositorio contiene ejercicios y mini‑proyectos del curso.

## Normas y colaboración
- Lee las reglas de trabajo y estilo en `agents.md`.
- Para contribuciones, revisa `CONTRIBUTING.md`.

## Estructura relevante
- Juego principal: `Aprende a programar con Python/Primeros Programas Simples/13. Entrega Pokemon Snake/Pokemon_Snake_v01.py`

## Requisitos
- Python 3.12 (ver `venv/` ya configurado) y dependencias en `requirements.txt`.

## Ejecución rápida del juego
```bash
python "Aprende a programar con Python/Primeros Programas Simples/13. Entrega Pokemon Snake/Pokemon_Snake_v01.py"
```

## Referencias
- Normas de agentes y estilo: ver `agents.md` (incluye tono/idioma, gates de aprobación y nomenclatura: español para textos y documentación; inglés para código/identificadores).

## Validación de calidad
- Instalar herramientas (en el `venv` del proyecto):
```bash
"/Users/axelamadorlopez/Documents/Curso_MasterMind/venv/bin/pip" install ruff mypy
```
- Linter (ruff):
```bash
"/Users/axelamadorlopez/Documents/Curso_MasterMind/venv/bin/ruff" check .
"/Users/axelamadorlopez/Documents/Curso_MasterMind/venv/bin/ruff" format .
```
- Tipado (mypy):
```bash
"/Users/axelamadorlopez/Documents/Curso_MasterMind/venv/bin/mypy" .
```
Estas herramientas leen automáticamente la configuración de `pyproject.toml`.

