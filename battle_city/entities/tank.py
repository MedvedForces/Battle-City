import pygame
from ..ui import menu_interface
from ..core.map import GameMap
from random import randint
from abc import ABC, abstractmethod
from .shells import Bullet


class Tank(ABC):
    @abstractmethod
    def __init__(self):
        self.alive = True

    @abstractmethod
    def update(self):
        pass

    def get_rotated_image(self):
        tank_img = GameMap.img_tanks[self.rank]
        return pygame.transform.rotate(tank_img,
                                       GameMap.ROTATIONS[self.direction])

    def activate_armor(self, duration_seconds=5):
        self.has_armor = True
        self.armor_timer = duration_seconds * GameMap.FPS

    def update_armor(self):
        if self.has_armor:
            self.armor_timer -= 1
            if self.armor_timer <= 0:
                self.has_armor = False

    def move(self, keys):
        directions = [
            (self.controls[0], -self.speed, 0, "Left"),
            (self.controls[1], self.speed, 0, "Right"),
            (self.controls[2], 0, -self.speed, "Up"),
            (self.controls[3], 0, self.speed, "Down")
        ]

        for key, dx, dy, direction in directions:
            if keys[key]:
                self.rect.x += dx
                self.rect.y += dy
                self.direction = direction
                break

    def draw(self, window):
        if self.has_armor:
            self.blick(window)
        else:
            window.blit(self.image, self.rect)

    def blick(self, window):
        alpha = 128 + 127 * (pygame.time.get_ticks() % 1000 > 500) #формула для мигания
        temp_image = self.image.copy()
        temp_image.fill((255, 255, 0, alpha),
                        special_flags=pygame.BLEND_RGBA_MULT)
        window.blit(temp_image, self.rect)

    def check_collisions(self):
        self.check_collisions_block("steel")
        self.check_collisions_block("brick")
        self.check_collisions_block("ice")
        self.check_collisions_block("bird")
        if (not self.check_collisions_block("water")):
            self.speed = self.speed_default

        self.check_collisions_tank("bot_default")
        self.check_collisions_tank("player")
        self.check_collisions_tank("bot_chasing")

        self.check_collisions_bonuses("bonus_hp")
        self.check_collisions_bonuses("bonus_armor")

        self.check_collision_map()


    def change_move(self):
        x1 = self.rect.x
        y1 = self.rect.y
        if self.direction == "Right":
            self.rect.x = x1 - 2
        if self.direction == "Left":
            self.rect.x = x1 + 2
        if self.direction == "Up":
            self.rect.y = y1 + 2
        if self.direction == "Down":
            self.rect.y = y1 - 2

    def check_collisions_block(self, block_type):
        for obj in GameMap.blocks:
            if obj != self and self.rect.colliderect(
                    obj.rect) and obj.type == block_type:
                if (obj.type != "water"):
                    self.change_move()
                else:
                    self.speed = self.speed_in_water
                if obj.type == block_type:
                    return True
        return False

    def check_collisions_tank(self, other_tank_type):
        for tank in GameMap.tanks:
            if tank != self and self.rect.colliderect(
                    tank.rect) and tank.type == other_tank_type:
                self.change_move()
                if tank.type == other_tank_type:
                    return True
        return False

    def check_collisions_bonuses(self, bonus_type):
        for obj in GameMap.bonuses:
            if obj != self and self.rect.colliderect(
                    obj.rect) and obj.type == bonus_type:
                if obj.type == "bonus_hp":
                    obj.alive = False
                    self.hp += 1
                elif obj.type == "bonus_armor":
                    obj.alive = False
                    self.activate_armor(5)
                if obj.type == bonus_type:
                    return True
        return False

    def check_collision_map(self):
        if (self.rect.x <= 0 or self.rect.x >= GameMap.WIDTH - 30
                or self.rect.y <= 0 or self.rect.y >= GameMap.HEIGHT - 30):
            self.change_move()
            return True
        return False

    def damage(self, amount):
        if hasattr(self, 'has_armor') and self.has_armor:
            return
        self.hp -= amount
        if self.hp <= 0:
            self.alive = False

    def handle_firing(self, keys):
        if keys[self.controls[4]] and self.fire_timer == 0:
            self.fire()
        if self.fire_timer > 0:
            self.fire_timer -= 1

    def fire(self):
        GameMap.shot_sound.play()

        direction = GameMap.DIRECTIONS[self.direction]
        Bullet(self, self.rect.centerx, self.rect.centery,
               direction[0] * self.bullet_speed,
               direction[1] * self.bullet_speed,
               self.bullet_damage)
        self.fire_timer = self.fire_delay


