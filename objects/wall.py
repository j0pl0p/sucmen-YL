import pygame
from objects.base import DrawableObject


class Wall(DrawableObject):
    """ Стена """
    CELL_WIDTH = 18

    def __init__(self, game, x, y):
        super().__init__(game)
        self.move(x, y)
        self.rect.width = self.CELL_WIDTH
        self.rect.height = self.CELL_WIDTH

    def process_draw(self):
        """ Отрисовка """
        pygame.draw.rect(self.game.screen, '#780000', self.rect, 0)


class Empty(DrawableObject):
    """ Пустое поле/коридор """
    CELL_WIDTH = 18

    def __init__(self, game, x, y):
        super().__init__(game)
        self.move(x, y)
        self.rect.width = self.CELL_WIDTH
        self.rect.height = self.CELL_WIDTH

    def process_draw(self):
        """ Отрисовка """
        pygame.draw.rect(self.game.screen, 'black', self.rect, 0)


class TeleportWall(Wall):
    """ Переход между краями уровня """
    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def collision_list(self, objects):
        """ Получение списка объектов, с которыми соприкасается стена-телепорт """
        return self.rect.collidelist(objects)

    def process_draw(self):
        """ Отрисовка """
        pygame.draw.rect(self.game.screen, '#000000', self.rect, 0)

