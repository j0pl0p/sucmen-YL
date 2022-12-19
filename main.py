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
main_menu()
