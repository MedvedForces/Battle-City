import pygame
import sys
from . import checkout, remove, update, draw
from ..ui import pause
from ..core.map import GameMap


def play_game(window):
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause.stop_game()
                if event.key == pygame.K_q:
                    GameMap.clean_map()
                    return

        remove.shells()
        remove.blocks()
        remove.tanks()
        remove.bonuses()

        update.game_tanks()
        update.game_blocks()
        update.game_shells()
        update.game_bonuses()

        window.fill("black")

        draw.game_tanks(window)
        draw.game_bullets(window)
        draw.game_blocks(window)
        draw.game_tanks(window)
        draw.game_bonuses(window)

        if (GameMap.count_bird == 0 or not checkout.bot_all()):
            running = False

        pygame.draw.rect(window, pygame.Color('gray'),
                         (0, GameMap.HEIGHT, GameMap.WIDTH, 1), 1)
        pygame.draw.rect(window, pygame.Color('gray'),
                         (GameMap.WIDTH, 0, 1, GameMap.HEIGHT), 1)

        pygame.display.flip()
        clock.tick(GameMap.FPS)