import pygame
from scenes.base import BaseWindow


class SettingsWindow(BaseWindow):
    """ Окно настроек """
    def __init__(self, game):
        super().__init__(game)