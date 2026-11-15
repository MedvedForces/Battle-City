import pygame

from map import GameMap
from menu_interface import main_menu

WIDTH, HEIGHT = 512, 512
SIZE = 32

def initialization():
    pygame.init()
    GameMap.load_resources()


def main():
    initialization()

    window = pygame.display.set_mode((WIDTH, HEIGHT))
    fontUI = pygame.font.Font(None, 30)
    main_menu(window, WIDTH, HEIGHT, fontUI)
    pygame.quit()


if __name__ == "__main__":
    main()