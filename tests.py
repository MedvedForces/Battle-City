import unittest
from itertools import count

import menu_interface
from map import GameMap
import pygame
import remove
import create_map
import menu_interface
import checkout
import main
from shells import Bullet, shells


class test_create_object(unittest.TestCase):
    main.initialization()

    # Создание объектов

    def test1_player(self):
        create_map.create_player(230, 400, "Left")
        self.assertEqual(True, checkout.players())
        GameMap.clean_map()

    def test2_brick(self):
        create_map.create_brick(230, 400)
        self.assertEqual(True, checkout.brick())
        GameMap.clean_map()
    def test3_steel(self):
        create_map.create_steel(230, 400)
        self.assertEqual(True, checkout.steel())
        GameMap.clean_map()
    def test3_ice(self):
        create_map.create_ice(230, 400)
        self.assertEqual(True, checkout.ice())
        GameMap.clean_map()
    def test5_water(self):
        create_map.create_water(230, 400)
        self.assertEqual(True, checkout.water())
        GameMap.clean_map()
    def test3_bird(self):
        create_map.create_bird(230, 400)
        self.assertEqual(True, checkout.bird())
        GameMap.clean_map()
    def test4_bot_default(self):
        create_map.create_bot_default(230, 400, "Left")
        self.assertEqual(True, checkout.bot_default())
        GameMap.clean_map()
    def test5_bot_chasing(self):
        create_map.create_bot_chasing(230, 400, "Left")
        self.assertEqual(True, checkout.bot_chasing())
        GameMap.clean_map()
    def test5_bonus_armor(self):
        create_map.create_bonus_armor(230, 400)
        self.assertEqual(True, checkout.bonus_armor())
        GameMap.clean_map()
    def test5_bonus_hp(self):
        create_map.create_bonus_hp(230, 400)
        self.assertEqual(True, checkout.bonus_hp())
        GameMap.clean_map()

    #
    def fire_shells_check_point(self, count_iteration, object):
        for i in range(count_iteration):
            if i == 0:
                object.fire()
                start_x = GameMap.shells[0].px
                start_y = GameMap.shells[0].py
            GameMap.shells[0].move()
        return start_x, start_y
    #

    def test3_bullet_right(self, count_iteration=5):
        create_map.create_player(230, 400, "Right")
        player = GameMap.tanks[0]

        start_x, start_y = self.fire_shells_check_point(count_iteration, player)

        self.assertEqual(True, start_x < GameMap.shells[0].px)
        self.assertEqual(True, start_y == GameMap.shells[0].py)

        GameMap.clean_map()

    def test4_bullet_left(self, count_iteration = 5):
        create_map.create_player(230, 400, "Left")
        player = GameMap.tanks[0]

        start_x, start_y = self.fire_shells_check_point(count_iteration, player)

        self.assertEqual(True, start_x > GameMap.shells[0].px)
        self.assertEqual(True, start_y == GameMap.shells[0].py)

        GameMap.clean_map()

    def test5_bullet_up(self, count_iteration=5):
        create_map.create_player(230, 400, "Up")
        player = GameMap.tanks[0]

        start_x, start_y = self.fire_shells_check_point(count_iteration, player)

        self.assertEqual(True, start_x == GameMap.shells[0].px)
        self.assertEqual(True, start_y > GameMap.shells[0].py)

        GameMap.clean_map()

    def test6_bullet_down(self, count_iteration = 5):
        create_map.create_player(230, 400, "Down")
        player = GameMap.tanks[0]

        start_x, start_y = self.fire_shells_check_point(count_iteration, player)

        self.assertEqual(True, start_x == GameMap.shells[0].px)
        self.assertEqual(True, start_y < GameMap.shells[0].py)

        GameMap.clean_map()

class test_checkout_file(unittest.TestCase):
    def test1_checkout_file(self):
        self.assertTrue(checkout.file('для теста файл.txt'))
        self.assertFalse(checkout.file('не сущ файл).txt'))

class test_clean_map(unittest.TestCase):
    def test1_clean_tank(self):
        create_map.create_player(230, 400, "Left")
        self.assertEqual(1, len(GameMap.tanks))
        GameMap.clean_map()
        self.assertEqual(0, len(GameMap.tanks))
    def test1_clean_block(self):
        create_map.create_brick(200, 200)
        create_map.create_ice(300, 200)
        create_map.create_steel(400, 200)
        self.assertEqual(3, len(GameMap.blocks))
        GameMap.clean_map()
        self.assertEqual(0, len(GameMap.blocks))


#
keys = [False] * 322

