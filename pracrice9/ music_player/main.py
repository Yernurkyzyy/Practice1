import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

music_dir = "music_player/music/"
songs = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
current_song = 0

def play_song():
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song]))
    pygame.mixer.music.play()

if songs: play_song()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: pygame.mixer.music.pause()
            if event.key == pygame.K_r: pygame.mixer.music.unpause() # Resume
            if event.key == pygame.K_s: pygame.mixer.music.stop()
            if event.key == pygame.K_n: # Next
                current_song = (current_song + 1) % len(songs)
                play_song()
            if event.key == pygame.K_b: # Back
                current_song = (current_song - 1) % len(songs)
                play_song()

    screen.fill((30, 30, 30))
    pygame.display.flip()
pygame.quit()