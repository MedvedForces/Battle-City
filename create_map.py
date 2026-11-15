import pygame

from map import GameMap
from tank import Player, BotDefault, BotChasing
from block import Brick, Steel, Ice, Bird, Water
from bonuses import BonusHP,BonusArmor

def create_player(x, y, direction):
    player_control = (
        pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE)
    Player("blue", x, y,
           direction, player_control)

def create_brick(x, y):
    Brick(x, y, GameMap.SIZE_BRICK_WIDTH, GameMap.SIZE_BRICK_HEIGHT)

def create_bird(x, y):
    Bird(x, y, GameMap.SIZE_BRICK_WIDTH, GameMap.SIZE_BRICK_WIDTH)

def create_bot_default(x, y, direction):
    BotDefault("red", x, y, direction)

def create_bot_chasing(x, y, direction):
    BotChasing("red", x, y, direction)

def create_water(x, y):
    Water(x, y, GameMap.SIZE_BRICK_WIDTH, GameMap.SIZE_BRICK_WIDTH)

def create_steel(x, y):
    Steel(x, y, GameMap.SIZE_BRICK_WIDTH, GameMap.SIZE_BRICK_WIDTH)
def create_ice(x, y):
    Ice(x, y, GameMap.SIZE_BRICK_WIDTH, GameMap.SIZE_BRICK_WIDTH)

def create_bonus_hp(x, y):
    BonusHP(x, y, GameMap.SIZE_BRICK_WIDTH, GameMap.SIZE_BRICK_WIDTH)
def create_bonus_armor(x, y):
    BonusArmor(x, y, GameMap.SIZE_BRICK_WIDTH, GameMap.SIZE_BRICK_WIDTH)