#

class test_object_move(unittest.TestCase):
    # Проверка на движение

    def test1_player_move_left(self):
        create_map.create_player(100, 100, "Left")
        player = GameMap.tanks[0]

        start_x, start_y = player.rect.x, player.rect.y

        keys[pygame.K_a] = True

        player.move(keys)

        self.assertEqual(player.rect.x, start_x - player.speed)
        self.assertEqual(player.rect.y, start_y)
        self.assertEqual(player.direction, "Left")

        keys[pygame.K_a] = False

        GameMap.clean_map()

    def test2_player_move_right(self):
        create_map.create_player(100, 100, "Left")
        player = GameMap.tanks[0]

        start_x, start_y = player.rect.x, player.rect.y

        keys[pygame.K_d] = True

        player.move(keys)

        self.assertEqual(player.rect.x, start_x + player.speed)
        self.assertEqual(player.rect.y, start_y)
        self.assertEqual(player.direction, "Right")

        keys[pygame.K_d] = False

        GameMap.clean_map()

    def test3_player_move_up(self):
        create_map.create_player(100, 100, "Left")
        player = GameMap.tanks[0]

        start_x, start_y = player.rect.x, player.rect.y

        keys[pygame.K_w] = True

        player.move(keys)

        self.assertEqual(player.rect.x, start_x)
        self.assertEqual(player.rect.y, start_y - player.speed)
        self.assertEqual(player.direction, "Up")

        keys[pygame.K_w] = False

        GameMap.clean_map()

    def test4_player_move_down(self):
        create_map.create_player(100, 100, "Left")
        player = GameMap.tanks[0]

        start_x, start_y = player.rect.x, player.rect.y

        keys[pygame.K_s] = True

        player.move(keys)

        self.assertEqual(player.rect.x, start_x)
        self.assertEqual(player.rect.y, start_y + player.speed)
        self.assertEqual(player.direction, "Down")

        keys[pygame.K_s] = False

        GameMap.clean_map()

    def test5_bot_default_random_move(self):
        pass


