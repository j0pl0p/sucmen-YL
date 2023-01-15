import pygame


class DrawableObject:
    """ Базовый класс объекта """
    def __init__(self, game):
        self.game = game
        self.rect = pygame.rect.Rect(0, 0, 0, 0)

    def move(self, x, y):
        """ Сдвинуть к координате (х, у) """
        self.rect.x = x
        self.rect.y = y

    def move_center(self, x, y):
        """ Сдвинуть центр к координате (х, у) """
        self.rect.centerx = x
        self.rect.centery = y

    def process_event(self, event):
        pass

    def process_logic(self):
        pass

    def process_draw(self):
        pass
