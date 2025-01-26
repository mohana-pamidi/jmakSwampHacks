import pygame
from constants import *
import random

class Bug:
    def __init__(self, location):
        self.location = location
        self.imagePath =  "images/buggie.png"
        self.bug_img = pygame.image.load(self.imagePath)
        self.bug_img = pygame.transform.scale(self.bug_img, (60, 60))
        self.word_duck_is_trying_to_guess = WORDS[self.get_random_word()]
        self.font = pygame.font.SysFont(None, 25)
        self.isCleared = True

    def returnText(self):

        text = self.font.render(("Your word is: " + self.word_duck_is_trying_to_guess), True, (0, 0, 0))

        return text


    def get_random_word(self):
        #MUST ACCOUNT FOR DUPLICATE WORDS
        return random.randint(1, len(WORDS) - 1)



    def get_location(self):
        return self.location


