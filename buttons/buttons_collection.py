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

        arrows = new_button(width / 2 + 40 * scale, 75, 'data/images/morgen/ice_p.png',
                            'data/images/morgen/ice.png', scale, self.function_arrows)
        wasd = new_button(width / 2 - 250 * scale / 2 - 100, 75, 'data/images/morgen/cadillac_p.png',
                          'data/images/morgen/cadillac.png', scale / 2, self.function_wasd)
        arrows.connect(wasd)

        mus_button = new_checkmark(30, height * 0.7, 'data/images/system/ok.png',
                                   scale, 'музыка вкл/выкл', self.function_checkmark_music)
        sound_button = new_checkmark(30, height * 0.8, 'data/images/system/ok.png',
                                     scale, 'звуки вкл/выкл', self.function_checkmark_sound)

        back_button = BackButton(5, 20, self.game, self.function_back, text='Принять')
        back_button.padding = 150
        buttons = [wasd, arrows, mus_button, sound_button, back_button]
        return buttons

    def function_back(self):
        self.game.set_window(self.game.WINDOW_MENU)
        self.game.settings.write_to_file()

    def function_wasd(self):
        pass

    def function_arrows(self):
        pass

    def function_checkmark_music(self):
        self.game.settings.music_change()

    def function_checkmark_sound(self):
        self.game.settings.sound_change()

    def prev_settings(self):
        pass


def new_button(x, y, image_path, pressed_image_path, scale, function):
    img = pg.image.load(image_path).convert_alpha()
    img_pressed = pg.image.load(pressed_image_path).convert_alpha()

    butt = SwitchButton(x, y, img, img_pressed, 0.3 * scale, function)
    return butt


def new_checkmark(x, y, img_path, scale, text, function):
    img = pg.image.load(img_path).convert_alpha()
    checkmark = CheckButton(x, y, 30, 30, img, int(scale), text, function)
    return checkmark


