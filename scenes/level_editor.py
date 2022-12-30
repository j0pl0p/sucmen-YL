import pygame
from scenes.base import BaseWindow
from objects.board import Board
from objects.button import ButtonObject
from objects.text import TextObject
import os


class LevelEditorWindow(BaseWindow):
    """ Окно редактора уровня """
    def __init__(self, game):
        super().__init__(game)

        self.board = Board(game, 10, 10)
        name = TextObject(game, 655, 20, 'leVelEditor v0.002', 'white', size=25 )
        btn_empty = ButtonObject(game, 600, 100, 125, 50, 'black', self.change_to_empty, 'Пустое поле')
        btn_wall = ButtonObject(game, 600, 150, 125, 50, 'black', self.change_to_wall, 'Стена')
        btn_mayo = ButtonObject(game, 600, 200, 125, 50, 'black', self.change_to_mayo, 'МайонеZ')
        btn_viagra = ButtonObject(game, 600, 250, 125, 50, 'black', self.change_to_viagra, 'ЛСД')
        btn_save = ButtonObject(game, 600, 350, 125, 50, 'black', self.save_map, 'Сохранить')
        btn_clear = ButtonObject(game, 600, 400, 125, 50, 'black', self.clear_map, 'Очистить')
        btn_back = ButtonObject(game, 600, 525, 125, 50, 'black', self.back, '< Назад')
        # TODO: Загрузка уже существующих файлов, переход на окно игры

        self.objects.extend([self.board, name,
                             btn_empty,
                             btn_wall,
                             btn_mayo,
                             btn_viagra,
                             btn_save, btn_clear, btn_back])

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
