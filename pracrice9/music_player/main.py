import pygame
import os

pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

# Set the correct music directory
music_dir = "music/"

# Load song list
try:
    songs = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
except FileNotFoundError:
    print(f"Error: Directory '{music_dir}' not found!")
    songs = []

current_song = 0

def play_song():
    if songs:
        pygame.mixer.music.load(os.path.join(music_dir, songs[current_song]))
        pygame.mixer.music.play()
        print(f"Now playing: {songs[current_song]}")

if songs: 
    play_song()
else:
    print("No MP3 files found in the music folder.")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: # Play/Pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Music Paused")
                else:
                    pygame.mixer.music.unpause()
                    print("Music Resumed")

            elif event.key == pygame.K_s: # Stop
                pygame.mixer.music.stop()
                print("Music Stopped")

            elif event.key == pygame.K_n: # Next track
                if songs:
                    current_song = (current_song + 1) % len(songs)
                    play_song()

            elif event.key == pygame.K_b: # Previous (Back)
                if songs:
                    current_song = (current_song - 1) % len(songs)
                    play_song()

            elif event.key == pygame.K_q: # Quit
                print("Quitting Player...")
                running = False

    # Visual updates
    screen.fill((30, 30, 30))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()