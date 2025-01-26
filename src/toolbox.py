
from window import *
from API import *
from bug import *
from duck import *
import numpy as np
import random
from constants import *


class Toolbox:
    def __init__(self):
        self.myDuck = Duck()
        self.myAPI = API()
        self.arrOfBugs = []
        self.keys = []
        self.input_active = False
        self.words_array = WORDS[:]
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("frontend/PressStart2P-Regular.ttf", 10)
        
    
    def randomizeInitBugs(self):
        random.seed()
        for i in range(NUM_OF_BUGS):
            # Get point
            pointX = random.uniform(BUG_RADIUS, SCREEN_WIDTH - BUG_RADIUS )
            pointY = random.uniform(BUG_RADIUS + 200, 600 - 50 - 60)
            # Create bug
            bug = Bug(((pointX, pointY)))
            bug.word_duck_is_trying_to_guess = bug.get_random_word(self.words_array)
            text_width = self.font.size("Your word is: " + bug.word_duck_is_trying_to_guess)[0]
            # Update location based on the length of the word
            bug.location = (max(0, pointX - text_width), pointY)

            # print(self.words_array)
            # print(bug.word_duck_is_trying_to_guess)
            self.arrOfBugs.append(bug)
            


            



    
  

