from buttons.switch_button import SwitchButton
from buttons.check_button import CheckButton
from buttons.back_button import BackButton
import pygame as pg


class ButtonsCollection:
    def __init__(self, game):
        self.game = game
        self.buttons = self.create_buttons()
        self.prev_settings()

    def create_buttons(self):
        width, height = self.game.width, self.game.height
        scale = width / 800 * 1.5

        morgen = new_button(width / 2 + 40 * scale, 75, 'data/images/morgen/ice_p.png',
                            'data/images/morgen/ice.png', scale, self.function_ice)
        cadillac = new_button(width / 2 - 250 * scale / 2 - 100, 75, 'data/images/morgen/cadillac_p.png',
                              'data/images/morgen/cadillac.png', scale / 2, self.function_cadillac)
        morgen.connect(cadillac)

        mus_button = new_checkmark(30, height * 0.7, 'data/images/system/ok.png',
                                   scale, 'музыка вкл/выкл', self.function_checkmark_music)
        sound_button = new_checkmark(30, height * 0.8, 'data/images/system/ok.png',
                                     scale, 'звуки вкл/выкл', self.function_checkmark_sound)

        back_button = BackButton(5, 20, self.game, self.function_back, text='Принять')
        back_button.padding = 150
        buttons = [cadillac, morgen, mus_button, sound_button, back_button]
        return buttons

    def function_back(self):
        self.game.set_window(self.game.WINDOW_MENU)
        self.game.settings.write_to_file()

    def function_cadillac(self):
        self.game.settings.song_change(self.game.settings.cadillac)

    def function_ice(self):
        self.game.settings.song_change(self.game.settings.ice)

    def function_checkmark_music(self):
        self.game.settings.music_change()

    def function_checkmark_sound(self):
        self.game.settings.sound_change()

    def prev_settings(self):
        self.buttons[0].switch = not self.game.settings.song
        self.buttons[1].switch = self.game.settings.song
        self.buttons[2].switch = self.game.settings.music
        self.buttons[3].switch = self.game.settings.sound


def new_button(x, y, image_path, pressed_image_path, scale, function):
    img = pg.image.load(image_path).convert_alpha()
    img_pressed = pg.image.load(pressed_image_path).convert_alpha()

    butt = SwitchButton(x, y, img, img_pressed, 0.3 * scale, function)
    return butt


def new_checkmark(x, y, img_path, scale, text, function):
    img = pg.image.load(img_path).convert_alpha()
    checkmark = CheckButton(x, y, 30, 30, img, int(scale), text, function)
    return checkmark