class Player(Tank):
    def __init__(self, color, x, y, direction, controls):
        super().__init__()
        self.type = "player"
        self.color = color
        self.direction = direction
        self.controls = controls

        self.fire_delay = 30
        self.fire_timer = 0
        self.bullet_speed = 5
        self.bullet_damage = 1

        self.speed_default = 2
        self.speed_in_water = 1
        self.speed = 2
        self.rank = 9
        self.hp = 3

        self.armor_timer = 0
        self.has_armor = False

        self.image = self.get_rotated_image()
        self.rect = self.image.get_rect(center=(x, y))

        GameMap.tanks.append(self)

    def update(self):
        self.update_armor()
        keys = pygame.key.get_pressed()
        self.move(keys)
        self.image = self.get_rotated_image()
        self.check_collisions()
        self.handle_firing(keys)


class BotAbstract(Tank):
    def __init__(self, color, x, y, direction):
        super().__init__()
        self.color = color
        self.direction = direction

        self.rank = 8
        self.speed = 2
        self.speed_in_water = 1
        self.speed_default = 2
        self.fire_delay = 30
        self.fire_timer = 0
        self.bullet_speed = 5
        self.bullet_damage = 1
        self.hp = 1

        self.armor_timer = 0
        self.has_armor = False

        self.move_timer = 0
        self.current_move_duration = 60
        self.direction_change_probability = 0.02
        self.fire_probability = 0.01
        self.last_collision_time = 0

        self.image = self.get_rotated_image()
        self.rect = self.image.get_rect(center=(x, y))

        GameMap.tanks.append(self)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def ai_behavior(self):
        pass

    def random_direction(self):
        random_array_direction = ["Left", "Right", "Up", "Down"]
        self.direction = random_array_direction[randint(0, 3)]
        self.image = self.get_rotated_image()

    def fire_random(self):
        random = randint(1, 100)
        if random <= self.fire_probability * 100 and self.fire_timer == 0:
            self.fire()

    def move_random(self):
        self.move_timer += 1

        if (self.move_timer >= self.current_move_duration or
                randint(1, 100) <= self.direction_change_probability * 100):
            self.random_direction()
            self.move_timer = 0
            self.current_move_duration = randint(30, 120)

        if self.direction in GameMap.DIRECTIONS:
            dx, dy = GameMap.DIRECTIONS[self.direction]
            dx *= self.speed
            dy *= self.speed
            self.rect.x += dx
            self.rect.y += dy


class BotDefault(BotAbstract):
    def __init__(self, color, x, y, direction):
        super().__init__(color, x, y, direction)
        self.type = "bot_default"
        self.rank = 8
        self.speed = 2
        self.hp = 1

    def ai_behavior(self):
        pass

    def update(self):
        self.update_armor()
        if self.fire_timer > 0:
            self.fire_timer -= 1

        old_x, old_y = self.rect.x, self.rect.y
        self.move_random()
        had_collision = self.check_collisions()

        if had_collision:
            self.rect.x, self.rect.y = old_x, old_y
            self.random_direction()
            self.move_timer = 0

        self.image = self.get_rotated_image()
        self.fire_random()


class BotChasing(BotAbstract):
    def __init__(self, color, x, y, direction):
        super().__init__(color, x, y, direction)
        self.type = "bot_chasing"
        self.rank = 7
        self.speed = 2
        self.hp = 1
        self.fire_probability = 0.03
        self.detection_range = 200

    def ai_behavior(self):
        pass

    def find_player(self):
        for tank in GameMap.tanks:
            if tank.type == "player":
                return tank
        return None

    def can_see_player(self, player):
        if not player:
            return False

        dx = abs(self.rect.centerx - player.rect.centerx)
        dy = abs(self.rect.centery - player.rect.centery)

        if dx <= self.detection_range and dy <= 32:
            return "horizontal"
        elif dy <= self.detection_range and dx <= 32:
            return "vertical"
        return False

    def move_towards_player(self, player):
        if not player:
            self.move_random()
            return

        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery

        if abs(dx) > abs(dy):
            if dx > 0:
                self.direction = "Right"
            else:
                self.direction = "Left"
        else:
            if dy > 0:
                self.direction = "Down"
            else:
                self.direction = "Up"

        if self.direction in GameMap.DIRECTIONS:
            move_dx, move_dy = GameMap.DIRECTIONS[self.direction]
            move_dx *= self.speed
            move_dy *= self.speed
            self.rect.x += move_dx
            self.rect.y += move_dy

    def update(self):
        self.update_armor()
        if self.fire_timer > 0:
            self.fire_timer -= 1

        player = self.find_player()
        visibility = self.can_see_player(player)

        old_x, old_y = self.rect.x, self.rect.y

        if player and visibility:
            self.move_towards_player(player)
            if visibility and randint(1, 100) <= self.fire_probability * 100:
                self.fire()
        else:
            self.move_random()

        had_collision = self.check_collisions()

        if had_collision:
            self.rect.x, self.rect.y = old_x, old_y
            self.random_direction()
            self.move_timer = 0

        self.image = self.get_rotated_image()

        if not visibility and self.fire_timer == 0:
            self.fire_random()