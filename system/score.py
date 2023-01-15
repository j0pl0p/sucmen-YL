import pygame
import os.path

from system.settings import SAVE_PATH


class Score:
    """ Счёт """
    def __init__(self, points=0):
        self.points = points

    def reset(self):
        self.points = 0

    def increase_on(self, points):
        self.points += points

    def current_points(self):
        return self.points


class HighScore:
    """ Рекорд """
    SAVE_FILE = SAVE_PATH
    HIGHSCORE_COUNT = 10

    def __init__(self):
        self.highscores = []
        if not os.path.exists(self.SAVE_FILE):
            with open(self.SAVE_FILE, 'w') as save_file:
                save_file.write('0\n')
        self.load_from_file()

    def load_from_file(self):
        """ Загрузка из файла """
        with open(self.SAVE_FILE, 'r') as save_file:
            self.highscores = []
            count = int(save_file.readline())
            for i in range(count):
                result = save_file.readline().split()
                self.highscores.append([result[0], int(result[1])])

    def save_to_file(self):
        """ Сохранение в файл """
        with open(self.SAVE_FILE, 'w') as save_file:
            save_file.write(f'{len(self.highscores)}\n')
            for i in range(len(self.highscores)):
                save_file.write(f'{self.highscores[i][0]} {self.highscores[i][1]}\n')

    def clean_all_results(self):
        """ Сброс результатов """
        with open(self.SAVE_FILE, 'w') as save_file:
            save_file.write('0\n')
            self.highscores = []

    def add_new_result(self, name, new_result):
        """ Добавление рекорда """
        insert_position = self.is_highscore(new_result)
        self.highscores = self.highscores[:insert_position] + [[name, new_result]] + self.highscores[insert_position:]
        if len(self.highscores) > self.HIGHSCORE_COUNT:
            self.highscores = self.highscores[:self.HIGHSCORE_COUNT]

    def is_highscore(self, new_result):
        """ оаоммм """
        insert_position = 0
        while insert_position < len(self.highscores) and self.highscores[insert_position][1] > new_result:
            insert_position += 1
        return insert_position
