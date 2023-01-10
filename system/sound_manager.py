import pygame.mixer as mixer
import os


class Sounds:
    songs = {
        'rage': mixer.Sound('data/sounds/rage.wav')
    }
    sounds = {

    }
    channel_song = 0
    channel_sound = 1

    @staticmethod
    def play_song(filename):
        mixer.Channel(Sounds.channel_song).play(Sounds.songs[filename], loops=-1)

    @staticmethod
    def play_sound(filename):
        mixer.Channel(Sounds.channel_sound).play(Sounds.sounds[filename])

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
