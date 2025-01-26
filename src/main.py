
import pygame, sys
from toolbox import *
from window import *
from gameState import *
import pygame

if __name__ == "__main__":
    pygame.init()
    myToolBox = Toolbox()
    myGameState = GameState(myToolBox)
    pygame.mixer.music.load("game_music.wav")
    pygame.mixer.music.play(-1)
    theWindow = Window(myToolBox, myGameState)
    theWindow.on_execute()
    


    
