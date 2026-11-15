import pygame
import sys
import pause
import checkout
from map import GameMap
import levels
from levels import create_levels_use_read_from_file
from play_game import play_game
from tank import Player
import remove
import update
from all_button_dictionary import buttons_custom_level
from all_object_number_dictionary import all_object_number, all_object_symbol
from button import ImageButton
import draw


def get_rotated_image(image, direction):
    return pygame.transform.rotate(image,
                                   GameMap.ROTATIONS[direction])

def draw_on_map(image, rect, window):
    window.blit(image, rect)

def save_map(map_width, map_height, map):
    file = open('map.txt', 'w')

    for row in range(map_height):
        for col in range(map_width):
            file.write(all_object_symbol[map[row][col]])
    print('Карта сохранена!')
    file.close()


def load_map(map_width, map):
    try:
        file = open('map.txt', 'r')
        row, col = 0, 0
        for line in file:
            for s in line:
                if s != '\n':
                    map[row][col] = all_object_symbol.index(s)
                    col += 1
                    if col >= map_width:
                        row += 1
                        col = 0
        file.close()

        print('Карта загружена!')
    except:
        print('Файл карты не найден!')

def create_object_on_map(map_width, map_height, map, cell_size, window):
    object_handlers = {
        'player': lambda x, y, direction: _draw_player(x, y, direction),
        'brick' : lambda x, y, direction: _draw_brick(x, y, direction),
        'steel': lambda x, y, direction: _draw_steel(x, y, direction),
        'ice': lambda x, y, direction: _draw_ice(x, y, direction),
        'water': lambda x, y, direction: _draw_water(x, y, direction),
        'bonus_hp': lambda x, y, direction: _draw_bonus_hp(x, y, direction),
        'bonus_armor': lambda x, y, direction: _draw_bonus_armor(x, y, direction),
        'bird': lambda x, y, direction: _draw_bird(x, y, direction),
        'bot_default': lambda x, y, direction: _draw_bot_default(x, y, direction),
        'bot_chasing' : lambda x, y, direction: _draw_bot_chasing(x, y, direction),
    }

    def _draw_player(x, y, direction):
        image = get_rotated_image(GameMap.img_tanks[9], direction)
        rect = image.get_rect(center=(x + 16, y + 16))
        window.blit(image, rect)

    def _draw_ice(x, y, direction):
        image = get_rotated_image(GameMap.img_ice, direction)
        rect = image.get_rect(center=(x + 16, y + 16))
        window.blit(image, rect)

    def _draw_water(x, y, direction):
        image = get_rotated_image(GameMap.img_water, direction)
        rect = image.get_rect(center=(x + 16, y + 16))
        window.blit(image, rect)

    def _draw_bird(x, y, direction):
        image = get_rotated_image(GameMap.img_bird, direction)
        rect = image.get_rect(center=(x + 16, y + 16))
        window.blit(image, rect)

    def _draw_brick(x, y, direction):
        image = get_rotated_image(GameMap.img_brick, direction)
        rect = image.get_rect(center=(x + 16, y + 16))
        window.blit(image, rect)

    def _draw_bonus_hp(x, y, direction):
        image = get_rotated_image(GameMap.img_bonus_hp, direction)
        rect = image.get_rect(center=(x + 16, y + 16))
        window.blit(image, rect)

    def _draw_bonus_armor(x, y, direction):
        image = get_rotated_image(GameMap.img_bonus_armor, direction)
        rect = image.get_rect(center=(x + 16, y + 16))
        window.blit(image, rect)

    def _draw_steel(x, y, direction):
        image = get_rotated_image(GameMap.img_steel, direction)
        rect = image.get_rect(center=(x + 16, y + 16))
        window.blit(image, rect)

    def _draw_bot_default(x, y, direction):
        image = get_rotated_image(GameMap.img_tanks[8], direction)
        rect = image.get_rect(center=(x + 16, y + 16))
        window.blit(image, rect)

    def _draw_bot_chasing(x, y, direction):
        image = get_rotated_image(GameMap.img_tanks[7], direction)
        rect = image.get_rect(center=(x + 16, y + 16))
        window.blit(image, rect)

    for row in range(map_height):
        for col in range(map_width):
            x, y = col * cell_size, row * cell_size
            cell_value = map[row][col]

            for (obj_type, direction), number in all_object_number.items():
                if number == cell_value:
                    if obj_type in object_handlers:
                        object_handlers[obj_type](x, y, direction)
                    break
            else:
                pygame.draw.rect(window, pygame.Color('gray'),
                                 (x, y, cell_size, cell_size), 1)


