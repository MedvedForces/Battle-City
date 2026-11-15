from map import GameMap

def shells():
    for shell in GameMap.shells:
        if not shell.alive:
            GameMap.shells.remove(shell)

def blocks():
    for block in GameMap.blocks:
        if not block.alive:
            GameMap.blocks.remove(block)

def tanks():
    for tank in GameMap.tanks:
        if not tank.alive:
            GameMap.tanks.remove(tank)

def bonuses():
    for bonus in GameMap.bonuses:
        if not bonus.alive:
            GameMap.bonuses.remove(bonus)