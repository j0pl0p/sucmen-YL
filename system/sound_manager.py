import pygame.mixer as mixer
import os


class Sounds:
    songs = {
        'cadillac': mixer.Sound('data/sounds/cadillac.mp3'),
        'ice': mixer.Sound('data/sounds/ice.mp3'),
        'mainmenu': mixer.Sound('data/sounds/mainmenu.mp3')
    }
    sounds = {
        'eating': mixer.Sound('data/sounds/eating.mp3')
    }
    rage = {
        'rage': mixer.Sound('data/sounds/rage.mp3')
    }
    channel_song = 0
    channel_sound = 1
    channel_rage = 2

    @staticmethod
    def play_song(filename, loops=-1):
        mixer.Channel(Sounds.channel_song).play(Sounds.songs[filename], loops=loops)

    @staticmethod
    def play_sound(filename):
        mixer.Channel(Sounds.channel_sound).play(Sounds.sounds[filename])

    @staticmethod
    def play_rage():
        mixer.Channel(Sounds.channel_rage).play(Sounds.rage['rage'])

    @staticmethod
    def stop_rage():
        mixer.Channel(Sounds.channel_rage).pause()

    @staticmethod
    def is_playing():
        return mixer.music.get_busy()

    @staticmethod
    def change_volume(volume=0.025, channel=channel_song):
        mixer.Channel(channel).set_volume(volume)

    @staticmethod
    def pause(channel=channel_song):
        mixer.Channel(channel).pause()

    @staticmethod
    def unpause(channel=channel_song):
        mixer.Channel(channel).unpause()
