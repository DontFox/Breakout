import pygame
import sys

pygame.init()

window_width = 800
window_height = 600

main_window = pygame.display.set_mode((window_width,window_height))


run = True
while run:
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            run = False
