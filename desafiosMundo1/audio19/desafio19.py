import pygame
pygame.init() #iniciando o pygame
pygame.mixer.music.load('desafios/audio19/projetoMp3Python.mp3') #adicionando o audio
pygame.mixer.music.play() #tocando a musica

clock = pygame.time.Clock()

while pygame.mixer.music.get_busy():
    clock.tick(10)
