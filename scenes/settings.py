import pygame
from scenes.base import BaseWindow
from objects.button import ButtonObject
from objects.image import ImageObject
from objects.text import TextObject


class SettingsWindow(BaseWindow):
    """ Окно настроек """
    def __init__(self, game):
        super().__init__(game)
        self.surface = pygame.Surface((1000, 750))
        self.surface.set_alpha(0)
        self.surface.fill((0, 0, 0))

        background = ImageObject(game, 'data/images/stg_background.png', 0, 0)
        name = TextObject(game, 400, 60, 'Настройки', 'white', 'Comic Sans MS', 35)
        btn_morgen = ButtonObject(game, 320, 250, 150, 50, 'black', self.open_morgen, text='Выбрать музыку')
        btn_editor = ButtonObject(game, 320, 350, 150, 50, 'black', self.open_editor, text='Редактор уровней')
        btn_back = ButtonObject(game, 320, 500, 150, 50, 'black', self.back, text='< Назад')

        self.objects.append(background)
        self.objects.append(name)
        self.objects.append(btn_morgen)
        self.objects.append(btn_editor)
        self.objects.append(btn_back)

    def process_draw(self):
        super().process_draw()
        self.game.screen.blit(self.surface, (0, 0))

    def open_morgen(self):
        pass

    def open_editor(self):
        pass

    def back(self):
        self.game.set_window(self.game.WINDOW_MENU)