import pygame
import sys
import os

pygame.init()

FPS = 60
SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('SUC-MEN')
clock = pygame.time.Clock()


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


class ImageSprite(pygame.sprite.Sprite):
    """ Спрайт-картинка. Сама по себе является пустышкой """
    def __init__(self, sprite_group, image='images/default.png', x=0, y=0, cut_bg=0):  # группа спрайтов, путь к картинке, x, y, вырезать фон
        super().__init__(sprite_group)
        self.x, self.y = x, y
        self.image = load_image(image, cut_bg)  # вырезание фона цвета пикселя (0, 0) если cut_bg = -1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        screen.blit(self.image, (self.x, self.y))

    def process_event(self):
        pass


class ButtonSprite(pygame.sprite.Sprite):
    """ Класс кнопки """
    def __init__(self, sprite_group, func, x=0, y=0, width=100, height=25, text='Кнопка', font_name='Comic Sans MS', font_size=20):  # группа спрайтов, x, y, ширина, высота, текст, шрифт (системный), кегль
        super().__init__(sprite_group)
        self.rect = pygame.Rect((x, y, width, height))
        self.x, self.y, self.width, self.height = x, y, width, height
        self.func = func
        self.text, self.font_name, self.font_size = text, font_name, font_size

        font = pygame.font.SysFont(self.font_name, self.font_size)
        self.image = font.render(self.text, True, (255, 255, 255))
        screen.blit(self.image, (self.x + 10, self.y + 10))
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height), 10)

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.func()

    def process_event(self, event):
        self.check_event(event)

    def update(self):
        pass


class BaseWindow:
    """ Базовый класс окна """
    def __init__(self, game):
        self.game = game
        self.objects_group = pygame.sprite.Group()
        self.screen = game.screen
        self.screen.set_alpha(0)
        self.screen.fill('black')

    def process_draw(self):
        self.objects_group.draw(self.screen)
        self.objects_group.update()

    def process_event(self, event):
        for object in self.objects_group:
            object.process_event(event)


class MenuWindow(BaseWindow):
    """ Главное меню """
    def __init__(self, game):
        super().__init__(game)
        background = pygame.transform.scale(load_image('images\mm_background.png'), (WIDTH, HEIGHT))
        logo = ImageSprite(self.objects_group, 'images\logo.png', 200, 10)
        btn_newgame = ButtonSprite(self.objects_group, self.new_game, 300, 250, text='Новая игра', font_size=40)
        btn_settings = ButtonSprite(self.objects_group, self.new_game, 300, 350, text='Настройки', font_size=40)
        screen.blit(background, (0, 0))

    def new_game(self):
        print('я кнопка')


class Game:
    """ Игра """
    SCENE_MENU = 0

    def __init__(self):
        self.screen = screen
        self.game_over = False
        self.scenes = [MenuWindow(self)]
        self.current_scene_index = 0

    def all_draw(self):
        self.scenes[self.current_scene_index].process_draw()
        pygame.display.flip()

    def frame(self):
        while not self.game_over:
            self.all_draw()
            clock.tick(FPS)

    def exit_game(self):
        self.game_over = True


# Пока что ненужная функция, но на всякий пожарный оставим
def main_menu():
    font1 = pygame.font.SysFont('Comic Sans MS', 75)
    font2 = pygame.font.SysFont('Arial', 50)
    font3 = pygame.font.SysFont('Times New Roman', 50)
    intro_text = [("SUC-MEN", font1, 225),  # Текст, шрифт и координата по оси х
                  ("", font1, 0),
                  ("Новая игра", font2, 280),
                  ("Настройки", font3, 275)]

    fon = pygame.transform.scale(load_image('mm_background.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    text_coord = 20
    for line, font, x in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = x
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


# Сама игра
# main_menu()
game = Game()
game.frame()