def custom_level(window):
    button_player = buttons_custom_level["button_player"]
    button_brick = buttons_custom_level["button_brick"]
    button_steel = buttons_custom_level["button_steel"]
    button_ice = buttons_custom_level["button_ice"]
    button_bird = buttons_custom_level["button_bird"]
    button_water = buttons_custom_level["button_water"]
    button_bonus_hp = buttons_custom_level["button_bonus_hp"]
    button_bonus_armor = buttons_custom_level["button_bonus_armor"]
    button_bot_default = buttons_custom_level["button_bot_default"]
    button_bot_chasing = buttons_custom_level["button_bot_chasing"]
    button_play = buttons_custom_level["button_play"]
    button_delete_all = buttons_custom_level["button_delete_all"]
    clock = pygame.time.Clock()

    cell_size = 32
    map_width, map_height = GameMap.WIDTH // cell_size, GameMap.HEIGHT // cell_size

    buttons = [button_player,
               button_brick,
               button_play,
               button_steel,
               button_bonus_hp,
               button_water,
               button_bonus_armor,
               button_bot_default,
               button_bot_chasing,
               button_ice,
               button_bird,
               button_delete_all]

    map = [[0] * map_width for i in range(map_height)]

    running = True

    current_object = None
    base_current_object = None

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_player.handle_event(event):
                    print("Выбран player!")
                    current_object = all_object_number[('player','Up')]
                    base_current_object = all_object_number[('player','Up')]
                if button_play.handle_event(event):
                    if not checkout.file('map.txt'):
                        print("Нужно создать карту, чтобы поиграть")
                    else:
                        levels.create_levels_use_read_from_file("map.txt", map_width, map_height)
                        if checkout.bird() and checkout.bot_all():
                            print("ЕЕЕ новый уровень!")
                            play_game(window)
                            levels.clean_level()
                        elif not checkout.bird():
                            print("Необходимо поставить птичку друг)")
                        else:
                            print("Необходимо поставить врагов друг)")
                if button_bot_default.handle_event(event):
                    print("Выбран bot_default!")
                    current_object = all_object_number[('bot_default', 'Up')]
                    base_current_object = all_object_number[('bot_default', 'Up')]
                if button_bot_chasing.handle_event(event):
                    print("Выбран bot_chasing!")
                    current_object = all_object_number[('bot_chasing', 'Up')]
                    base_current_object = all_object_number[('bot_chasing', 'Up')]
                if button_water.handle_event(event):
                    print("Выбран water!")
                    current_object = all_object_number[('water', 'Up')]
                    base_current_object = all_object_number[('water', 'Up')]
                if button_bird.handle_event(event):
                    print('Выбран bird')
                    current_object = all_object_number[('bird', 'Up')]
                    base_current_object = all_object_number[('bird', 'Up')]
                if button_bonus_hp.handle_event(event):
                    print('Выбран bonus_hp')
                    current_object = all_object_number[('bonus_hp', 'Up')]
                    base_current_object = all_object_number[('bonus_hp', 'Up')]
                if button_bonus_armor.handle_event(event):
                    print('Выбран bonus_armor')
                    current_object = all_object_number[('bonus_armor', 'Up')]
                    base_current_object = all_object_number[('bonus_armor', 'Up')]
                if button_steel.handle_event(event):
                    print("Выбран steel!")
                    current_object = all_object_number[('steel', 'Up')]
                    base_current_object = all_object_number[('steel', 'Up')]
                if button_brick.handle_event(event):
                    print("Выбран brick!")
                    current_object = all_object_number[('brick','Up')]
                    base_current_object = all_object_number[('brick','Up')]
                if button_ice.handle_event(event):
                    print("Выбран ice!")
                    current_object = all_object_number[('ice', 'Up')]
                    base_current_object = all_object_number[('ice', 'Up')]
                if button_delete_all.handle_event(event):
                    map = [[0] * map_width for i in range(map_height)]
                    print("Вы удалили все!")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return
                if event.key == pygame.K_s:
                    save_map(map_width, map_height, map)
                if event.key == pygame.K_l:
                    load_map(map_width, map)
                if event.key == pygame.K_z:
                    current_object += 1
                    if (current_object != base_current_object
                            and (current_object - base_current_object) == 4):
                        current_object -= 4


        window.fill("black")

        for btn in buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(window)

        mouse_px, mouse_py = pygame.mouse.get_pos()
        a1, a2, a3 = pygame.mouse.get_pressed()

        mouse_row, mouse_col = mouse_py // cell_size, mouse_px // cell_size

        if 0 < mouse_px < GameMap.WIDTH and 0 < mouse_py < GameMap.HEIGHT:
            if a1 and current_object != None:
                map[mouse_row][mouse_col] = current_object
            elif a3:
                map[mouse_row][mouse_col] = 0

        create_object_on_map(map_width, map_height, map, cell_size, window)

        pygame.display.flip()
        clock.tick(GameMap.FPS)
