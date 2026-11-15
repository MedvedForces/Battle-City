import pygame
import sys

def stop_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_ESCAPE):
                return