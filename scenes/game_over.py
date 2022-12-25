import pygame
from scenes.base import BaseWindow
from objects.image import ImageObject


class GameOverWindow(BaseWindow):
    """ Конец игры! """
    def __init__(self, game):
        super().__init__(game)

        background = ImageObject(game, 'data/images/gameover.png', 0, 0)
        self.objects.append(background)
