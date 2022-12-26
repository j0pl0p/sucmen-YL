import pygame

from buttons.back_button import BackButton
from objects.button import ButtonObject
from scenes.base import BaseWindow


class MorgenWindow(BaseWindow):
    """ Окно выбора музыки """
    def __init__(self, game):
        super().__init__(game)

        self.back_button = BackButton(5, 20, self.game, self.function_back, text='Назад')
        btn_morgen_ice = ButtonObject(game, 320, 150, 150, 50, 'black', self.function_apply, text='Эй уу айс цепь на мне это айс')
        btn_morgen_cadillac = ButtonObject(game, 320, 250, 150, 50, 'black', self.function_apply, text='Как дела как дела это новый кадилак')

        self.objects.append(btn_morgen_cadillac)
        self.objects.append(btn_morgen_ice)

    def function_back(self):
        self.game.set_window(self.game.WINDOW_SETTINGS)

    def function_apply(self):
        # выбор функции
        self.game.set_window(self.game.WINDOW_SETTINGS)

    def process_draw(self):
        super().process_draw()
        self.back_button.draw(self.game.screen)
