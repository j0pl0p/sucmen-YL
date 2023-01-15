import pygame
from objects.image import ImageObject


class Mayo(ImageObject):
    """ Гранулированный майонез """
    POINTS = 10
    filename = 'data/images/mayo.png'
    CELL_WIDTH = 18

    def __init__(self, game, x=0, y=0):
        super().__init__(game, self.filename, x, y)
        self.image_width = self.rect.width
        self.rect.width = self.CELL_WIDTH
        self.rect.height = self.CELL_WIDTH

    def process_draw(self):
        """ Отрисовка шарика гранулированного майонеза """
        self.game.screen.blit(self.image,
            (self.rect.centerx - self.image_width // 2,
             self.rect.centery - self.image_width // 2))

    def collision_list(self, objects):
        """ Получение списка объектов, с которым соприкасается майонез """
        return self.rect.collidelist(objects)


class Viagra(ImageObject):
    """ Крокодил или любой другой вид тяжёлых наркотиков, оказывающий
    сильное психотропное воздействие и принимающийся инъекционно """
    POINTS = 50
    filename = 'data/images/drug.png'
    CELL_WIDTH = 18

    def __init__(self, game, x=0, y=0):
        super().__init__(game, self.filename, x, y)
        self.image_width = self.rect.width
        self.rect.width = self.CELL_WIDTH
        self.rect.height = self.CELL_WIDTH

    def process_draw(self):
        """ Отрисовка шприца """
        self.game.screen.blit(self.image,
            (self.rect.centerx - self.image_width // 2,
             self.rect.centery - self.image_width // 2))

    def collision_list(self, objects):
        """ Получение списка объектов, с которым соприкасается шприц """
        return self.rect.collidelist(objects)
