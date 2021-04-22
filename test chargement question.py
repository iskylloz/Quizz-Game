import os
import random
import pygame

pygame.init()

# Ecran
white = (255, 255, 255)
x = 1000
y = 600
screen = pygame.display.set_mode((x, y))
screen.fill(white)
pygame.display.flip()
# Ce bout de code n'est pas de moi je l'ai trouvé sur un forum
# -------------------------------------------------------------------------------------------------
# Chargement des images du dossier questions vertes
dossier_image = 'question/blue/'
images_path = os.listdir(dossier_image)
images = []
for path in images_path:
    images.append(pygame.transform.scale(pygame.image.load(dossier_image + path), (x, y)))
# -------------------------------------------------------------------------------------------------
nbr_image = len(images)
curr_draw = random.randint(0, nbr_image-1)
if curr_draw % 2 == 1:
    current_iq = curr_draw
    current_ia = current_iq - 1
    # Random choice parmis les images du dossier
    current_q = images[current_iq]
    current_a = images[current_ia]
else:
    curr_draw = random.randint(0, nbr_image-1)

# Key state
question_key = False
answer_key = False
next_key = False
info_key = False


# Game state
running = True
q_state = 'Q'

# Boucle de jeu

while running:
    screen.fill(white)

    if q_state == 'Q':
        screen.blit(current_q, (0, 0))
    if q_state == 'R':
        screen.blit(current_a, (0, 0))

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

    # Check inputs
    if next_key:
        # Action de la touche
        curr_draw = random.randint(0, nbr_image-1)
        if curr_draw % 2 == 1:
            current_iq = curr_draw
            current_ia = current_iq - 1
            current_q = images[current_iq]
            current_a = images[current_ia]
        else:
            curr_draw = random.randint(0, nbr_image-1)
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
        print('nbr images =', nbr_image)
        print('current iq', current_iq)
        print('current draw =', curr_draw)
        print(images)
        info_key = False

    pygame.display.update()
