import pygame, sys
from pygame.locals import *
#import duck




class Window:
    def __init__(self):
        self._running = True
        self.start_screen= True
        self._display_surf =None
        self.game_running=False
        self.size = self.width, self.height = 900, 700
        self.info_on_screen=False
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_caption("DuckieAIventure")
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 275 <= x <= 600 and 425 <= y <= 625 and self.start_screen:
                self.start_screen = False
                self.game_running = True
            if 750<=x<=850 and 0<=y<=100 and self.game_running:
                if self.info_on_screen==False:
                    self.info_on_screen=True
                elif self.info_on_screen:
                    self.info_on_screen=False




    def on_loop(self):
        #duck.main()
        if self.start_screen:
            self.on_render()
        if self.game_running:
            game_screen_image = pygame.image.load("../images/game_background.png")
            self._display_surf.blit(game_screen_image, game_screen_image.get_rect(topleft=(0, 0)))
            info_button=pygame.image.load("../images/info_button.png")
            self._display_surf.blit(info_button, info_button.get_rect(topright=(850,0)))
            if self.info_on_screen:
                info_tab = pygame.image.load("../images/info_tab.png")
                self._display_surf.blit(info_tab, info_tab.get_rect(topright=(750, 100)))
            pygame.display.flip()

    def on_render(self):
        start_screen_image = pygame.image.load("../images/Start screen.png")
        self._display_surf.blit(start_screen_image, start_screen_image.get_rect(topleft=(0, 0)))
        start_button = pygame.image.load("../images/Start.png")
        self._display_surf.blit(start_button, start_button.get_rect(center=(450, 525)))
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
            self.on_loop()

        self.on_cleanup()
