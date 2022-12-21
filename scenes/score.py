import pygame
from data.scenes.base import BaseWindow


class ScoreWindow(BaseWindow):
    """ Таблица рекордов """
    def __init__(self):
        super().__init__()
