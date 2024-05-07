"""Maori Quiz Setup with pygame - Setting colour/font variables and initial gameloop
William Owen 7/05/24"""

import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Te Reo Maori Quiz")

black = (0, 0, 0)
white = (255, 255, 255)
blue = (50, 85, 168)
purple = (160, 105, 201)
green = (139, 166, 81)
red = (186, 91, 105)
colour_list = [black, white, blue, purple, green, red]


arial = pygame.font.SysFont("Arial", 20)
comic_sans = pygame.font.SysFont("comicsansms", 20)


clock = pygame.time.Clock()


# Main

quit_test = False
while not quit_test:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_test = True

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
quit()

