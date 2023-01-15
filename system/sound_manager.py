import pygame.mixer as mixer
import os


class Sounds:
    """ Звуки """
    songs = {
        'cadillac': mixer.Sound('data/sounds/cadillac.mp3'),
        'ice': mixer.Sound('data/sounds/ice.mp3'),
        'mainmenu': mixer.Sound('data/sounds/mainmenu.mp3'),
        'death': mixer.Sound('data/sounds/death.mp3')
    }
    sounds = {
        'eating': mixer.Sound('data/sounds/eating.mp3'),
        'spears': mixer.Sound('data/sounds/spears.mp3')
    }
    rage = {
        'rage': mixer.Sound('data/sounds/rage.mp3')
    }
    channel_song = 0
    channel_sound = 1
    channel_rage = 2
    __cur_song = ''
    __prev_song = ''

    @staticmethod
    def current_song():
        """ Получение музыки, которая играет в данный момент """
        return Sounds.__cur_song

    @staticmethod
    def play_song(filename, loops=-1):
        """ Включение музыки """
        mixer.Channel(Sounds.channel_song).play(Sounds.songs[filename], loops=loops)
        Sounds.__prev_song = Sounds.__cur_song
        Sounds.__cur_song = filename

    @staticmethod
    def play_sound(filename):
        """ Включение звука """
        mixer.Channel(Sounds.channel_sound).play(Sounds.sounds[filename])

    @staticmethod
    def play_rage():
        """ Включение музыки под крокодилом """
        mixer.Channel(Sounds.channel_rage).play(Sounds.rage['rage'])
        Sounds.__prev_song = Sounds.__cur_song
        Sounds.__cur_song = 'rage'

    @staticmethod
    def stop_rage():
        """ Остановка музыки под крокодилом """
        mixer.Channel(Sounds.channel_rage).pause()
        Sounds.__cur_song = Sounds.__prev_song
        Sounds.__prev_song = 'rage'

    @staticmethod
    def is_playing():
        """ Проверка на игру"""
        return mixer.music.get_busy()

    @staticmethod
    def change_volume(volume=0.025, channel=channel_song):
        """ Изменение громкости """
        mixer.Channel(channel).set_volume(volume)

    @staticmethod
    def pause(channel=channel_song):
        """ Пауза """
        mixer.Channel(channel).pause()
        Sounds.__prev_song = Sounds.__cur_song
        Sounds.__cur_song = ''

    @staticmethod
    def unpause(channel=channel_song):
        """ Возобновление музыки """
        mixer.Channel(channel).unpause()
        Sounds.__cur_song = Sounds.__prev_song
        Sounds.__prev_song = ''