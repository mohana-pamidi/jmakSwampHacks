
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
        self.clock = pygame.time.Clock()
        self.randomizeInitBugs()
        
    
    def randomizeInitBugs(self):
        for i in range(10):
            pointX = random.uniform(0, SCREEN_WIDTH)
            pointY = random.uniform(0, SCREEN_HEIGHT)
            bug = Bug(((pointX, pointY)))
            print(bug.word_duck_is_trying_to_guess)
            self.arrOfBugs.append(bug)
            


            



    
  

