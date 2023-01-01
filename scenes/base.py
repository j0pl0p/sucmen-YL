import pygame


class BaseWindow:
    """ Базовый класс окна """
    def __init__(self, game):
        self.game = game
        self.objects = []

    def on_activate(self):
        pass

    def on_deactivate(self):
        pass

    def process_event(self, event):
        for object in self.objects:
            object.process_event(event)

    def process_logic(self):
        for object in self.objects:
            object.process_logic()

    def process_draw(self):
        for object in self.objects:
            object.process_draw()
