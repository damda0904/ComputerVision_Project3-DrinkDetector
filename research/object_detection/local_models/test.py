import pygame

music_file = "coke.mp3"

pygame.mixer.init()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    clock.tick(30)
pygame.mixer.quit()