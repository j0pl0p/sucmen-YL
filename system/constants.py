import pygame


class Constants:
    RED = pygame.color.Color('red')
    YELLOW = pygame.color.Color('yellow')
    BLUE = pygame.color.Color('blue')
    GREEN = pygame.color.Color('green')
    BLACK = pygame.color.Color('black')
    WHITE = pygame.color.Color('white')
    ORANGE = pygame.color.Color('orange')

    pygame.font.init()
    FONT = 'system/bank_ghothic_medium.ttf'

    SETTINGS_PATH = 'game/settings.json'
    SAVE_PATH = 'game/data.txt'
