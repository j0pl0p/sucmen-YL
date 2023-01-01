import json
import os.path
import pygame


pygame.font.init()
FONT = 'system/bank_ghothic_medium.ttf'

SETTINGS_PATH = 'settings.json'
SAVE_PATH = 'data.txt'


class Settings:
    ice = 1
    cadillac = 0
    save_file = SETTINGS_PATH
    DEFAULT_SETTINGS = {
        'song': 0,
        'music': True,
        'sound': True,
    }

    def __init__(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as fp:
                self.storage = json.load(fp)
        else:
            self.storage = Settings.DEFAULT_SETTINGS

    def __del__(self):
        self.write_to_file()

    @property
    def song(self):
        return self.storage['song']

    @property
    def music(self):
        return self.storage['music']

    @property
    def sound(self):
        return self.storage['sound']

    def write_to_file(self):
        with open(self.save_file, 'w') as fp:
            json.dump(self.storage, fp, indent=4)

    def music_change(self):
        self.storage['music'] = not self.music

    def sound_change(self):
        self.storage['sound'] = not self.sound

    def song_change(self, song):
        self.storage['song'] = song