class test_tank_collisions(unittest.TestCase):
    #
    def object_move_check_collision_map(self, count_iteration, object, keys):
        for i in range(count_iteration):
            object.move(keys)
            if object.check_collision_map():
                return True
        return False
    #


    #
    def object_move_check_collision_block(self, count_iteration, object, keys, block):
        for i in range(count_iteration):
            object.move(keys)
            if object.check_collisions_block(block.type):
                return True
        return False
    #

    #
    def object_move_check_collision_tank(self, count_iteration, my_tank, keys, tank_bot):
        for i in range(count_iteration):
            my_tank.move(keys)
            if my_tank.check_collisions_tank(tank_bot.type):
                return True
        return False
    #

    #
    def object_move_check_collision_chasing(self, count_iteration, my_tank, keys, tank_bot):
        for i in range(count_iteration):
            my_tank.move(keys)
            if my_tank.check_collisions_tank(tank_bot.type):
                return True
        return False
    #

    def test1_player_right_collisions_map(self, count_iteration = 70):
        create_map.create_player(400, 400, "Right")

        player = GameMap.tanks[0]

        keys[pygame.K_d] = True

        self.assertEqual(True,
                         self.object_move_check_collision_map(count_iteration, player, keys))

        keys[pygame.K_d] = False
        GameMap.clean_map()

    def test2_player_left_collisions_map(self, count_iteration = 70):
        create_map.create_player(100, 100, "Left")

        player = GameMap.tanks[0]

        keys[pygame.K_a] = True

        self.assertEqual(True,
                         self.object_move_check_collision_map(count_iteration, player, keys))

        keys[pygame.K_a] = False
        GameMap.clean_map()

    def test3_player_up_collisions_map(self, count_iteration = 70):
        create_map.create_player(100, 100, "Up")

        player = GameMap.tanks[0]

        keys[pygame.K_w] = True

        self.assertEqual(True,
                         self.object_move_check_collision_map(count_iteration, player, keys))

        keys[pygame.K_w] = False
        GameMap.clean_map()

    def test4_player_down_collisions_map(self, count_iteration = 70):
        create_map.create_player(100, 400, "Down")

        player = GameMap.tanks[0]

        keys[pygame.K_s] = True

        self.assertEqual(True,
                         self.object_move_check_collision_map(count_iteration, player, keys))

        keys[pygame.K_s] = False
        GameMap.clean_map()


    def test5_player_right_collisions_brick(self, count_iteration = 70):
        create_map.create_player(100, 100, "Left")
        create_map.create_brick(200, 100)

        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_d] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration, player, keys, block))

        keys[pygame.K_d] = False
        GameMap.clean_map()

    def test6_player_left_collisions_brick(self, count_iteration = 70):
        create_map.create_player(300, 100, "Left")
        create_map.create_brick(200, 100)

        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_a] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration, player, keys, block))

        keys[pygame.K_a] = False

        GameMap.clean_map()

    def test7_player_up_collisions_brick(self, count_iteration = 70):
        create_map.create_player(200, 200, "Left")
        create_map.create_brick(200, 100)

        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_w] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration, player, keys, block))

        keys[pygame.K_w] = False
        GameMap.clean_map()

    def test8_player_down_collisions_brick(self, count_iteration = 70):
        create_map.create_player(200, 0, "Left")
        create_map.create_brick(200, 100)

        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_s] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration,
                                                player, keys, block))

        keys[pygame.K_s] = False
        GameMap.clean_map()

    def test9_player_right_collisions_steel(self, count_iteration = 70):
        create_map.create_player(100, 100, "Left")
        create_map.create_steel(200, 100)

        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_d] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration, player, keys, block))

        keys[pygame.K_d] = False
        GameMap.clean_map()

    def test10_player_left_collisions_steel(self, count_iteration = 70):
        create_map.create_player(300, 100, "Left")
        create_map.create_steel(200, 100)
        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_a] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration, player, keys, block))

        keys[pygame.K_a] = False

        GameMap.clean_map()

    def test11_player_up_collisions_steel(self, count_iteration = 70):
        create_map.create_player(200, 200, "Left")
        create_map.create_steel(200, 100)
        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_w] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration, player, keys, block))

        keys[pygame.K_w] = False
        GameMap.clean_map()

    def test12_player_down_collisions_steel(self, count_iteration = 70):
        create_map.create_player(200, 0, "Left")
        create_map.create_steel(200, 100)
        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_s] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration,
                                                player, keys, block))

        keys[pygame.K_s] = False
        GameMap.clean_map()

    def test13_player_right_collisions_ice(self, count_iteration = 70):
        create_map.create_player(100, 100, "Left")
        create_map.create_ice(200, 100)

        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_d] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration, player, keys, block))

        keys[pygame.K_d] = False
        GameMap.clean_map()

    def test14_player_left_collisions_ice(self, count_iteration = 70):
        create_map.create_player(300, 100, "Left")
        create_map.create_ice(200, 100)

        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_a] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration, player, keys, block))

        keys[pygame.K_a] = False

        GameMap.clean_map()

    def test15_player_up_collisions_ice(self, count_iteration = 70):
        create_map.create_player(200, 200, "Left")
        create_map.create_ice(200, 100)

        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_w] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration, player, keys, block))

        keys[pygame.K_w] = False
        GameMap.clean_map()

    def test16_player_down_collisions_ice(self, count_iteration = 70):
        create_map.create_player(200, 0, "Left")
        create_map.create_ice(200, 100)

        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_s] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration,
                                                player, keys, block))

        keys[pygame.K_s] = False
        GameMap.clean_map()

    #решил с этого момента не делать проверку на все 4 стороны

    def test17_player_down_collisions_bird(self, count_iteration = 70):
        create_map.create_player(200, 0, "Left")
        create_map.create_bird(200, 100)

        block = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_s] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration,
                                                player, keys, block))

        keys[pygame.K_s] = False
        GameMap.clean_map()

    def test18_player_down_collisions_bot_default(self, count_iteration = 70):
        create_map.create_player(200, 0, "Left")
        create_map.create_bot_default(200, 100, "Left")

        bot = GameMap.tanks[1]

        player = GameMap.tanks[0]

        keys[pygame.K_s] = True

        self.assertEqual(True,
                         self.object_move_check_collision_tank(count_iteration,
                                                player, keys, bot))

        keys[pygame.K_s] = False
        GameMap.clean_map()

    def test18_player_down_collisions_bot_chasing(self, count_iteration = 70):
        create_map.create_player(200, 0, "Left")
        create_map.create_bot_chasing(200, 100, "Left")

        bot = GameMap.tanks[1]

        player = GameMap.tanks[0]

        keys[pygame.K_s] = True

        self.assertEqual(True,
                         self.object_move_check_collision_chasing(count_iteration,
                                                player, keys, bot))

        keys[pygame.K_s] = False
        GameMap.clean_map()

    def test19_player_down_collisions_water(self, count_iteration = 70):
        create_map.create_player(200, 0, "Left")
        create_map.create_water(200, 100)

        water = GameMap.blocks[0]

        player = GameMap.tanks[0]

        keys[pygame.K_s] = True

        self.assertEqual(True,
                         self.object_move_check_collision_block(count_iteration,
                                                player, keys, water))

        keys[pygame.K_s] = False
        GameMap.clean_map()

