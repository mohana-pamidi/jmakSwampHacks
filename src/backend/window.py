import pygame, sys
from pygame.locals import *
import duck

from src.backend.duck import screen


class Window:
    def __init__(self):
        self._running = True
        self.start_screen= True
        self._display_surf = None
        self.size = self.width, self.height = 900, 700
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_caption("DuckieAIventure")
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        duck.main()
    
    def on_render(self):

        self._display_surf.fill((125, 199, 242))  # Background color
        header_image = pygame.Surface((200, 200))  # Create a dummy surface
        header_image.fill((255, 0, 0))  # Fill it with red
        header_rect = header_image.get_rect(center=(self.width / 2, self.height / 3))
        self._display_surf.blit(header_image, header_rect)
        pygame.display.flip()

        '''
        self._display_surf.fill((125, 199, 242))
        header_image=pygame.image.load("../images/Duckies_Ai_Adventure.png")
        self._display_surf.blit(header_image,header_image.get_rect(center=(self.width/2,self.height/3)))
        pygame.display.flip()
        '''
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
                if self.start_screen():
                    self.on_render()
                if not self.start_screen:
                    self.on_loop()

        self.on_cleanup()
