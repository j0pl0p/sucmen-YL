import pygame
from scenes.base import BaseWindow
from objects.image import ImageObject
from objects.field import Field
from objects.player import Player
from objects.text import TextObject
from objects.monsters.monsters import Larry, Kissy, Huggy, Wunk
from system.sound_manager import Sounds


class GameWindow(BaseWindow):
    """ Окно с игрой """
    start = False

    def __init__(self, game, score, map_path='maps/default.txt'):
        super().__init__(game)
        self.field = Field(self.game, 10, 10, map_path)
        self.objects.append(self.field)
        self.player = Player(self.game, self.field, 18 * 15, 18 * 24)
        self.monsters = [Larry(self.game, self.field),
                         Kissy(self.game, self.field),
                         Huggy(self.game, self.field),
                         Wunk(self.game, self.field)]
        self.objects += self.monsters
        self.objects.append(self.player)
        self.score = score
        self.huggy_bounty = 200

    def process_logic(self):
        if not self.start:
            return
        super().process_logic()
        # проверка на мутантов
        for huggy in self.monsters:
            if huggy.collide_with(self.player):
                if not huggy.frightened_is_active:
                    self.game.set_window(self.game.WINDOW_DEATH)
                    for m in self.monsters:
                        m.reset()
                else:
                    huggy.reset()
                    if self.game.settings.sound:
                        Sounds.play_sound('spears')
                    self.score.increase_on(self.huggy_bounty)
                    self.huggy_bounty *= 2
        # условие победы
        if self.field.seeds_count == 0:
            self.game.set_window(self.game.WINDOW_GAMEOVER)
            # self.reset()

    def process_event(self, event):
        super().process_event(event)
        if event.type != pygame.KEYDOWN:
            return
        if not self.start:
            if event.type == pygame.KEYDOWN:
                self.start = True
        if event.key == pygame.K_ESCAPE:
            self.game.set_window(self.game.WINDOW_PAUSE)
        if event.key == pygame.K_p:
            self.game.set_window(self.game.WINDOW_PAUSE)

    def process_draw(self):
        super().process_draw()
        text1 = TextObject(self.game, 600, 100, '1UP', pygame.Color('white'))
        text2 = TextObject(self.game, 600, 140, str(self.score.current_points()), pygame.Color('white'))
        text3 = TextObject(self.game, self.game.width // 2, self.game.height // 2 - 60,
                           'Нажмите любую клавишу чтобы продолжить', pygame.Color('red'))
        text1.process_draw()
        text2.process_draw()
        # pygame.draw.rect(self.game.screen, 'black', (10, 18 * 13 + 10, 36, 54))
        # pygame.draw.rect(self.game.screen, 'black', (26 * 18 + 10, 18 * 13 + 10, 36, 54))
        if not self.start:
            text3.process_draw()

    def on_activate(self):
        super().on_activate()
        self.start = False
        if self.game.settings.music:
            if Sounds.current_song() not in ['ice', 'cadillac']:
                Sounds.play_song('ice' if self.game.settings.song == 1 else 'cadillac')

    def reset(self):
        self.score.reset()
        self.field.load_map()
        self.player.reset_position()
        for m in self.monsters:
            m.reset()

