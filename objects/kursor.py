import pygame

from objects.text import TextObject
from datetime import datetime


class KursorObject(TextObject):
    def __init__(self, game, x, y, text='_', color=pygame.color.Color(255, 255, 255)):
        super().__init__(game, x, y, text, color)
        self.update_start_time()
        self.visible = True
        self.time_start = datetime.now()

    def update_start_time(self):
        self.time_start = datetime.now()

    def process_logic(self):
        time_current = datetime.now()
        if (time_current - self.time_start).seconds % 2 == 0:
            self.visible = True
        else:
            self.visible = False

    def process_draw(self):
        if self.visible:
            self.game.screen.blit(self.surface, self.rect)
