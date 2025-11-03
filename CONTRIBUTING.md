# Contribuir

Gracias por contribuir. Sigue estas pautas para mantener la calidad del repositorio.

## Antes de empezar
- Lee `agents.md` (gates de aprobación, estilo de interacción y normas de idioma/nomenclatura).
- Usa Python 3.12 y las dependencias de `requirements.txt`.

## Flujo de trabajo
1. Abre un issue o acordemos por chat el objetivo.
2. Propón opciones/plan y espera aprobación (ver gates en `agents.md`).
3. Implementa en cambios pequeños.
4. Pasa linter/typing y prueba manual.
5. Abre PR describiendo impacto, riesgos y próximos pasos.

## Estilo de código
- Identificadores y nombres en inglés.
- Textos, documentación y comentarios en español.
- Sin “magic numbers”; utiliza constantes.
- Early returns y manejo de errores claro (sin `except` vacíos).

## Commits
- Mensajes en imperativo: `feat:`, `fix:`, `refactor:`, `docs:`.
- Un commit por unidad de cambio coherente.

## Checklist de PR
- [ ] Linter/typing OK
- [ ] Se siguieron los gates de aprobación de `agents.md`
- [ ] Descripción del cambio e impacto
- [ ] Sin regresiones de UX/controles

