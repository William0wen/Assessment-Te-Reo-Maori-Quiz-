"""Creating the class in which I can store, randomize and display different questions for the quiz
Making the answers clickable, checking if clicked answer is true or not
William Owen 14/05/24"""

import pygame
import random
import time
pygame.init()

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Te Reo Maori Quiz")

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
blue = (169, 198, 245)
purple = (217, 164, 245)
green = (203, 237, 161)
red = (245, 162, 171)
tan = (252, 221, 172)
colour_list = [blue, purple, green, red, tan]


# Fonts
arial = pygame.font.SysFont("Arial", 50)
comic_sans = pygame.font.SysFont("comicsansms", 50)

question_list = []
question_randomizer = []
randomized_questions = []

clock = pygame.time.Clock()


class Question:
    def __init__(self, question, answer1, answer2, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.correct_answer = correct_answer
        question_list.append(self)

    def display_question(self, text_colour):
        correct_choice = ""

        question_randomizer.append(self.answer1)
        question_randomizer.append(self.answer2)
        question_randomizer.append(self.correct_answer)

        # Randomizing order of answers displayed
        choice_1 = random.choice(question_randomizer)
        if choice_1 == self.correct_answer:
            correct_choice = choice_1
        question_randomizer.remove(choice_1)
        choice_2 = random.choice(question_randomizer)
        if choice_2 == self.correct_answer:
            correct_choice = choice_2
        question_randomizer.remove(choice_2)
        choice_3 = random.choice(question_randomizer)
        if choice_3 == self.correct_answer:
            correct_choice = choice_3
        question_randomizer.remove(choice_3)

        randomized_questions.append(choice_1)
        randomized_questions.append(choice_2)
        randomized_questions.append(choice_3)

        clicked = False
        while not clicked:

            # Getting the question and answer captions prepared to display
            question_caption = comic_sans.render(self.question, True, black)
            question_rect = question_caption.get_rect()
            question_rect.center = (500, 200)

            choice_1_caption = arial.render(choice_1, True, black, text_colour)
            if correct_choice == choice_1:
                correct_choice_rect = choice_1_caption.get_rect()
                correct_choice_rect.center = (250, 500)
            else:
                choice_1_rect = choice_1_caption.get_rect()
                choice_1_rect.center = (250, 500)

            choice_2_caption = arial.render(choice_2, True, black, text_colour)
            if correct_choice == choice_2:
                correct_choice_rect = choice_2_caption.get_rect()
                correct_choice_rect.center = (500, 500)
            else:
                choice_2_rect = choice_2_caption.get_rect()
                choice_2_rect.center = (500, 500)

            choice_3_caption = arial.render(choice_3, True, black, text_colour)
            if correct_choice == choice_3:
                correct_choice_rect = choice_3_caption.get_rect()
                correct_choice_rect.center = (750, 500)
            else:
                choice_3_rect = choice_3_caption.get_rect()
                choice_3_rect.center = (750, 500)

            # Displaying the captions to the screen
            screen.blit(question_caption, question_rect)
            if correct_choice == choice_1:
                screen.blit(choice_1_caption, correct_choice_rect)
            else:
                screen.blit(choice_1_caption, choice_1_rect)

            if correct_choice == choice_2:
                screen.blit(choice_2_caption, correct_choice_rect)
            else:
                screen.blit(choice_2_caption, choice_2_rect)

            if correct_choice == choice_3:
                screen.blit(choice_3_caption, correct_choice_rect)
            else:
                screen.blit(choice_3_caption, choice_3_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Checking if the mouse position is over the answers
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if correct_choice_rect.collidepoint(pos):
                        print("correct option")
                    else:
                        print("Not correct")

            pygame.display.flip()
        pygame.display.flip()


question_1 = Question("1. What is my name?", "Wrong 1", "Wrong 2", "Correct")


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

        random_colour = random.choice(colour_list)

        # Quit loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_test = True

            # Detecting mouse click on the start button
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                # print(pos)
                if start_button.collidepoint(pos):
                    in_progress = True
                    while in_progress:
                        screen.fill(random_colour)
                        Question.display_question(question_1, random_colour)

        pygame.display.flip()

        clock.tick(60)


# Main
title_page()

pygame.quit()
quit()

