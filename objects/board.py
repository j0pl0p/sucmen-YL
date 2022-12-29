import pygame
from objects.base import DrawableObject
from objects.wall import Wall, Empty, TeleportWall
from objects.mayonnaise import Mayo, Viagra
import copy


class Board(DrawableObject):
    """ Класс новой карты """
    WIDTH = 28
    HEIGHT = 31
    CELL_SIZE = 18
    FIELD_CELLS = {'0': Empty,
                   '1': Wall,
                   '2': Mayo,
                   '3': Viagra,
                   '4': TeleportWall}
    MODE = 'empty'
    DEFAULT_MAP = [list('1111111111111111111111111111'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000111001110000000001'),
                   list('1000000000100000010000000001'),
                   list('1000000000100000010000000001'),
                   list('1000000000100000010000000001'),
                   list('1000000000111111110000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1000000000000000000000000001'),
                   list('1111111111111111111111111111')]

    def __init__(self, game, x, y):
        super().__init__(game)
        self.boardfile = copy.deepcopy(self.DEFAULT_MAP)
        self.game = game
        self.move(x, y)
        self.left, self.top = x, y
        self.load_map()
        self.rect.width = len(self.boardfile[0]) * self.CELL_SIZE
        self.rect.height = len(self.boardfile) * self.CELL_SIZE

    def process_draw(self):
        self.load_map()
        pygame.draw.rect(self.game.screen, '#363636', (self.left-1, self.top-1,
                                                    self.CELL_SIZE*self.WIDTH+2,
                                                    self.CELL_SIZE*self.HEIGHT+2), 1)
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                pygame.draw.rect(self.game.screen, '#454545', (self.left + x * self.CELL_SIZE,
                                                             self.top + y * self.CELL_SIZE,
                                                             self.CELL_SIZE,
                                                             self.CELL_SIZE), 1)


    def process_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                cell = self.get_cell(event.pos)
                self.on_click(cell)
            elif event.button == 2:
                cell = self.get_cell(event.pos)
                self.on_click(cell, mode=2)

    def get_cell(self, pos):
        if self.rect.collidepoint(pos):
            return ((pos[0] - self.left) // self.CELL_SIZE,
                    (pos[1] - self.top) // self.CELL_SIZE)
        else:
            return None

    def on_click(self, cell, mode=1):
        if cell is not None:
            cx, cy = cell
            if not self.is_editable(cx, cy):
                return
            if mode == 2 or self.MODE == 'empty':
                self.boardfile[cy][cx] = '0'
            elif self.MODE == 'wall':
                self.boardfile[cy][cx] = '1'
            elif self.MODE == 'mayo':
                self.boardfile[cy][cx] = '2'
            elif self.MODE == 'viagra':
                self.boardfile[cy][cx] = '3'

    def is_editable(self, x, y):
        if x not in [self.WIDTH-1, 0] and y not in [self.HEIGHT-1, 0]:
            if x not in range(10, 18) or y not in range(12, 17):
                return True
        return False

    def load_map(self):
        viagra = pygame.image.load('data/images/drug.png')
        row = -1
        for line in self.boardfile:
            col = -1
            row += 1
            for symbol in line:
                col += 1
                if symbol == '1':
                    pygame.draw.rect(self.game.screen, '#780000', (self.left + self.CELL_SIZE * col,
                                                                   self.top + self.CELL_SIZE * row,
                                                                   self.CELL_SIZE, self.CELL_SIZE))
                elif symbol == '2':
                    pygame.draw.circle(self.game.screen, '#f5f5dc', (self.left + self.CELL_SIZE * (col+0.5),
                                                                     self.top + self.CELL_SIZE * (row+0.5)), 3)
                elif symbol == '3':
                    self.game.screen.blit(viagra, (self.left + self.CELL_SIZE * col+1,
                                                   self.top + self.CELL_SIZE * row+1))

    def save_map(self, file):
        for r in self.boardfile:
            file.write(''.join(r)+'\n')
        file.close()
        return True

    def clear_map(self):
        self.boardfile = copy.deepcopy(self.DEFAULT_MAP)