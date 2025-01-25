import pygame, sys
from toolbox import *
from window import *

if __name__ == "__main__":
    myToolBox = Toolbox()
    theWindow = Window(myToolBox)
    theWindow.on_execute()


    
