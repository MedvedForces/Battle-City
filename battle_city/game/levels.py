from pathlib import Path

from . import create_map
from ..core.map import GameMap
from ..data.all_object_number_dictionary import all_object_number, all_object_symbol
from ..entities.tank import BotChasing
from ..entities.block import Brick
from ..core.paths import MAPS_DIR


def create_levels_use_read_from_file(level, map_width, map_height):
    level_path = Path(level)
    if not level_path.is_absolute():
        level_path = MAPS_DIR / level_path
    file = open(level_path, 'r')

    map = [[0] * map_width for i in range(map_height)]

    row, col = 0, 0
    for line in file:
        for s in line:
            if s != '\n':
                map[row][col] = all_object_symbol.index(s)
                col += 1
                if col >= map_width:
                    row += 1
                    col = 0
                    if row >= map_height:
                        break

    cell_size = 32

    object_handlers = {
        'player': lambda x, y, direction: create_map.create_player(x, y,
                                                                   direction),
        'bot_default': lambda x, y, direction: create_map.create_bot_default(x, y, direction),
        'bot_chasing': lambda x, y, direction: create_map.create_bot_chasing(x, y, direction),
        'brick': lambda x, y, direction: create_map.create_brick(x, y),
        'steel': lambda x, y, direction: create_map.create_steel(x, y),
        'ice': lambda x, y, direction: create_map.create_ice(x, y),
        'water' : lambda x, y, direction: create_map.create_water(x, y),
        'bird': lambda x, y, direction: create_map.create_bird(x, y),
        'bonus_hp': lambda x, y, direction: create_map.create_bonus_hp(x, y),
        'bonus_armor': lambda x, y, direction: create_map.create_bonus_armor(x, y),
    }

    for row in range(map_height):
        for col in range(map_width):
            x, y = col * cell_size, row * cell_size
            cell_value = map[row][col]

            for (obj_type, direction), number in all_object_number.items():
                if number == cell_value:
                    if obj_type in object_handlers:
                        object_handlers[obj_type](x, y, direction)
                    break

    for obj in GameMap.blocks:
        if obj.type == 'bird':
            GameMap.count_bird += 1

    file.close()


def level1():
    create_levels_use_read_from_file(MAPS_DIR / "level1.txt",
                   GameMap.WIDTH // 32, GameMap.HEIGHT // 32)


def level2():
    create_levels_use_read_from_file(MAPS_DIR / "level2.txt",
                   GameMap.WIDTH // 32, GameMap.HEIGHT // 32)
    create_map.create_bonus_armor(400, 400)

def clean_level():
    GameMap.clean_map()
    GameMap.count_bird = 0