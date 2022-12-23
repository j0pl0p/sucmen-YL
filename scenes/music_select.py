import pygame
from scenes.base import BaseWindow


class MorgenWindow(BaseWindow):
    """ Окно выбора музыки """
    def __init__(self, game):
        super().__init__(game)
