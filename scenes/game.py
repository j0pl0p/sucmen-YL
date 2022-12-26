import pygame
from scenes.base import BaseWindow
from objects.image import ImageObject
from objects.field import Field
from objects.player import Player
from objects.text import TextObject


class GameWindow(BaseWindow):
    """ Окно с игрой """
    start = False

    def __init__(self, game, score):
        super().__init__(game)
        self.field = Field(self.game, 10, 10, 'maps/default.txt')
        self.objects.append(self.field)
        self.player = Player(self.game, self.field, 18 * 15, 18 * 24)
        self.objects.append(self.player)
        self.score = score

    def process_logic(self):
        if not self.start:
            return
        super().process_logic()
        # условие победы
        if self.field.seeds_count == 0:
            self.game.set_scene(self.game.WINDOW_GAMEOVER)
            self.reset()

    def process_event(self, event):
        super().process_event(event)
        if event.type != pygame.KEYDOWN:
            return
        if not self.start:
            if event.type == pygame.KEYDOWN:
                self.start = True

    def process_draw(self):
        super().process_draw()
        text1 = TextObject(self.game, 600, 100, '1UP', pygame.Color('white'))
        text2 = TextObject(self.game, 600, 140, str(self.score.current_points()), pygame.Color('white'))
        text3 = TextObject(self.game, self.game.width // 2, self.game.height // 2 - 60,
                           'Нажмите любую клавишу чтобы продолжить', pygame.Color('red'))
        text1.process_draw()
        text2.process_draw()
        pygame.draw.rect(self.game.screen, 'black', (10, 18 * 13 + 10, 36, 54))
        pygame.draw.rect(self.game.screen, 'black', (26 * 18 + 10, 18 * 13 + 10, 36, 54))
        if not self.start:
            text3.process_draw()

    def on_activate(self):
        super().on_activate()
        self.start = False

    def reset(self):
        self.score.reset()
        self.field.load_map()
        self.player.reset_position()

