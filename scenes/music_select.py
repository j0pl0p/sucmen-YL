import pygame

from buttons.back_button import BackButton
from objects.button import ButtonObject
from objects.text import TextObject
from scenes.base import BaseWindow


class MorgenWindow(BaseWindow):
    """ Окно выбора музыки """
    def __init__(self, game):
        super().__init__(game)
        text = {
            'ice': 'Эй уу айс цепь на мне это айс',
            'cadillac': 'Как дела как дела это новый кадилак'
        }

        text_chosen = TextObject(game, 500, 500, f'Выбрано:     {text["ice"]}', 'white', 'Comic Sans MS', 33)
        btn_morgen_ice = ButtonObject(game, 320, 150, 150, 50, 'black', lambda: self.function_apply(text['ice']), text=text['ice'])
        btn_morgen_cadillac = ButtonObject(game, 320, 200, 150, 50, 'black', lambda: self.function_apply(text['cadillac']), text=text['cadillac'])

        self.back_button = BackButton(5, 20, self.game, self.function_back, text='Назад')
        self.objects.append(btn_morgen_cadillac)
        self.objects.append(btn_morgen_ice)
        self.objects.append(text_chosen)

    def function_back(self):
        self.game.set_window(self.game.WINDOW_SETTINGS)

    def function_apply(self, title):
        # выбор функции
        self.objects[2] = TextObject(self.game, 350, 500, f'Выбрано:      {title}', 'white', 'Comic Sans MS', 35)
        self.game.set_window(self.game.WINDOW_SETTINGS)

    def process_draw(self):
        super().process_draw()
        self.back_button.draw(self.game.screen)
