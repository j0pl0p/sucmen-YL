from datetime import datetime

import pygame
import time
from objects.text import TextObject
from scenes.base import BaseWindow
from objects.image import ImageObject


class DeathAnimationWindow(BaseWindow):
    """ чоо """

    def __init__(self, game):
        super().__init__(game)

    def update_start_time(self):
        self.time_start = datetime.now()

    def process_logic(self):
        img1 = pygame.image.load('data/images/huggy_anim/huggy(1).png')
        self.game.screen.blit(img1, (0, 67))
        pygame.display.flip()
        time.sleep(2)
        img2 = pygame.image.load('data/images/huggy_anim/huggy(2).png')
        self.game.screen.blit(img2, (0, 67))
        pygame.display.flip()
        time.sleep(2)
        img3 = pygame.image.load('data/images/huggy_anim/huggy(3).png')
        img4 = pygame.image.load('data/images/huggy_anim/huggy(4).png')
        for _ in range(20):
            self.game.screen.blit(img3, (0, 67))
            pygame.display.flip()
            time.sleep(0.1)
            self.game.screen.blit(img4, (0, 67))
            pygame.display.flip()
            time.sleep(0.1)

        self.game.set_window(self.game.WINDOW_GAMEOVER)
