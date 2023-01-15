import pygame

from buttons.buttons_collection import ButtonsCollection
from scenes.base import BaseWindow
from system.sound_manager import Sounds


class MorgenWindow(BaseWindow):
    """ Окно выбора музыки """
    def __init__(self, game):
        super().__init__(game)
        self.screen = game.screen
        self.buttons = ButtonsCollection(game)

    def process_event(self, event):
        """ Обработка нажатий """
        super().process_event(event)
        if event.type != pygame.KEYDOWN:
            return
        if event.type == pygame.K_ESCAPE:
            self.buttons.function_back()
            self.game.sound.mus_switch()

    def process_draw(self):
        """ Отрисовка """
        self.buttons.prev_settings()
        super().process_draw()
        for btn in self.buttons.buttons:
            btn.draw(self.screen)
