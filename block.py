import pygame
from map import GameMap
from abc import ABC, abstractmethod


class Block(ABC):
    @abstractmethod
    def __init__(self):
        self.alive = True

    @abstractmethod
    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, self.rect)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.alive = False

class Brick(Block):
    def __init__(self, px, py, size_width, size_height):
        super().__init__()
        GameMap.blocks.append(self)
        self.type = 'brick'
        self.image = GameMap.img_brick

        self.rect = pygame.Rect(px, py, size_width, size_height)
        self.hp = 1

    def update(self):
        pass

class Steel(Block):
    def __init__(self, px, py, size_width, size_height):
        super().__init__()
        GameMap.blocks.append(self)
        self.type = 'steel'
        self.image = GameMap.img_steel

        self.rect = pygame.Rect(px, py, size_width, size_height)
        self.hp = 999999 # 999999, чтобы понятно было.В damage отнимается 0

    def update(self):
        pass

class Ice(Block):
    def __init__(self, px, py, size_width, size_height):
        super().__init__()
        GameMap.blocks.append(self)
        self.type = 'ice'
        self.image = GameMap.img_ice

        self.rect = pygame.Rect(px, py, size_width, size_height)
        self.hp = 1

    def update(self):
        pass

class Water(Block):
    def __init__(self, px, py, size_width, size_height):
        super().__init__()
        GameMap.blocks.append(self)
        self.type = 'water'
        self.image = GameMap.img_water

        self.rect = pygame.Rect(px, py, size_width, size_height)

    def update(self):
        pass

class Bird(Block):
    def __init__(self, px, py, size_width, size_height):
        super().__init__()
        GameMap.blocks.append(self)
        self.type = 'bird'
        self.image = GameMap.img_bird

        self.rect = pygame.Rect(px, py, size_width, size_height)
        self.hp = 1

    def update(self):
        pass
