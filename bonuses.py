import pygame
import menu_interface
from map import GameMap
from random import randint
from abc import ABC, abstractmethod
from shells import Bullet


class Bonus(ABC):
    @abstractmethod
    def __init__(self):
        self.alive = True

    @abstractmethod
    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, self.rect)

class BonusHP(Bonus):
    def __init__(self, px, py, size_width, size_height):
        super().__init__()
        GameMap.bonuses.append(self)
        self.type = 'bonus_hp'
        self.image = GameMap.img_bonus_hp

        self.rect = pygame.Rect(px, py, size_width, size_height)

    def update(self):
        pass

class BonusArmor(Bonus):
    def __init__(self, px, py, size_width, size_height):
        super().__init__()
        GameMap.bonuses.append(self)
        self.type = 'bonus_armor'
        self.image = GameMap.img_bonus_armor

        self.rect = pygame.Rect(px, py, size_width, size_height)

    def update(self):
        pass

