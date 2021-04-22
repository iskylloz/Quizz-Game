import pygame
import math


class Bleu:
    def __init__(self):
        self.window_info = pygame.display.Info()
        self.x, self.y = self.window_info.current_w, self.window_info.current_h

        self.question_bleu = []

        self.barack_obama = (pygame.image.load('question/blue/barack obama.jpeg').convert_alpha(),
                             pygame.transform.scale(
                                 pygame.image.load('question/blue/barack obama r.png').convert_alpha(),
                                 (math.ceil(self.x * 0.9), math.ceil(self.y * 0.9))))
        self.question_bleu.append(self.barack_obama)

        self.bernard_hinault = (pygame.image.load('question/blue/bernard hinault.jpg').convert_alpha(),
                                pygame.transform.scale(
                                    pygame.image.load('question/blue/bernard hinault r.png').convert_alpha(),
                                    (math.ceil(self.x * 0.9), math.ceil(self.y * 0.9))))
        self.question_bleu.append(self.bernard_hinault)

        self.mary_pierce = (pygame.image.load('question/blue/mary pierce.jpg').convert_alpha(),
                            pygame.transform.scale(pygame.image.load('question/blue/mary pierce r.png').convert_alpha(),
                                                   (math.ceil(self.x * 0.9), math.ceil(self.y * 0.9))))
        self.question_bleu.append(self.mary_pierce)
