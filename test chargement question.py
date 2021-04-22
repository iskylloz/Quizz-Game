import os
import random
import pygame
import math

pygame.init()

# Ecran
win_info = pygame.display.Info()
white = (75, 255, 0)
x = win_info.current_w
y = win_info.current_h
screen = pygame.display.set_mode((x, y), pygame.FULLSCREEN)
screen.fill(white)
pygame.display.flip()
# Bout de code venant de : https://openclassrooms.com/forum/sujet/affichage-dimage-aleatoires-python-pygame
# ------------------------------------------------------------------
# Chargement des green_pic du dossier questions vertes
green_file = 'question/green/'
green_path = os.listdir(green_file)
green_pic = []
green_question = []
green_answer = []
for path in green_path:
    green_pic.append(pygame.image.load(green_file + path))
# ------------------------------------------------------------------
for idc_green, elt_green in enumerate(green_pic):
    if idc_green % 2 != 0:
        green_question.append(elt_green)
    else:
        green_answer.append(elt_green)

nbr_green = len(green_question)
green_draw = random.randint(0, nbr_green-1)
curr_q_green = green_question[green_draw]
curr_a_green = green_answer[green_draw]

# Key state
question_key = False
answer_key = False
next_key = False
info_key = False
escape_key = False

# Game state
running = True
q_state = 'Q'

# Boucle de jeu

while running:

    screen.fill(white)

    if q_state == 'Q':
        screen.blit(curr_q_green, (math.ceil(x*0.1), 0))
    if q_state == 'R':
        screen.blit(pygame.transform.scale(curr_a_green, (x, y)), (0, 0))

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                next_key = True
            if event.key == pygame.K_q:
                question_key = True
            if event.key == pygame.K_a:
                answer_key = True
            if event.key == pygame.K_TAB:
                info_key = True
            if event.key == pygame.K_ESCAPE:
                escape_key = True

    # Check inputs
    if next_key:
        # Action de la touche
        green_question.remove(curr_q_green)
        green_answer.remove(curr_a_green)
        nbr_green = len(green_question)
        green_draw = random.randint(0, nbr_green-1)
        curr_q_green = green_question[green_draw]
        curr_a_green = green_answer[green_draw]
        q_state = 'Q'
        next_key = False
    if question_key:
        # Action de la touche
        q_state = 'Q'
        question_key = False
    if answer_key:
        # Action de la touche
        q_state = 'R'
        answer_key = False
    if info_key:
        print('List img =', green_pic)
        print('List Q =', green_question)
        print('List A =', green_answer)
        info_key = False
    if escape_key:
        running = False
        escape_key = False

    pygame.display.update()
