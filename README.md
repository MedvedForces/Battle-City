# Battle City

Battle City — игра, созданная в качестве проекта по предмету Python на втором курсе университета. Игра сделана по мотивам Battle City.

В игре доступны два готовых уровня, а также редактор, в котором можно создавать собственные уровни.

## Установка и запуск

Установите Pygame:

```powershell
python -m pip install pygame
```

Запустите игру из корневой папки проекта:

```powershell
python main.py
```

## Запуск тестов

```powershell
python -m unittest discover -s tests
```

## Структура проекта

- `battle_city/core/` — основное состояние игры и пути к ресурсам.
- `battle_city/entities/` — танки, блоки, бонусы и снаряды.
- `battle_city/game/` — загрузка уровней, работа с картой и игровой цикл.
- `battle_city/ui/` — меню, кнопки и редактор уровней.
- `battle_city/data/` — данные игровых объектов.
- `assets/sprites/`, `assets/audio/`, `assets/extra_sprites/` — изображения и звуки.
- `assets/maps/` — готовые уровни и файл пользовательской карты.
- `tests/` — тесты и необходимые для них файлы.
- `main.py` — запуск игры.
