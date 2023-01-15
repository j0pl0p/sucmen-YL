from datetime import datetime

import pygame
import time
from objects.text import TextObject
from scenes.base import BaseWindow
from scenes.game import GameWindow
from objects.image import ImageObject
from system.sound_manager import Sounds


class DeathAnimationWindow(BaseWindow):
    """ Окно анимации проигрыша """

    def __init__(self, game):
        super().__init__(game)
        self.name = None

    def process_logic(self):
        """ Сама анимация """
        Sounds.pause()
        img1 = pygame.image.load(f'data/images/{self.name}_anim/{self.name} (1).png')
        self.game.screen.blit(img1, (0, 67))
        pygame.display.flip()
        time.sleep(1)
        if self.game.settings.music:
            Sounds.play_song('death')
        img2 = pygame.image.load(f'data/images/{self.name}_anim/{self.name} (2).png')
        self.game.screen.blit(img2, (0, 67))
        pygame.display.flip()
        time.sleep(3.4)
        img3 = pygame.image.load(f'data/images/{self.name}_anim/{self.name} (3).png')
        img4 = pygame.image.load(f'data/images/{self.name}_anim/{self.name} (4).png')
        for _ in range(10):
            self.game.screen.blit(img3, (0, 67))
            pygame.display.flip()
            time.sleep(0.1)
            self.game.screen.blit(img4, (0, 67))
            pygame.display.flip()
            time.sleep(0.1)

        self.name = None
        Sounds.pause()
        self.game.set_window(self.game.WINDOW_GAMEOVER)

    def set_killer(self, killer):
        """ Установка нужного мутанта (цветов) """
        if killer is not None:
            self.name = killer
