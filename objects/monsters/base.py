from datetime import datetime
from random import randint
import pygame.transform
from objects.wall import Wall, TeleportWall
from objects.image import ImageObject
from system.sound_manager import Sounds

pygame.init()


class Monster(ImageObject):
    """Базовый класс хагиваги"""
    # состояния
    HUNT, WANDER, FRIGHTENED, BEGIN, STAY_IN = 0, 1, 2, -1, -2
    # направления
    LEFT, UP, DOWN, RIGHT = 0, 1, 2, 3
    # иконки
    filename = 'data/images/mutants/huggy/huggy.png'
    filename_frightened = 'data/images/mutants/scared.png'
    IMAGES = {LEFT: pygame.image.load(filename),
              UP: pygame.image.load(filename),
              DOWN: pygame.image.load(filename),
              RIGHT: pygame.image.load(filename)}
    CHANGE_STATE_DELTA = {STAY_IN: -1, BEGIN: -1, HUNT: 8500, WANDER: 4500, FRIGHTENED: 6000}
    DEFAULT_DIRECTIONS = {RIGHT: [1, 0],
                          LEFT: [-1, 0],
                          UP: [0, -1],
                          DOWN: [0, 1]}

    def __init__(self, filename, game, field, x, y):
        super().__init__(game, filename, x, y)
        self.image = pygame.transform.scale(self.image, (18, 18))
        self.field = field
        self.rect = self.image.get_rect(x=x, y=y)
        self.frightened_remain = -1  # секунды до конца страха
        self.direction = None
        self.state = self.STAY_IN
        self.frightened_is_active = False
        self.is_state_changed = False
        self.state_change_time = datetime.now()
        self.aim_x, self.aim_y = 0, 0
        self.aim_default_x, self.aim_default_y = 0, 0
        self.aim_begin_x, self.aim_begin_y = 0, 0
        self.initial_seed_count = self.field.get_seed_count()

    def process_move(self, coefficient=1):
        if self.direction is None:
            return

        directions = self.DEFAULT_DIRECTIONS
        self.move_center(
            self.rect.centerx + directions[self.direction][0] * coefficient,
            self.rect.centery + directions[self.direction][1] * coefficient
        )

    def get_possible_directions(self, is_state_changed=False):
        if self.direction is None:
            return []

        directions = [self.LEFT, self.UP, self.RIGHT, self.DOWN]
        special_positions = [[12, 11], [13, 11], [14, 11], [15, 11], [12, 23], [15, 23]]
        if [self.rect.x, self.rect.y] in [[10 + c[0] * 18, 10 + c[1] * 18] for c in special_positions]:
            if [self.rect.x, self.rect.y] in [[10 + c[0] * 18, 10 + c[1] * 18] for c in [[13, 11], [14, 11]]]:
                directions = [self.LEFT, self.UP, self.RIGHT]
            else:
                directions = [self.LEFT, self.RIGHT, self.DOWN]

        save_direction = self.direction
        possible_directions = []

        for i in range(len(directions)):
            test_direction = directions[i]
            if is_state_changed and test_direction == save_direction or \
                    not is_state_changed and save_direction + test_direction == 3:
                continue

            self.direction = test_direction
            self.process_move(18)

            if self.check_collisions() == 0:
                possible_directions.append(test_direction)
            elif self.check_collisions() == 2:
                if self.direction == self.RIGHT:
                    self.rect.x = 18 * 2 - 10
                    self.rect.y = (18 * 15) - 8
                    possible_directions.append(3)
                    return possible_directions
                else:
                    self.rect.x = 18 * 26 + 10
                    self.rect.y = (18 * 15) - 8
                    possible_directions.append(0)
                    return possible_directions

            self.direction = 3 - test_direction
            self.process_move(18)

        self.direction = save_direction

        if not possible_directions:
            return [3 - save_direction]
        return possible_directions

    def check_is_in_cell(self):
        return not ((self.rect.x - 10) % 18 or (self.rect.y - 10) % 18)

    def check_collisions(self):
        for i in range(len(self.field.field)):
            for j in range(len(self.field.field[i])):
                if type(self.field.field[i][j]) == Wall and self.rect.colliderect(self.field.field[i][j].rect):
                    return 1
                elif type(self.field.field[i][j]) == TeleportWall and self.rect.colliderect(self.field.field[i][j].rect):
                    return 2
        return 0

    def collide_with(self, other):
        return self.rect.colliderect(other.rect)

    def get_next_direction(self):
        possible_directions = self.get_possible_directions()
        if not possible_directions:
            self.direction = None
            return

        min_distance = 10000000
        best_direction = 0
        for i in range(len(possible_directions)):
            test_direction = possible_directions[i]

            self.direction = test_direction
            self.process_move(18)

            test_distance = ((self.aim_x - self.rect.x) ** 2 + (self.aim_y - self.rect.y) ** 2) ** 0.5
            if test_distance < min_distance:
                min_distance = test_distance
                best_direction = test_direction

            self.direction = 3 - test_direction
            self.process_move(18)

        self.direction = best_direction

    def new_state(self, new_state):
        self.state_change_time = datetime.now()
        self.state = new_state

    def change_state(self):
        if self.state == self.BEGIN:
            if self.rect.x == self.aim_x and self.rect.y == self.aim_y:
                self.new_state(self.WANDER)
        elif self.frightened_is_active:
            if self.state != self.FRIGHTENED:
                self.new_state(self.FRIGHTENED)
                self.game.windows[self.game.current_window_index].player.bad_trip_active = True # applying rage.png to player
                self.image = pygame.image.load(self.filename_frightened)
                self.image = pygame.transform.scale(self.image, (18, 18))
                self.frightened_remain = self.CHANGE_STATE_DELTA[self.FRIGHTENED] // 1000 - 1
            elif (datetime.now() - self.state_change_time).seconds * 1000 >= self.CHANGE_STATE_DELTA[self.state]:
                self.new_state(self.WANDER)
                Sounds.stop_rage()
                Sounds.unpause(Sounds.channel_song)
                self.game.windows[self.game.current_window_index].player.bad_trip_active = False # removing rage.png from player
                self.frightened_remain = -1
                self.image = pygame.image.load(self.filename)
                self.image = pygame.transform.scale(self.image, (18, 18))
                self.frightened_is_active = False
                self.game.windows[self.game.WINDOW_GAME].ghost_bounty = 200
            else:
                self.frightened_remain = int((datetime.now() - self.state_change_time).seconds) + \
                                         self.CHANGE_STATE_DELTA[self.FRIGHTENED] // 1000 - 1
        elif (datetime.now() - self.state_change_time).seconds * 1000 >= self.CHANGE_STATE_DELTA[self.state]:
            if self.state == self.WANDER:
                self.new_state(self.HUNT)
            elif self.state == self.HUNT:
                self.new_state(self.WANDER)

    def choose_aim_position(self):
        if self.state == self.STAY_IN:
            self.aim_x, self.aim_y = self.rect.x, self.rect.y
        elif self.state == self.BEGIN:
            self.aim_x, self.aim_y = self.aim_begin_x, self.aim_begin_y
        elif self.state == self.WANDER:
            self.aim_x, self.aim_y = self.aim_default_x, self.aim_default_y
        elif self.state == self.HUNT:
            pacman = self.game.scenes[self.game.current_scene_index].pacman
            self.aim_x, self.aim_y = pacman.rect.x, pacman.rect.y
        elif self.state == self.FRIGHTENED:
            self.aim_x, self.aim_y = 10 + 18 * randint(-100, 200), 10 + 18 * randint(-100, 200)

    def process_logic(self):
        if self.check_is_in_cell():
            self.change_state()
            self.choose_aim_position()
            self.get_next_direction()
        self.process_move()

    def process_draw(self, color=(255, 255, 255)):
        if self.direction and self.state != self.FRIGHTENED:
            self.image = pygame.image.load(self.IMAGES[self.direction])
            self.image = pygame.transform.scale(self.image, (18, 18))
        super(Monster, self).process_draw()