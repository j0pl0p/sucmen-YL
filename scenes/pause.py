import pygame

from objects.button import ButtonObject
from objects.text import TextObject
from scenes.base import BaseWindow


class PauseWindow(BaseWindow):
    def __init__(self, game):
        super().__init__(game)
        self.objects.append(TextObject(self.game, self.game.width // 2, self.game.height //2 - 200, 'ПАУЗА', (255, 255, 255)))
        self.objects.append(ButtonObject(self.game, self.game.width // 2 - 100, self.game.height // 2 - 60, 200, 50, (0, 0, 0), self.resume, text='Продолжить'))
        self.objects.append(ButtonObject(self.game, self.game.width // 2 - 100, self.game.height // 2, 200, 50, (0, 0, 0), self.quit, text='Выйти в меню'))

    def process_event(self, event):
        super().process_event(event)
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_ESCAPE:
            self.game.set_window(self.game.WINDOW_GAME)

    def resume(self):
        self.game.set_window(self.game.WINDOW_GAME)

    def quit(self):
        self.game.windows[self.game.WINDOW_GAME].reset()
        self.game.set_window(self.game.WINDOW_MENU)