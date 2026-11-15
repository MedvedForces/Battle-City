from ..core.map import GameMap

def game_tanks():
    for tank in GameMap.tanks:
        tank.update()

def game_blocks():
    for block in GameMap.blocks:
        block.update()

def game_shells():
    for obj in GameMap.shells:
        obj.update()

def game_bonuses():
    for obj in GameMap.bonuses:
        obj.update()