import pygame


class StandardButton:
    def __init__(self, x, y, width, height, image, scale, function=None):
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.switch = False
        self.scale = scale
        self.function = function

    def click(self):
        """ Выполнение функции """
        if self.function is not None:
            self.function()

    def is_clicked(self):
        """ Проверка на нажатие """
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
