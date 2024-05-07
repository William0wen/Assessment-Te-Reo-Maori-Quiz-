"""Maori Quiz test starting page with text displaying name of quiz
William Owen 7/05/24"""

import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Te Reo Maori Quiz")

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
blue = (50, 85, 168)
purple = (160, 105, 201)
green = (139, 166, 81)
red = (186, 91, 105)
colour_list = [black, white, blue, purple, green, red]


# Fonts
arial = pygame.font.SysFont("Arial", 20)
comic_sans = pygame.font.SysFont("comicsansms", 50)

# Setting up captions to display later
title_caption = comic_sans.render("Te Reo Maori Quiz", True, black)
title_rect = title_caption.get_rect()
title_rect.center = (500, 200)


clock = pygame.time.Clock()


# Main

quit_test = False
while not quit_test:
    screen.fill(white)
    screen.blit(title_caption, title_rect)
    # Quit loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_test = True

    pygame.display.flip()

    # Framerate set
    clock.tick(30)

pygame.quit()
quit()

