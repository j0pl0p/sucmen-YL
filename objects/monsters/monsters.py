from objects.monsters.base import Monster


class Larry(Monster):
    """ Скари Лари = Блинки (красный призрак) из оригинальной игры """
    filename = 'data/images/mutants/larry/up.png'
    IMAGES = {Monster.LEFT: 'data/images/mutants/larry/left.png',
              Monster.UP: 'data/images/mutants/larry/up.png',
              Monster.DOWN: 'data/images/mutants/larry/down.png',
              Monster.RIGHT: 'data/images/mutants/larry/right.png'}
    cruise_elroy_is_active = False

    def __init__(self, game, field, x=10 + 18 * 14, y=10 + 18 * 11):
        super().__init__(self.filename, game, field, x, y)
        self.x, self.y = x, y
        self.aim_default_x, self.aim_default_y = 10 + 18 * 50, 10 - 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 13, 10 + 18 * 11

    def reset(self):
        super().__init__(self.filename, self.game, self.field, self.x, self.y)
        self.aim_default_x, self.aim_default_y = 10 + 18 * 50, 10 - 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 13, 10 + 18 * 11

    # подробнее на habr.com
    def check_cruise_elroy(self):
        seed_count = self.field.get_seed_count()
        if seed_count / self.initial_seed_count <= 0.25:
            self.cruise_elroy_is_active = True

    def change_state(self):
        if self.state == self.STAY_IN:
            self.state = self.BEGIN
            self.direction = self.UP
        else:
            super().change_state()

    # позиция берётся из класса амняма хабиба и тд
    def choose_aim_position(self):
        if not self.cruise_elroy_is_active:
            self.check_cruise_elroy()

        if self.state == self.WANDER:
            if self.cruise_elroy_is_active:
                player = self.game.windows[self.game.current_window_index].player
                self.aim_x, self.aim_y = player.rect.x, player.rect.y
            else:
                self.aim_x, self.aim_y = self.aim_default_x, self.aim_default_y
        elif self.state == self.HUNT:
            player = self.game.windows[self.game.current_window_index].player
            self.aim_x, self.aim_y = player.rect.x, player.rect.y
        else:
            super().choose_aim_position()

    def process_draw(self):
        super().process_draw((227, 0, 27))


class Kissy(Monster):
    """ Киси Миси = Пинки (розовый призрак) из оригинальной игры """
    filename = 'data/images/mutants/kissy/up.png'
    IMAGES = {Monster.LEFT: 'data/images/mutants/kissy/left.png',
              Monster.UP: 'data/images/mutants/kissy/up.png',
              Monster.DOWN: 'data/images/mutants/kissy/down.png',
              Monster.RIGHT: 'data/images/mutants/kissy/right.png'}

    def __init__(self, game, field, x=10 + 18 * 14, y=10 + 18 * 14):
        super().__init__(self.filename, game, field, x, y)
        self.x, self.y = x, y
        self.aim_default_x, self.aim_default_y = 10 - 18 * 50, 10 - 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 13, 10 + 18 * 11

    def reset(self):
        super().__init__(self.filename, self.game, self.field, self.x, self.y)
        self.aim_default_x, self.aim_default_y = 10 - 18 * 50, 10 - 18 * 50
        self.aim_begin_x, self.aim_begin_y = 10 + 18 * 13, 10 + 18 * 11

    def change_state(self):
        if self.state == self.STAY_IN:
            self.state = self.BEGIN
            self.direction = self.UP
        else:
            super().change_state()

    # позиция берётся из класса амняма хабиба и тд
    def choose_aim_position(self):
        if self.state == self.HUNT:
            player = self.game.windows[self.game.current_window_index].player
            pacman_directions = {player.LEFT: [-4, 0], player.RIGHT: [4, 0], player.UP: [-4, -4], player.DOWN: [0, 4]}
            self.aim_x, self.aim_y = player.rect.x + 18 * pacman_directions[player.direction][0], \
                                     player.rect.y + 18 * pacman_directions[player.direction][1]
        else:
            super().choose_aim_position()

    def process_draw(self):
        super().process_draw((255, 99, 178))
