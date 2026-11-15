from ..core.map import GameMap

def game_tanks(window):
    for tank in GameMap.tanks:
        tank.draw(window)

def game_blocks(window):
    for block in GameMap.blocks:
        block.draw(window)

def game_bullets(window):
    for obj in GameMap.shells:
        obj.draw(window)

def game_bonuses(window):
    for obj in GameMap.bonuses:
        obj.draw(window)