import sys
from objects.base import DrawableObject
from objects.wall import Wall, Empty, TeleportWall
from objects.mayonnaise import Mayo, Viagra


class Field(DrawableObject):
    """ Класс карты В ИГРЕ """
    CELL_WIDTH = 18
    FIELD_CELLS = {'0': Empty,
                   '1': Wall,
                   '2': Mayo,
                   '3': Viagra,
                   '4': TeleportWall}

    def __init__(self, game, x, y, map_filename):
        super().__init__(game)
        self.map_filename = map_filename
        self.field = []
        self.move(x, y)
        self.seeds_count = 0
        self.load_map()
        self.rect.width = len(self.field[0]) * self.CELL_WIDTH
        self.rect.height = len(self.field) * self.CELL_WIDTH

    def load_map(self):
        """ Загрузка карты из файла """
        with open(self.map_filename, 'r') as f:
            row_index = 0
            for line in f:
                row, col_index = [], 0
                for symbol in line:
                    if symbol in self.FIELD_CELLS.keys():
                        cell_classname = self.FIELD_CELLS[symbol]
                        if cell_classname == Mayo:
                            self.seeds_count += 1
                        row.append(cell_classname(game=self.game,
                                                  x=self.rect.x + self.CELL_WIDTH * col_index,
                                                  y=self.rect.y + self.CELL_WIDTH * row_index))
                    col_index += 1
                row_index += 1
                self.field.append(row)

    def update(self, row_index, column_index, new_type):
        self.field[row_index][column_index] = new_type(game=self.game,
                                                       x=self.rect.x + self.CELL_WIDTH * column_index,
                                                       y=self.rect.y + self.CELL_WIDTH * row_index)

    def get_seed_count(self):
        """ Подсчёт оставшегося майонеза на карте """
        count = 0
        for row in self.field:
            for obj in row:
                if type(obj) == Mayo or type(obj) == Viagra:
                    count += 1
        return count

    def process_draw(self):
        """ Отрисовка каждого объекта на карте """
        for row in self.field:
            for item in row:
                if item:
                    item.process_draw()
