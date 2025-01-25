from window import *
from API import *
from bug import *
import numpy as np
import random
from constants import *


class Toolbox:
    def __init__(self): 
        self.theWindow = Window()
        self.myAPI = API()
        self.arrOfBugs = []
        self.randomizeInitBugs()
        
    
    def randomizeInitBugs(self):
        for i in range(10):
            pointX = random.uniform(0, SCREEN_WIDTH)
            pointY = random.uniform(0, SCREEN_HEIGHT)
            bug = Bug(((pointX, pointY)))
            self.arrOfBugs.append(bug)


            



    
  

