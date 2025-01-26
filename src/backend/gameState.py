# This is the gameState class
# File Name: gameState.py
from enum import Enum
import toolbox
from constants import *

# This enum is to help track what state the player is in while playing
class State(Enum):
    WELCOME = 1
    PROMPTING = 2
    PLAYING = 3
    WIN = 4

class GameState:
    # Constructor
    def __init__(self, toolbox):
        # Attributes
        self.toolbox = toolbox
        self.num_bugs_left = NUM_OF_BUGS       # the score of the game
        self.curr_bug_duck_on = self.toolbox.arrOfBugs[0]
        self.welcome_frame = ""
        self.state = State.WELCOME

    ''' FUNCTIONS '''
    # getstate returns the current state of the game
    def __get_state__(self):
        return self.state

    # setstate sets the state of the game based on the param. passed in
    def __set_state__(self, state):
        self.state = state

    # get_num_bugs returns the number bugs the user has collected
    def get_num_bugs(self):
        return self.num_bugs_left

    # set_num_bugs updates the current number of bugs
    def set_num_bugs(self, num_bugs):
        self.num_bugs_left = num_bugs
    
    def get_curr_bug_duck_on(self):
        return self.curr_bug_duck_on
    
    def set_curr_bug_duck_on(self, bug):
        self.curr_bug_duck_on = bug


