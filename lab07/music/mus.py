import pygame
import os

pygame.init()
screen = pygame.display.set_mode((300, 100))
music_dir = os.getcwd()
music_files = os.listdir(music_dir)
current_track = 0

pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    pygame.mixer.music.play()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_track]))
    pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_music()
            elif event.key == pygame.K_x:
                stop_music()
            elif event.key == pygame.K_z:
                next_track()
            elif event.key == pygame.K_c:
                previous_track()
    screen.fill((255, 255, 255))
    pygame.display.flip()
#previous track - c, next track - z, stop music - x, play music - space
pygame.quit()
