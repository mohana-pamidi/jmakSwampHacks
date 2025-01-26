import pygame, sys
from pygame.locals import *
from toolbox import *
from gameState import *



class Window:
    def __init__(self, toolbox, gameState):
        pygame.init()
        self._running = True
        self.start_screen = True
        self._display_surf = None
        self.game_running = False
        self.gameState = gameState
        self.size = self.width, self.height = 900, 700
        self.toolbox = toolbox
        self.font = pygame.font.Font(None, 36)
        self.keys = []
        self.user_text = ""
        self.info_on_screen=False
 
    def on_init(self):
        self._display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_caption("DuckieAIventure")
        self._running = True
 
    def on_event(self, event):

        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 275 <= x <= 600 and 350 <= y <= 449 and self.start_screen:
                self.start_screen = False
                self.game_running = True
            if 275<=x<=600 and 451<=y<= 550 and self.start_screen:
                self._running=False
            if 750<=x<=850 and 0<=y<=100 and self.game_running:
                if self.info_on_screen==False:
                    self.info_on_screen=True
                elif self.info_on_screen:
                    self.info_on_screen=False

        if event.type == pygame.KEYDOWN:
            
            if self.toolbox.input_active:

                print("can type input_active is not false")
                if event.key == pygame.K_RETURN:
                    # Send the prompt to Google Gemini/ make API call
                    response =  self.user_text

                    if response == "goodbye":
                        self.toolbox.input_active = False
                        # get rid of bug

                    self.user_text = ""  # Reset input


                elif event.key == pygame.K_BACKSPACE:
                    self.user_text =  self.user_text [:-1]  # Remove last character
                else:
                    self.user_text += event.unicode  # Add typed character


    def on_loop(self):

        state = self.gameState.__get_state__()

        if state == State.WELCOME and self.start_screen:
            self.on_render()
           # self.gameState. __set_state__(State.PLAYING)

        print("State: " , state)
        if state == State.PLAYING and self.game_running:
            # Welcome Screen Graphics
            game_screen_image = pygame.image.load("images/game_background.png")
            self._display_surf.blit(game_screen_image, game_screen_image.get_rect(topleft=(0, 0)))
            info_button=pygame.image.load("images/info_button.png")
            self._display_surf.blit(info_button, info_button.get_rect(topright=(850,0)))
            if self.info_on_screen:
                info_tab = pygame.image.load("images/info_tab.png")
                self._display_surf.blit(info_tab, info_tab.get_rect(topright=(750, 100)))

            # Duck Playing Graphics
            self.toolbox.keys = pygame.key.get_pressed()

            if not self.toolbox.input_active:
                self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y = self.toolbox.myDuck.move_duck(
                    self.toolbox.keys, self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y)

            # Check to see if duck is near bug
            if self.toolbox.myDuck.is_near_bug(self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y):

                self.gameState.__set_state__(State.PROMPTING)
                self.toolbox.input_active = True

            self._display_surf.blit(self.toolbox.myDuck.duck_img,
                                    (self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y))
            
            self._display_surf.blit(self.toolbox.arrOfBugs[0].bug_img,
                                    BUG_POSITION)
            
        if state == State.PROMPTING and self.game_running:
            self.draw_text_box()

        self.toolbox.clock.tick(60)

        pygame.display.flip()



    def on_render(self):
        start_screen_image = pygame.image.load("images/Start screen.png")
        self._display_surf.blit(start_screen_image, start_screen_image.get_rect(topleft=(0, 0)))
        start_button = pygame.image.load("images/Start.png")
        self._display_surf.blit(start_button, start_button.get_rect(center=(450, 400)))

        exit_button = pygame.image.load("images/exit.png")
        self._display_surf.blit(exit_button, exit_button.get_rect(center=(450,500)))
        pygame.display.flip()
        self.gameState. __set_state__(State.PLAYING)

        '''
        self._display_surf.fill((125, 199, 242))
        header_image=pygame.image.load("../images/Duckies_Ai_Adventure.png")
        self._display_surf.blit(header_image,header_image.get_rect(center=(self.width/2,self.height/3)))
        pygame.display.flip()
        '''
    def on_cleanup(self):
        pygame.quit()

    def draw_text_box(self):
        pygame.draw.rect(self._display_surf, (255, 255, 255), (200, 500, 500, 50))
        pygame.draw.rect(self._display_surf, (0, 0, 0), (200, 500, 500, 50), 2)
        text_surface = self.font.render( self.user_text, True, (0, 0, 0))
        self._display_surf.blit(text_surface, (210, 510))

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()

        self.on_cleanup()
