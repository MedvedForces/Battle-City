from map import GameMap
import os

def file(name):
    if os.path.exists(name):
        return True
    return False

def brick():
    for obj in GameMap.blocks:
        if obj.type == "brick":
            return True

def ice():
    for obj in GameMap.blocks:
        if obj.type == "ice":
            return True

def water():
    for obj in GameMap.blocks:
        if obj.type == "water":
            return True

def bird():
    for obj in GameMap.blocks:
        if obj.type == "bird":
            return True

def bot_default():
    for obj in GameMap.tanks:
        if obj.type == "bot_default":
            return True

def bot_chasing():
    for obj in GameMap.tanks:
        if obj.type == "bot_chasing":
            return True

def bot_all():
    for obj in GameMap.tanks:
        if obj.type == "bot_chasing" or obj.type == "bot_default":
            return True
    return False

def steel():
    for obj in GameMap.blocks:
        if obj.type == "steel":
            return True

def players():
    for tank in GameMap.tanks:
        if tank.type == "player":
            return True

def bonus_hp():
    for bonus in GameMap.bonuses:
        if bonus.type == "bonus_hp":
            return True

def bonus_armor():
    for bonus in GameMap.bonuses:
        if bonus.type == "bonus_armor":
            return True