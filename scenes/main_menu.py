import datetime

import pygame

from scenes.game import GameWindow
from system.sound_manager import Sounds
from scenes.base import BaseWindow
from objects.button import ButtonObject
from objects.image import ImageObject


class MenuWindow(BaseWindow):
    """ Главное меню """
    def __init__(self, game):
        super().__init__(game)
        self.surface = pygame.Surface((1000, 750))
        self.surface.set_alpha(0)
        self.surface.fill((0, 0, 0))

        background = ImageObject(game, 'data/images/mm_background.png', 0, 0)
        logo = ImageObject(game, 'data/images/logo.png', 183, 15)
        btn_new_game = ButtonObject(game, 320, 250, 150, 50, 'black', self.start_game, text='Новая игра')
        btn_settings = ButtonObject(game, 320, 350, 150, 50, 'black', self.open_settings, text='Настройки')
        btn_highscores = ButtonObject(self.game, 320, 450, 150, 50, 'black', self.open_highscores, text='Рекорды')

        self.objects.append(background)
        self.objects.append(logo)
        self.objects.append(btn_new_game)
        self.objects.append(btn_settings)
        self.objects.append(btn_highscores)

        if self.game.settings.music:
            Sounds.play_song('mainmenu')

    def process_draw(self):
        super().process_draw()
        self.game.screen.blit(self.surface, (0, 0))

    def start_game(self):
        self.game.set_window(self.game.WINDOW_GAME)

    def open_settings(self):
        self.game.set_window(self.game.WINDOW_SETTINGS)

    def open_highscores(self):
        self.game.set_window(self.game.WINDOW_HIGHSCORE)

    def on_activate(self):
        self.game.score.reset()
        self.game.windows[self.game.WINDOW_GAME] = GameWindow(self.game, self.game.score)
        if self.game.settings.music:
            print(Sounds.current_song())
            if Sounds.current_song() != 'mainmenu':
                Sounds.play_song('mainmenu')
        else:
            Sounds.pause(channel=Sounds.channel_song)

