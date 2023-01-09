import pygame

from objects.image import ImageObject
from objects.wall import Wall, TeleportWall, Empty
from objects.mayonnaise import Mayo, Viagra


class Player(ImageObject):
    filename = 'data/images/player/right/1.png'
    image = pygame.image.load(filename)
    RIGHT, LEFT, UP, DOWN = 1, 2, 3, 4
    DEFAULT_DIRECTIONS = {RIGHT: [1, 0],
                          LEFT: [-1, 0],
                          UP: [0, -1],
                          DOWN: [0, 1]}
    BUTTONS = {'button_right': pygame.K_RIGHT,
               'button_up': pygame.K_UP,
               'button_left': pygame.K_LEFT,
               'button_down': pygame.K_DOWN}

    def __init__(self, game, field, x=0, y=0, direction=RIGHT):
        super().__init__(game)
        self.field = field
        self.rect.center = (x, y)
        self.direction = direction
        self.can_move = True
        self.next_direction = direction
        self.current_cell = [0, 0]
        self.future_cell = [0, 0]

    def step(self, back=False):
        if not back:
            directions = Player.DEFAULT_DIRECTIONS
            if not self.can_move:
                return
        else:
            # шаг назад (от стены)
            directions = {
                self.RIGHT: [-1, 0],
                self.LEFT: [1, 0],
                self.UP: [0, 1],
                self.DOWN: [0, -1],
            }
        self.move_center(
            self.rect.centerx + directions[self.direction][0],
            self.rect.centery + directions[self.direction][1]
        )

    def reset_position(self, x = 18 * 15, y = 18 * 24, direction = RIGHT):
        self.rect.centerx = x
        self.rect.centery = y
        self.direction = direction
        self.next_direction = direction

    def check_borders(self):
        if self.rect.left < 0 or self.rect.right > self.game.size[0] or self.rect.top < 0 or self.rect.bottom > self.game.size[1]:
            self.reset_position()

    def collide(self):
        near_positions = [
            [self.current_cell[0]-1, self.current_cell[1]],
            [self.current_cell[0]+1, self.current_cell[1]],
            [self.current_cell[0], self.current_cell[1]-1],
            [self.current_cell[0], self.current_cell[1]+1],
        ]
        for i in range(len(self.field.field)):
            for j in range(len(self.field.field[i])):
                obj = self.field.field[i][j]
                if type(obj) == Wall:
                    if self.rect.colliderect(obj.rect):
                        self.step(back=True)
                        self.can_move = False
                if type(obj) == Mayo or type(obj) == Viagra:
                    if self.rect.collidepoint(obj.rect.center):
                        self.field.update(i, j, Empty)
                        if type(obj) == Mayo:
                            self.game.score.increase_on(Mayo.POINTS)
                            self.field.seeds_count -= 1
                        else:
                            self.image = pygame.image.load('data/images/player/rage.png')
                            for m in self.game.windows[self.game.current_window_index].monsters:
                                if m.state != m.STAY_IN:
                                    m.frightened_is_active = True

                if type(obj) == TeleportWall:
                    if self.rect.colliderect(obj.rect):
                        if self.direction == self.RIGHT:
                            self.reset_position(18 * 2, 18 * 15, self.RIGHT)
                        else:
                            self.reset_position(18 * 27, 18 * 15, self.LEFT)

    def change_direction(self):
        dir = {
            self.RIGHT: pygame.Rect(self.rect.x + 5, self.rect.y, self.rect.w, self.rect.h),
            self.LEFT: pygame.Rect(self.rect.x - 5, self.rect.y, self.rect.w, self.rect.h),
            self.UP: pygame.Rect(self.rect.x, self.rect.y - 5, self.rect.w, self.rect.h),
            self.DOWN: pygame.Rect(self.rect.x, self.rect.y + 5, self.rect.w, self.rect.h)
        }
        for row in self.field.field:
            for item in row:
                if type(item) == Wall:
                    if dir[self.next_direction].colliderect(item.rect):
                        return
        self.direction = self.next_direction

    def process_logic(self):
        self.change_direction()
        self.collide()
        self.step()
        self.check_borders()
        self.get_current_cell()

    def process_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key == pygame.K_RIGHT:
            self.next_direction = self.RIGHT
        elif event.key == pygame.K_LEFT:
            self.next_direction = self.LEFT
        elif event.key == pygame.K_UP:
            self.next_direction = self.UP
        elif event.key == pygame.K_DOWN:
            self.next_direction = self.DOWN
        self.can_move = True

    def process_draw(self):
        super(Player, self).process_draw()

        # if self.field:
        #     pygame.draw.rect(self.game.screen, 'red', [self.current_cell[0] * self.field.CELL_WIDTH + self.field.rect.x,
        #                                                self.current_cell[1] * self.field.CELL_WIDTH + self.field.rect.y,
        #                                                self.field.CELL_WIDTH,
        #                                                self.field.CELL_WIDTH], 2)
        #     pygame.draw.rect(self.game.screen, 'yellow', [self.future_cell[0] * self.field.CELL_WIDTH + self.field.rect.x,
        #                                                   self.future_cell[1] * self.field.CELL_WIDTH + self.field.rect.y,
        #                                                   self.field.CELL_WIDTH,
        #                                                   self.field.CELL_WIDTH], 2)

    def get_current_cell(self):
        cell_column = (self.rect.centerx - self.field.rect.x) // self.field.CELL_WIDTH
        cell_row = (self.rect.centery - self.field.rect.y) // self.field.CELL_WIDTH
        self.current_cell = [cell_column, cell_row]
        cell_column += self.DEFAULT_DIRECTIONS[self.direction][0]*4
        cell_row += self.DEFAULT_DIRECTIONS[self.direction][1]*4
        self.future_cell = [cell_column, cell_row]
