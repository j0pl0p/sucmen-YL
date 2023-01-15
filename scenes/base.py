import pygame


class BaseWindow:
    """ Базовый класс окна """
    def __init__(self, game):
        self.game = game
        self.objects = []

    def on_activate(self):
        """ Выполнение действий при смене на данную сцену """
        pass

    def on_deactivate(self):
        """ Выполнение действий при смене с данной сцены на другую """
        pass

    def process_event(self, event):
        """ Выполнение действий, связанных с нажатиями и т.д. """
        for object in self.objects:
            object.process_event(event)

    def process_logic(self):
        """ Выполнение действий, связанных с логикой объектов """
        for object in self.objects:
            object.process_logic()

    def process_draw(self):
        """ Отрисовка объектов на сцене """
        for object in self.objects:
            object.process_draw()
