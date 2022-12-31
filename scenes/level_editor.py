import pygame

from objects.field import Field
from scenes.base import BaseWindow
from scenes.game import GameWindow
from objects.board import Board
from objects.button import ButtonObject
from objects.text import TextObject
import tkinter.filedialog
import os


class LevelEditorWindow(BaseWindow):
    """ Окно редактора уровня """
    def __init__(self, game):
        super().__init__(game)

        self.board = Board(game, 10, 10)
        btn_empty = ButtonObject(game, 600, 25, 125, 50, 'black', self.change_to_empty, 'Пустое поле')
        btn_wall = ButtonObject(game, 600, 75, 125, 50, 'black', self.change_to_wall, 'Стена')
        btn_mayo = ButtonObject(game, 600, 125, 125, 50, 'black', self.change_to_mayo, 'МаZик')
        btn_viagra = ButtonObject(game, 600, 175, 125, 50, 'black', self.change_to_viagra, 'Крокодил')
        btn_save = ButtonObject(game, 600, 275, 125, 50, 'black', self.save_map, 'Сохранить')
        btn_clear = ButtonObject(game, 600, 325, 125, 50, 'black', self.clear_map, 'Очистить')
        btn_load = ButtonObject(game, 600, 375, 125, 50, 'black', self.load, 'Загрузить')
        btn_play = ButtonObject(game, 600, 425, 125, 50, 'black', self.play, 'Играть')
        btn_back = ButtonObject(game, 600, 525, 125, 50, 'black', self.back, '< Назад')

        self.objects.extend([self.board,
                             btn_empty,
                             btn_wall,
                             btn_mayo,
                             btn_viagra,
                             btn_save, btn_clear, btn_back, btn_load, btn_play])

    def change_to_empty(self):
        self.board.MODE = 'empty'

    def change_to_wall(self):
        self.board.MODE = 'wall'

    def change_to_mayo(self):
        self.board.MODE = 'mayo'

    def change_to_viagra(self):
        self.board.MODE = 'viagra'

    def save_map(self):
        name = 'map?.txt'
        i = 1
        while os.path.exists(f'maps/{name.replace("?", str(i))}'):
            i += 1
        with open(f'maps/{name.replace("?", str(i))}', 'w') as new_file:
            if self.board.save_map(new_file):
                print(f'new map file: {name.replace("?", str(i))}')

    def back(self):
        self.game.set_window(self.game.WINDOW_SETTINGS)

    def clear_map(self):
        self.board.clear_map()

    def load(self):
        top = tkinter.Tk()
        top.withdraw()
        file_name = tkinter.filedialog.askopenfilename(parent=top)
        top.destroy()
        if file_name and file_name[-4:] == '.txt':
            with open(file_name, 'r') as file:
                self.board.set_map(file)

    def play(self):
        if not self.board.get_seed():
            print('Добавьте майонезу чтобы начать')
            return
        with open('maps/temp.txt', 'w') as temp:
            self.board.save_map(temp)
        self.game.windows[self.game.WINDOW_GAME] = GameWindow(self.game, self.game.score, 'maps/temp.txt')
        self.game.set_window(self.game.WINDOW_GAME)
