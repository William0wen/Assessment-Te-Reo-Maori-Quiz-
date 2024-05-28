"""Creating a new endless mode
Making nice final score screen for endless mode
William Owen 26/05/24"""

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

# print(pygame.font.get_fonts())
# Fonts
arial = pygame.font.SysFont("Arial", 50)
comic_sans = pygame.font.SysFont("comicsansms", 50)
hygraphicmedium = pygame.font.SysFont("hygraphicmedium", 40)
small_hygraphicmedium = pygame.font.SysFont("hygraphicmedium", 30)


question_randomizer = []
randomized_questions = []
incorrect = []

# Assigning the questions to variables which will be chosen randomly from a list
questions = []

clock = pygame.time.Clock()


class Question:
    def __init__(self, question, answer1, answer2, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.correct_answer = correct_answer
        questions.append(Question)

    def display_question(self, text_colour, current_round):
        correct_choice = ""

        correct_choice_rect = 0
        choice_1_rect = 0
        choice_2_rect = 0
        choice_3_rect = 0

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

            # Displaying the current round
            current_round_caption = hygraphicmedium.render(f"Round {current_round}", True, black)
            current_round_rect = current_round_caption.get_rect()
            current_round_rect.center = (850, 100)
            screen.blit(current_round_caption, current_round_rect)

            # Getting the question and answer captions prepared to display
            question_caption = comic_sans.render(self.question, True, black)
            question_rect = question_caption.get_rect()
            question_rect.center = (500, 200)

            # All this is to keep track of what the correct choice is
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
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if correct_choice == choice_1:
                        choice_1_caption = arial.render(choice_1, True, black, bright_green)
                        choice_1_rect = choice_1_caption.get_rect()
                        choice_1_rect.center = (250, 500)
                        screen.blit(choice_1_caption, choice_1_rect)
                    elif correct_choice == choice_2:
                        choice_2_caption = arial.render(choice_2, True, black, bright_green)
                        choice_2_rect = choice_2_caption.get_rect()
                        choice_2_rect.center = (500, 500)
                        screen.blit(choice_2_caption, choice_2_rect)
                    elif correct_choice == choice_3:
                        choice_3_caption = arial.render(choice_3, True, black, bright_green)
                        choice_3_rect = choice_3_caption.get_rect()
                        choice_3_rect.center = (750, 500)
                        screen.blit(choice_3_caption, choice_3_rect)

                    if correct_choice_rect.collidepoint(pos):
                        pygame.display.flip()
                        time.sleep(0.7)
                        return 1
                    else:
                        # Display incorrect on the screen
                        not_correct = arial.render("INCORRECT", True, bright_red)
                        not_correct_rect = not_correct.get_rect()
                        not_correct_rect.center = (500, 300)
                        screen.blit(not_correct, not_correct_rect)
                        pygame.display.flip()
                        time.sleep(0.7)
                        return 0

            pygame.display.flip()
        pygame.display.flip()


# Regular mode questions
question_1 = Question("What is 'Monday' in Māori? ", "Rāmere", "Rātapu", "Rāhina")
question_2 = Question("What is 'Tuesday' in Māori?", "Rāapa", "Rāhoroi", "Rātu")
question_3 = Question("What is 'Wednesday' in Māori?", "Rāpare", "Rāmere", "Rāapa")
question_4 = Question("What is 'Thursday' in Māori?", "Rāapa", "Rātu", "Rāpare")
question_5 = Question("What is 'Friday' in Māori?", "Rāapa", "Rāpare", "Rāmere")
question_6 = Question("What is 'Saturday' in Māori?", "Rāmere", "Rātapu", "Rāhoroi")
question_7 = Question("What is 'Sunday' in Māori?", "Rāhina", "Rāhoroi", "Rātapu")
question_8 = Question("What is 'one' in Māori?", "Whā", "Whitu", "Tahi")
question_9 = Question("What is 'two' in Māori?", "Rima", "Ono", "Rua")
question_10 = Question("What is 'three' in Māori?", "Whā", "Tahi", "Toru")
question_11 = Question("What is 'four' in Māori?", "Iwa", "Tekau", "Whā")
question_12 = Question("What is 'five' in Māori?", "Waru", "Ono", "Rima")
question_13 = Question("What is 'six' in Māori?", "Whā", "Rua", "Ono")
question_14 = Question("What is 'seven' in Māori?", "Waru", "Toru", "Whitu")
question_15 = Question("What is 'eight' in Māori?", "Whā", "Tahi", "Waru")
question_16 = Question("What is 'nine' in Māori?", "Takau", "Tahi", "Iwa")
question_17 = Question("What is 'ten' in Māori?", "Whā", "Whitu", "Tekau")
# Additional endless mode questions
question_18 = Question("What is 'white' in Māori?", "Whero", "Karaka", "Mā")
question_19 = Question("What is 'red' in Māori?", "Mā", "Kikorangi", "Whero")
question_20 = Question("What is 'orange' in Māori?", "Kākāriki", "Kikorangi", "Karaka")
question_21 = Question("What is 'yellow' in Māori?", "Whero", "Kākāriki", "Kōwhai")
question_22 = Question("What is 'green' in Māori?", "Kōwhai", "Mā", "Kākāriki")
question_23 = Question("What is 'blue' in Māori?", "Karaka", "Kōwhai", "Kikorangi")
question_24 = Question("What is 'work' in Māori?", "Hui", "Hīkoi", "Mahi")
question_25 = Question("What is 'sea' in Māori?", "Maunga", "Motu", "Moana")
question_26 = Question("What is 'mountain' in Māori?", "Motu", "Moana", "Maunga")
question_27 = Question("What is 'children' in Māori?", "Tapu", "Tamāhine", "Tamariki")
question_28 = Question("What is 'water' in Māori?", "Waiata", "Waka", "Wai")
question_29 = Question("What is 'homeland' in Māori?", "Waiata", "Whānau", "Whenua")
question_30 = Question("What is 'funeral' in Māori?", "Hangi", "Taonga", "Tangi")


# Function for the title page I can call whenever I want to start a new quiz
def title_page():

    instructions_caption = small_hygraphicmedium.render("Please click directly on your chosen answer", True, black)
    instructions_rect = instructions_caption.get_rect()
    instructions_rect.center = (500, 250)
    title_caption = comic_sans.render("Te Reo Māori Quiz", True, black)
    title_rect = title_caption.get_rect()
    title_rect.center = (500, 200)

    button = pygame.image.load("start_button.png").convert_alpha()
    endless_button = pygame.image.load("endless_mode_button.png").convert_alpha()

    # Main loop
    quit_test = False
    while not quit_test:
        screen.fill(white)
        screen.blit(title_caption, title_rect)
        screen.blit(instructions_caption, instructions_rect)
        start_button = screen.blit(button, (350, 400))
        endless_mode_button = screen.blit(endless_button, (397, 560))

        # Quit loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_test = True

            # Detecting mouse click on the start button
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                if start_button.collidepoint(pos):
                    new_quiz()

                elif endless_mode_button.collidepoint(pos):
                    endless_mode()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    quit()


def new_quiz():

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

    correct_questions = 0
    in_progress = True
    while in_progress:
        for current_round in range(1, 11):
            # Setting random bg colour
            random_colour = random.choice(colour_list)
            screen.fill(random_colour)

            # Getting random question
            current_question = random.choice(questions)
            # adding the return statement of the function5 onto total correct questions
            correct_questions += Question.display_question(current_question, random_colour, current_round)

            questions.remove(current_question)

        in_progress = False

    # Refreshing the question list
    for question in questions:
        questions.remove(question)

    scoring_page(correct_questions)


# Final scoring page for user to see their final score before continuing
def scoring_page(correct_questions):
    screen.fill(white)

    score_caption = comic_sans.render(f"Final score: {correct_questions}/10", True, black)
    score_rect = score_caption.get_rect()
    score_rect.center = (500, 200)
    screen.blit(score_caption, score_rect)

    button = pygame.image.load("start_button.png").convert_alpha()
    start_button = screen.blit(button, (130, 450))
    button = pygame.image.load("quit_button.png").convert_alpha()
    quit_button = screen.blit(button, (510, 450))

    pygame.display.flip()

    quit_test = False
    while not quit_test:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_test = True

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if start_button.collidepoint(pos):
                    title_page()

                elif quit_button.collidepoint(pos):
                    quit_test = True

        pygame.display.flip()

    pygame.quit()
    quit()


def endless_mode():

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
    questions.append(question_24)
    questions.append(question_25)
    questions.append(question_26)
    questions.append(question_27)
    questions.append(question_28)
    questions.append(question_29)
    questions.append(question_30)

    score = 0
    current_round = 1
    in_progress = True
    while in_progress:
        # Setting random bg colour
        screen.fill(bright_green)

        # Getting random question
        current_question = random.choice(questions)
        current_question_ = Question.display_question(current_question, bright_green, current_round)

        if current_question_ == 1:
            score += 1
            current_round += 1

        elif current_question_ == 0:
            in_progress = False

    # Refreshing the question list
    for question in questions:
        questions.remove(question)

    # Appending score to txt file
    txt_file = open("scores.txt", "a")
    txt_file.write(f"{score}\n")
    txt_file.close()

    # Sorting txt file
    f = open("scores.txt", "r")
    data = f.read()
    scores = data.split("\n")
    f.close()

    scores.sort()
    high_score = scores[-1]  # Finding highest score in txt file

    endless_mode_scoring_page(score, high_score)


def endless_mode_scoring_page(score, high_score):
    screen.fill(white)

    your_score_caption = comic_sans.render(f"Your score: {score}", True, black)
    your_score_rect = your_score_caption.get_rect()
    your_score_rect.center = (500, 200)
    screen.blit(your_score_caption, your_score_rect)

    high_score_caption = comic_sans.render(f"Highest recorded score: {high_score}", True, black)
    high_score_rect = high_score_caption.get_rect()
    high_score_rect.center = (500, 300)
    screen.blit(high_score_caption, high_score_rect)

    button = pygame.image.load("start_button.png").convert_alpha()
    start_button = screen.blit(button, (130, 450))
    button = pygame.image.load("quit_button.png").convert_alpha()
    quit_button = screen.blit(button, (510, 450))

    pygame.display.flip()

    quit_test = False
    while not quit_test:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_test = True

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if start_button.collidepoint(pos):
                    title_page()

                elif quit_button.collidepoint(pos):
                    quit_test = True

        pygame.display.flip()

    pygame.quit()
    quit()


# Main
title_page()

pygame.quit()
quit()
