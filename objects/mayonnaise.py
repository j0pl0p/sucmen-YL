import pygame
from objects.image import ImageObject


class Mayo(ImageObject):
    POINTS = 10
    filename = 'images/mayo.png'
    CELL_WIDTH = 18

    def __init__(self, game, x=0, y=0):
        super().__init__(game, self.filename, x, y)
        self.image_width = self.rect.width
        self.rect.width = self.CELL_WIDTH
        self.rect.height = self.CELL_WIDTH

    def process_draw(self):
        self.game.screen.blit(self.image,
            (self.rect.centerx - self.image_width // 2,
             self.rect.centery - self.image_width // 2))

    def collision_list(self, objects):
        return self.rect.collidelist(objects)


class Viagra(ImageObject):
    POINTS = 50
    filename = 'images/drug.png'
    CELL_WIDTH = 18

    def __init__(self, game, x=0, y=0):
        super().__init__(game, self.filename, x, y)
        self.image_width = self.rect.width
        self.rect.width = self.CELL_WIDTH
        self.rect.height = self.CELL_WIDTH

    def process_draw(self):
        self.game.screen.blit(self.image,
            (self.rect.centerx - self.image_width // 2,
             self.rect.centery - self.image_width // 2))

    def collision_list(self, objects):
        return self.rect.collidelist(objects)
