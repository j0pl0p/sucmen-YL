from datetime import datetime

import pygame

from objects.text import TextObject
from scenes.base import BaseWindow
from objects.image import ImageObject


class GameOverWindow(BaseWindow):
    """ Game Over """
    text_format = 'Game over ({})'
    seconds_to_end = 3

    def __init__(self, game):
        super().__init__(game)
        self.last_seconds_passed = 0
        self.text = TextObject(self.game, self.game.width // 2, self.game.height // 2, self.get_gameover_text_formatted(), (255, 255, 255))
        self.objects.append(self.text)
        self.update_start_time()

    def get_gameover_text_formatted(self):
        """ Форматирование текста """
        return self.text_format.format(self.seconds_to_end - self.last_seconds_passed)

    def on_activate(self):
        """ Установка времени """
        self.update_start_time()

    def update_start_time(self):
        """ Обновление времени """
        self.time_start = datetime.now()

    def process_logic(self):
        """ Логика объектов """
        time_current = datetime.now()
        seconds_passed = (time_current - self.time_start).seconds
        if self.last_seconds_passed != seconds_passed:
            self.last_seconds_passed = seconds_passed
            self.objects[0].update_text(self.get_gameover_text_formatted())
        if seconds_passed >= self.seconds_to_end:
            self.game.set_window(self.game.WINDOW_ENTERNAME)