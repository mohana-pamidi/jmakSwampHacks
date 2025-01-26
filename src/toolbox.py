
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
        
    
    def randomizeInitBugs(self):
        for i in range(NUM_OF_BUGS):
            pointX = random.uniform(BUG_RADIUS, SCREEN_WIDTH - BUG_RADIUS)
            pointY = random.uniform(BUG_RADIUS, SCREEN_HEIGHT - BUG_RADIUS)
            bug = Bug(((pointX, pointY)))
            bug.word_duck_is_trying_to_guess = bug.get_random_word(self.words_array)
            # print(self.words_array)
            # print(bug.word_duck_is_trying_to_guess)
            self.arrOfBugs.append(bug)
            


            



    
  

