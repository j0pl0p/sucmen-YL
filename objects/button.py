import pygame
from objects.base import DrawableObject
from buttons.imported_button import ImportedButton


pygame.init()


class ButtonObject(DrawableObject):
    """ Класс кнопки """
    BUTTON_STYLE = {
        "hover_color": 'black',
        "clicked_color": 'black',
        "clicked_font_color": 'grey',
        "hover_font_color": 'red',
        "font": pygame.font.SysFont('Comic Sans MS', 24)
    }

    def __init__(self, game, x, y, width, height, color, function, text):
        super().__init__(game)
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.button = ImportedButton((x, y, width, height), color, function, text=text, **self.BUTTON_STYLE) # загрузка скопированной кнопки

    def process_event(self, event):
        self.button.check_event(event)

    def process_draw(self):
        self.button.update(self.game.screen)
