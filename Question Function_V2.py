"""Creating the class in which I can store and randomize different questions for the quiz
Converting plain print statements onto the pygame interface
William Owen 13/05/24"""

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
        
        # Randomizing order of answers displayed
        choice_1 = random.choice(question_randomizer)
        question_randomizer.remove(choice_1)
        choice_2 = random.choice(question_randomizer)
        question_randomizer.remove(choice_2)
        choice_3 = random.choice(question_randomizer)
        question_randomizer.remove(choice_3)
        print(choice_1, "", choice_2, "", choice_3)


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
                # print(pos)
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

