# Battle City

## Run

Install the dependency:

```powershell
python -m pip install pygame
```

Then start the game from the project root:

```powershell
python main.py
```

Run the tests with:

```powershell
python -m unittest discover -s tests
```

## Project layout

- `battle_city/core/` — shared game state and project-relative resource paths.
- `battle_city/entities/` — tanks, blocks, bonuses, and shells.
- `battle_city/game/` — level loading, map operations, and game loop.
- `battle_city/ui/` — menus, buttons, and custom-level editor.
- `battle_city/data/` — map object identifiers.
- `assets/sprites/`, `assets/audio/`, `assets/extra_sprites/` — images and sounds.
- `assets/maps/` — built-in levels and the saved custom map.
- `tests/` — automated tests and their fixtures.
- `main.py` — application entry point.
