import pygame
import os

class MusicPlayer:
    def __init__(self, music_dir):
        self.music_dir = music_dir
        self.songs = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
        self.current_idx = 0

    def play(self):
        if self.songs:
            pygame.mixer.music.load(os.path.join(self.music_dir, self.songs[self.current_idx]))
            pygame.mixer.music.play()

    def next_track(self):
        self.current_idx = (self.current_idx + 1) % len(self.songs)
        self.play()

    def prev_track(self):
        self.current_idx = (self.current_idx - 1) % len(self.songs)
        self.play()

    def stop(self):
        pygame.mixer.music.stop()