import pygame
from scenes.base import BaseWindow
from objects.button import ButtonObject
from objects.image import ImageObject


class MenuWindow(BaseWindow):
    """ Главное меню """
    def __init__(self, game):
        super().__init__(game)
        self.surface = pygame.Surface((1000, 750))
        self.surface.set_alpha(0)
        self.surface.fill((0, 0, 0))
        background = ImageObject(game, 'data/images/mm_background.png', 0, 0)
        logo = ImageObject(game, 'data/images/logo.png', 183, 15)
        self.objects.append(background)
        self.objects.append(logo)

    def process_draw(self):
        super().process_draw()
        self.game.screen.blit(self.surface, (0, 0))

    def start_game(self):
        pass

    def open_settings(self):
        pass