class test_shells_colisions_and_kill(unittest.TestCase):
    #
    def shells_collision_brick(self, object, count_iteration):
        object.fire()
        shell = GameMap.shells[0]
        for i in range(count_iteration):
            shell.move()
            if (shell.check_collisions_block("brick")):
                return True
        return False

    #

    #
    def shells_collision_steel(self, object, count_iteration):
        object.fire()
        shell = GameMap.shells[0]
        for i in range(count_iteration):
            shell.move()
            if (shell.check_collisions_block("steel")):
                return True
        return False

    def shells_collision_tank(self, my_tank, other_tank, count_iteration):
        my_tank.fire()
        shell = GameMap.shells[0]
        for i in range(count_iteration):
            shell.move()
            if (shell.check_collisions_tank(other_tank.type)):
                return True
        return False

    def shells_collision_bird(self, object, count_iteration):
        object.fire()
        shell = GameMap.shells[0]
        for i in range(count_iteration):
            shell.move()
            if shell.check_collisions_block("bird"):
                return True
        return False

    #

    #
    def shells_collision_ice(self, object, count_iteration):
        object.fire()
        shell = GameMap.shells[0]
        for i in range(count_iteration):
            shell.move()
            if (shell.check_collisions_block("ice")):
                return True
        return False
    #

    def test1_bullet_collisions_brick(self, count_iteration=10):
        create_map.create_player(200, 100, "Left")
        create_map.create_brick(150, 100)
        player = GameMap.tanks[0]

        self.assertTrue(self.shells_collision_brick(player, count_iteration))

        remove.shells()
        remove.blocks()

        self.assertEqual(len(GameMap.blocks), 0)
        self.assertEqual(len(GameMap.shells), 0)

        GameMap.clean_map()

    def test2_bullet_collisions_steel(self, count_iteration=10):
        create_map.create_player(200, 100, "Left")
        create_map.create_steel(150, 100)
        player = GameMap.tanks[0]

        self.assertTrue(self.shells_collision_steel(player, count_iteration))

        remove.shells()
        remove.blocks()

        self.assertEqual(len(GameMap.blocks), 1)
        self.assertEqual(len(GameMap.shells), 0)

        GameMap.clean_map()

    def test3_bullet_collisions_ice(self, count_iteration=10):
        create_map.create_player(400, 100, "Left")
        create_map.create_ice(350, 100)
        player = GameMap.tanks[0]

        self.assertTrue(self.shells_collision_ice(player, count_iteration))

        remove.shells()
        remove.blocks()

        self.assertEqual(len(GameMap.blocks), 0)
        self.assertEqual(len(GameMap.shells), 1)

        GameMap.clean_map()

    def test4_bullet_collisions_bird(self, count_iteration=10):
        create_map.create_player(200, 100, "Left")
        create_map.create_bird(150, 100)
        player = GameMap.tanks[0]

        self.assertTrue(self.shells_collision_bird(player, count_iteration))

        remove.shells()
        remove.blocks()

        self.assertEqual(len(GameMap.blocks), 0)
        self.assertEqual(len(GameMap.shells), 0)

        GameMap.clean_map()

    def test5_bullet_collisions_bot_default(self, count_iteration=10):
        create_map.create_player(200, 100, "Left")
        create_map.create_bot_default(150, 100, "Left")
        player = GameMap.tanks[0]
        bot = GameMap.tanks[1]

        self.assertTrue(self.shells_collision_tank(player, bot, count_iteration))

        remove.shells()
        remove.tanks()

        self.assertEqual(len(GameMap.tanks), 1)
        self.assertEqual(len(GameMap.shells), 0)

        GameMap.clean_map()

    def test6_bullet_collisions_bot_chasing(self, count_iteration=10):
        create_map.create_player(200, 100, "Left")
        create_map.create_bot_chasing(150, 100, "Left")
        player = GameMap.tanks[0]
        bot = GameMap.tanks[1]

        self.assertTrue(self.shells_collision_tank(player, bot, count_iteration))

        remove.shells()
        remove.tanks()

        self.assertEqual(len(GameMap.tanks), 1)
        self.assertEqual(len(GameMap.shells), 0)

        GameMap.clean_map()

if __name__ == '__main__':
    unittest.main()
