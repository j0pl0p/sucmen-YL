import pygame

from buttons.standard_button import StandardButton


class SwitchButton(StandardButton):
    """ Кнопка-вариант """
    def __init__(self, x, y, image, image_pressed, scale, function=None):
        width = image.get_width()
        height = image.get_height()
        super().__init__(x, y, width, height, image, scale, function)
        self.image_pressed = pygame.transform.scale(image_pressed, (int(width * scale), int(height * scale)))
        self.other = None

    def off(self):
        """ выкл """
        self.switch = False

    def connect(self, button):
        """ Подключение к другим вариантам """
        self.other = button
        button.other = self

    def click(self):
        """ Выполнение функции """
        super().click()
        self.switch = True
        self.other.off()

    def is_clicked(self):
        """ Проверка на нажатие """
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.click()

        super().is_clicked()

    def draw(self, screen):
        """ Отрисовка """
        self.is_clicked()
        img = {
            True: self.image_pressed,
            False: self.image
        }
        self.is_clicked()
        screen.blit(img[self.switch], (self.rect.x, self.rect.y))
