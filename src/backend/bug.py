import pygame

class Bug:
    def __init__(self, location): 
        self.location = location
        self.imagePath = "../images/buggie.png"
        self.bug_img = pygame.image.load("../images/buggie.png")
        self.bug_img = pygame.transform.scale(self.bug_img, (60, 60))
        self.isHidden = True

    def get_location(self):
        return self.location


