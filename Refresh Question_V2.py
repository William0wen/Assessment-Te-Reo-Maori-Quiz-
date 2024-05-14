"""Refreshing the pygame display after one of the answers has been clicked,
Adds graphic afterwards so the user knows the correct question
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
bright_green = (85, 255, 66)
bright_red = (247, 47, 74)
colour_list = [blue, purple, green, red, tan]


# Fonts
arial = pygame.font.SysFont("Arial", 50)
comic_sans = pygame.font.SysFont("comicsansms", 50)

question_list = []
question_randomizer = []
randomized_questions = []
incorrect = []

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
        else:
            incorrect.append(choice_1)
        question_randomizer.remove(choice_1)
        choice_2 = random.choice(question_randomizer)
        if choice_2 == self.correct_answer:
            correct_choice = choice_2
        else:
            incorrect.append(choice_2)
        question_randomizer.remove(choice_2)
        choice_3 = random.choice(question_randomizer)
        if choice_3 == self.correct_answer:
            correct_choice = choice_3
        else:
            incorrect.append(choice_3)
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
                    if correct_choice == choice_1:
                        choice_1_caption = arial.render(choice_1, True, black, bright_green)
                        choice_1_rect = choice_1_caption.get_rect()
                        choice_1_rect.center = (250, 500)
                        screen.blit(choice_1_caption, choice_1_rect)

                        pygame.display.flip()
                    elif correct_choice == choice_2:
                        choice_2_caption = arial.render(choice_2, True, black, bright_green)
                        choice_2_rect = choice_2_caption.get_rect()
                        choice_2_rect.center = (500, 500)
                        screen.blit(choice_2_caption, choice_2_rect)
                        pygame.display.flip()
                    elif correct_choice == choice_3:
                        choice_3_caption = arial.render(choice_3, True, black, bright_green)
                        choice_3_rect = choice_3_caption.get_rect()
                        choice_3_rect.center = (750, 500)
                        screen.blit(choice_3_caption, choice_3_rect)

                    if correct_choice_rect.collidepoint(pos):
                        print("correct option")
                        pygame.display.flip()
                        time.sleep(0.7)
                        return True
                    else:
                        print("Not correct")
                        not_correct = arial.render("INCORRECT", True, bright_red)
                        not_correct_rect = not_correct.get_rect()
                        not_correct_rect.center = (500, 300)
                        screen.blit(not_correct, not_correct_rect)
                        pygame.display.flip()
                        time.sleep(0.7)
                        return False

            pygame.display.flip()
        pygame.display.flip()


# Assigning the questions to variables which will be chosen randomly from a list
questions = []
question_1 = Question("What is 'Monday' in Māori?", "Rāmere", "Rātapu", "Rāhina")
question_2 = Question("What is 'Tuesday' in Māori?", "Rāapa", "Rāhoroi", "Rātu")
question_3 = Question("What is 'Wednesday' in Māori?", "Rāpare", "Rāmere", "Rāapa")
question_4 = Question("What is 'Thursday' in Māori?", "Rāapa", "Rātu", "Rāpare")
question_5 = Question("What is 'Friday' in Māori?", "Rāapa", "Rāpare", "Rāmere")
question_6 = Question("What is 'Saturday' in Māori?", "Rāmere", "Rātapu", "Rāhoroi")
question_7 = Question("What is 'Sunday' in Māori?", "Rāhina", "Rāhoroi", "Rātapu")
question_8 = Question("What is one in Māori?", "Whā", "Whitu", "Tahi")
question_9 = Question("What is two in Māori?", "Rima", "Ono", "Rua")
question_10 = Question("What is three in Māori?", "Whā", "Tahi", "Toru")
question_11 = Question("What is four in Māori?", "Iwa", "Tekau", "Whā")
question_12 = Question("What is five in Māori?", "Waru", "Ono", "Rima")
question_13 = Question("What is six in Māori?", "Whā", "Rua", "Ono")
question_14 = Question("What is seven in Māori?", "Waru", "Toru", "Whitu")
question_15 = Question("What is eight in Māori?", "Whā", "Tahi", "Waru")
question_16 = Question("What is nine in Māori?", "Takau", "Tahi", "Iwa")
question_17 = Question("What is ten in Māori?", "Whā", "Whitu", "Tekau")
question_18 = Question("What is white in Māori?", "Whero", "Karaka", "Mā")
question_19 = Question("What is red in Māori?", "Mā", "Kikorangi", "Whero")
question_20 = Question("What is orange in Māori?", "Kākāriki", "Kikorangi", "Karaka")
question_21 = Question("What is yellow in Māori?", "Whero", "Kākāriki", "Kōwhai")
question_22 = Question("What is green in Māori?", "Kōwhai", "Mā", "Kākāriki")
question_23 = Question("What is blue in Māori?", "Karaka", "Kōwhai", "Kikorangi")


# Function for the title page I can call whenever I want to start a new quiz
def title_page():
    title_caption = comic_sans.render("Te Reo Māori Quiz", True, black)
    title_rect = title_caption.get_rect()
    title_rect.center = (500, 200)

    button = pygame.image.load("start_button.png").convert_alpha()

    # Main loop
    quit_test = False
    while not quit_test:
        screen.fill(white)
        screen.blit(title_caption, title_rect)
        start_button = screen.blit(button, (350, 400))

        # Quit loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_test = True

            # Detecting mouse click on the start button
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                # print(pos)
                if start_button.collidepoint(pos):
                    new_question()
        pygame.display.flip()

        clock.tick(60)


def new_question():
    # Append questions to question list
    questions.append(question_1)
    questions.append(question_2)
    questions.append(question_3)
    questions.append(question_4)
    questions.append(question_5)
    questions.append(question_6)
    questions.append(question_7)
    questions.append(question_8)
    questions.append(question_9)
    questions.append(question_10)
    questions.append(question_11)
    questions.append(question_12)
    questions.append(question_13)
    questions.append(question_14)
    questions.append(question_15)
    questions.append(question_16)
    questions.append(question_17)
    questions.append(question_18)
    questions.append(question_19)
    questions.append(question_20)
    questions.append(question_21)
    questions.append(question_22)
    questions.append(question_23)
    in_progress = True
    while in_progress:
        for number in range(1, 11):
            # Setting random bg colour
            print(f"Round {number}")
            random_colour = random.choice(colour_list)
            screen.fill(random_colour)

            # Getting random question
            current_question = random.choice(questions)
            Question.display_question(current_question, random_colour)
            questions.remove(current_question)

        title_page()


def scoring_page():
    pass


# Main
title_page()

pygame.quit()
quit()

