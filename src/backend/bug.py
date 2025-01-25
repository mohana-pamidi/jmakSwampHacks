import pygame
from constants import *
import random

class Bug:
    def __init__(self, location): 
        self.location = location
        self.imagePath =  "C:/Users/SRIDH/Projects/jmakSwampHacks/src/images/buggie.png"
        self.bug_img = pygame.image.load(self.imagePath)
        self.bug_img = pygame.transform.scale(self.bug_img, (60, 60))
        self.word_duck_is_trying_to_guess = WORDS[self.get_random_word()]
        self.isCleared = True

    def get_random_word(self):
        #MUST ACCOUNT FOR DUPLICATE WORDS
        return random.randint(1, len(WORDS) - 1)



    def get_location(self):
        return self.location


