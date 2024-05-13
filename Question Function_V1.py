"""Creating the class in which I can store and randomize different questions for the quiz
William Owen 11/05/24"""

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
tan = (171, 162, 128)
colour_list = [black, white, blue, purple, green, red, tan]


# Fonts
arial = pygame.font.SysFont("Arial", 50)
comic_sans = pygame.font.SysFont("comicsansms", 50)

question_list = []
question_randomizer = []

clock = pygame.time.Clock()

class Question:
    def __init__(self, question, answer1, answer2, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.correct_answer = correct_answer
        question_list.append(self)

    def display_question(self):
        screen.fill(white)

        question_randomizer.append(self.answer1)
        question_randomizer.append(self.answer2)
        question_randomizer.append(self.correct_answer)
        print(self.question)
        chance = random.randint(1, 6)
        if chance == 1:
            print(self.answer1)
            print(self.answer2)
            print(self.correct_answer)
        elif chance == 2:
            print(self.answer2)
            print(self.answer1)
            print(self.correct_answer)
        elif chance == 3:
            print(self.correct_answer)
            print(self.answer1)
            print(self.answer2)
        elif chance == 4:
            print(self.answer1)
            print(self.correct_answer)
            print(self.answer2)
        elif chance == 5:
            print(self.answer2)
            print(self.correct_answer)
            print(self.answer1)
        elif chance == 6:
            print(self.correct_answer)
            print(self.answer2)
            print(self.answer1)


question_1 = Question("What is my name?", "William", "Jonty", "Thomas")


# Function for the title page I can call whenever I want to start a new quiz
def title_page():
    title_caption = comic_sans.render("Te Reo Maori Quiz", True, black)
    title_rect = title_caption.get_rect()
    title_rect.center = (500, 200)

    button = pygame.image.load("start_button.png").convert_alpha()

    # Main loop
    quit_test = False
    while not quit_test:
        screen.fill(white)
        screen.blit(title_caption, title_rect)
        start_button = screen.blit(button, (350, 400))

        pygame.display.flip()

        # Quit loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_test = True

            # Detecting mouse click on the start button
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                if start_button.collidepoint(pos):
                    Question.display_question(question_1)

        pygame.display.flip()

        clock.tick(60)


def start_quiz():
    print("Quiz Start")


# Main
title_page()

pygame.quit()
quit()

