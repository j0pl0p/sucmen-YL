import pygame
import pygame_gui
import sys
import os

from scenes.enter_name import EnterNameWindow
from scenes.high_scores import HighscoreWindow
from scenes.main_menu import MenuWindow
from scenes.music_select import MorgenWindow
from scenes.pause import PauseWindow
from scenes.settings import SettingsWindow
from scenes.game import GameWindow
from scenes.game_over import GameOverWindow
from scenes.level_editor import LevelEditorWindow

from system.score import Score
from system.settings import Settings
from system.sound_manager import Sounds

pygame.init()

FPS = 60
SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('SUC-MEN')
clock = pygame.time.Clock()
TIME_DELTA = clock.tick(FPS) / 1000.0


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    try:
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]
    except FileNotFoundError:
        print(f"Файл карты '{filename}' не найден в папке data")
        sys.exit()

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def terminate():
    pygame.quit()
    sys.exit()


class Game:
    """ Игра """
    size = width, height = 800, 600
    WINDOW_MENU = 0
    WINDOW_SETTINGS = 1
    WINDOW_GAME = 2
    WINDOW_GAMEOVER = 3
    WINDOW_LEVELEDITOR = 4
    WINDOW_MORGEN = 5
    WINDOW_HIGHSCORE = 6
    WINDOW_ENTERNAME = 7
    WINDOW_PAUSE = 8
    current_window_index = WINDOW_MENU

    Sounds.change_volume(0.05, channel=Sounds.channel_sound)
    Sounds.change_volume(0.1, channel=Sounds.channel_rage)
    Sounds.change_volume(0.1, channel=Sounds.channel_song)

    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        self.score = Score()
        self.settings = Settings()
        self.player_name = ''
        self.game_over = False
        self.windows = [
            MenuWindow(self),
            SettingsWindow(self),
            GameWindow(self, self.score),
            GameOverWindow(self),
            LevelEditorWindow(self),
            MorgenWindow(self),
            HighscoreWindow(self, self.score),
            EnterNameWindow(self),
            PauseWindow(self)
        ]

    @staticmethod
    def exit_button_pressed(event):
        return event.type == pygame.QUIT

    def process_exit_events(self, event):
        if Game.exit_button_pressed(event):
            self.exit_game()

    def process_all_events(self):
        for event in pygame.event.get():
            self.process_exit_events(event)
            self.windows[self.current_window_index].process_event(event)

    def process_all_logic(self):
        self.windows[self.current_window_index].process_logic()

    def set_window(self, index):
        self.windows[self.current_window_index].on_deactivate()
        self.current_window_index = index
        self.windows[self.current_window_index].on_activate()

    def process_all_draw(self):
        self.screen.fill((0, 0, 0))
        self.windows[self.current_window_index].process_draw()
        pygame.display.flip()

    def main_loop(self):
        while not self.game_over:
            self.process_all_events()
            self.process_all_logic()
            self.process_all_draw()
            pygame.time.wait(10)

    def exit_game(self):
        print('Bye bye')
        self.game_over = True


def main():
    pygame.mixer.pre_init(44100, -16, 1, 2048)
    pygame.mixer.init()
    pygame.init()
    pygame.font.init()
    game = Game()
    game.main_loop()
    sys.exit()


if __name__ == '__main__':
    main()
