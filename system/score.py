import pygame


class Score:
    def __init__(self, points=0):
        self.points = points

    def reset(self):
        self.points = 0

    def increase_on(self, points):
        self.points += points

    def current_points(self):
        return self.points


class HighScore:
    pass

