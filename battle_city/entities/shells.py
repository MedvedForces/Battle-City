import pygame
from ..core.map import GameMap
from abc import ABC, abstractmethod

class shells(ABC):
    def __init__(self):
        self.alive = True
    def move(self):
        self.px += self.dx
        self.py += self.dy
    def draw(self, window):
        pygame.draw.circle(window, "yellow", (self.px, self.py), 2)
    # def collisions_bricks(self):
    #     for block in GameMap.blocks:
    #         if (self.parent != block and block.type == "brick"
    #                 and block.rect.collidepoint(self.px, self.py)):
    #             block.damage(self.damage)
    #             self.alive = False
    #             # Bang(self.px, self.py)
    #             return True
    #     return False

    def check_collisions_block(self, block_type):
        for block in GameMap.blocks:
            if (self.parent != block and block_type == block.type
                    and block.rect.collidepoint(self.px, self.py)):
                block.damage(self.damage)
                if block_type == "ice":
                    self.count_damage_ice -= 1
                    if self.count_damage_ice == 0:
                        self.alive = False
                    return True
                if block_type == "steel":
                    self.alive = False
                    return True
                if block_type == "bird":
                    self.alive = False
                    GameMap.count_bird -= 1
                    return True
                if block_type == "brick":
                    self.alive = False
                    return True
        return False

    def check_collisions_tank(self, tank_type):
        for tank in GameMap.tanks:
            if (self.parent != tank and tank_type == tank.type
                    and tank.rect.collidepoint(self.px, self.py)):
                tank.damage(self.damage)
                self.alive = False
                if tank.type == tank_type:
                    return True
        return False

    # def collisions_ice(self):
    #     for block in GameMap.blocks:
    #         if (self.parent != block and block.type == "ice"
    #                 and block.rect.collidepoint(self.px, self.py)):
    #             block.damage(self.damage)
    #             self.count_damage_ice -= 1
    #             if self.count_damage_ice == 0:
    #                 self.alive = False
    #             # Bang(self.px, self.py)
    #             return True
    #     return False

    # def collisions_steels(self):
    #     for block in GameMap.blocks:
    #         if (self.parent != block and block.type == "steel"
    #                 and block.rect.collidepoint(self.px, self.py)):
    #             block.damage(self.damage)
    #             self.alive = False
    #             # Bang(self.px, self.py)
    #             return True
    #     return False

    # def collisions_bird(self):
    #     for block in GameMap.blocks:
    #         if (self.parent != block and block.type == "bird"
    #                 and block.rect.collidepoint(self.px, self.py)):
    #             block.damage(self.damage)
    #             self.alive = False
    #             GameMap.count_bird -= 1
    #             # Bang(self.px, self.py)
    #             return True
    #     return False


class Bullet(shells):
    def __init__(self, parent, px, py, dx, dy, damage):
        super().__init__()
        GameMap.shells.append(self)
        self.type = "bullet"
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage
        self.count_damage_ice = 3

    def update(self):
        self.move()
        if (self.px < 0 or self.px > GameMap.WIDTH
                or self.py < 0 or self.py > GameMap.HEIGHT):
            GameMap.shells.remove(self)
        else:
            self.check_collisions_block("brick")
            self.check_collisions_block("steel")
            self.check_collisions_block("ice")
            self.check_collisions_block("bird")

            self.check_collisions_tank("bot_default")
            self.check_collisions_tank("player")
            self.check_collisions_tank("bot_chasing")
