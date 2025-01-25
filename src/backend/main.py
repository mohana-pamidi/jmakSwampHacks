
import pygame, sys
from toolbox import *
from window import *
from gameState import *

if __name__ == "__main__":
    myToolBox = Toolbox()
    myGameState = GameState(myToolBox)
    theWindow = Window(myToolBox, myGameState)
    theWindow.on_execute()


    
