import sys

import pygame
from ..game import remove, levels, draw, update
from . import pause
from .custom_level import custom_level
from ..game.create_map import create_steel
from ..core.map import GameMap
from .button import ImageButton
from ..game.play_game import play_game
from .all_button_dictionary import buttons_setting_menu, buttons_main_menu

def setting_menu(window, WIDTH, HEIGHT, fontUI):
    # загрузка кнопок
    button_audio = buttons_setting_menu["button_audio"]
    button_video = buttons_setting_menu["button_video"]
    button_back = buttons_setting_menu["button_back"]

    buttons = [button_audio, button_video, button_back]

    running = True
    while running:
        window.fill((0, 0, 0))

        text_surface = fontUI.render("SETTINGS", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 50))
        window.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.handle_event(event):
                    return
                elif button_audio.handle_event(event):
                    print("Настройки аудио")
                elif button_video.handle_event(event):
                    print("Настройки видео")

        for btn in buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(window)

        pygame.display.flip()


def main_menu(window, WIDTH, HEIGHT, fontUI):
    # загрузка кнопок
    button_level1 = buttons_main_menu["button_level1"]
    button_level2 = buttons_main_menu["button_level2"]
    button_create_level = buttons_main_menu["button_create_level"]
    button_settings= buttons_main_menu["button_settings"]

    buttons = [button_level1, button_level2, button_create_level, button_settings]

    running = True
    while running:
        window.fill((0, 0, 0))

        text_surface = fontUI.render("MENU", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH / 2, 50))
        window.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_level1.handle_event(event):
                    levels.level1()
                    play_game(window)
                    levels.clean_level()
                elif button_level2.handle_event(event):
                    levels.level2()
                    play_game(window)
                    levels.clean_level()
                elif button_settings.handle_event(event):
                    setting_menu(window, WIDTH, HEIGHT, fontUI)
                elif button_create_level.handle_event(event):
                    #levels.level1()
                    print("Привет, тут ты можешь создать свой уровень)\n"
                          "В центре ты видишь карту, на которую можно ставить блоки и танки\n"
                          "Справа паналька, где ты можешь выбрать танк и блок, не забудь про птичку)\n"
                          "Чтобы выбрать объект тыкни на него, затем правой левой кнопкой мыши поставь на карту\n"
                          "Чтобы удалить объект нажми на него левой кнопкой мыши\n"
                          "Чтобы повернуть объект нажми z, а затем поставь\n"
                          "s - сохранение карты, l - загрузка\n"
                          "Чтобы очистить карту нажми на крестик\n"
                          "Чтобы попробовать поиграть нажми в правый нижний угол\n"
                          "Удачи!!!"
                          )
                    custom_level(window)

        for btn in buttons:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(window)

        pygame.display.flip()