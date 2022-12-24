import pygame
from scenes.base import BaseWindow


class GameWindow(BaseWindow):
    """ Окно с игрой """
    def __init__(self, game):
        super().__init__(game)
