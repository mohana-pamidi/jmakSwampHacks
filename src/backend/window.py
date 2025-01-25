import pygame, sys
from pygame.locals import *
from toolbox import *


class Window:
    def __init__(self, toolbox):
        pygame.init()
        self._running = True
        self.start_screen= True
        self._display_surf = None
        self.size = self.width, self.height = 900, 700
        self.toolbox = toolbox
        self.font = pygame.font.Font(None, 36)
        self.keys = []
        self.user_text = ""
 
    def on_init(self):
        self._display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_caption("DuckieAIventure")
        self._running = True
 
    def on_event(self, event):

        if event.type == pygame.QUIT:
            self._running = False

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
        self.toolbox.keys = pygame.key.get_pressed()

        if not self.toolbox.input_active:
            self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y = self.toolbox.myDuck.move_duck(self.toolbox.keys, self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y)

        # Check to see if duck is near bug
        if self.toolbox.myDuck.is_near_bug(self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y):
            print("reset")
            self.toolbox.input_active = True

        self._display_surf.blit(self.toolbox.myDuck.duck_img, (self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y))

        self.toolbox.clock.tick(60)




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
                if self.start_screen:
                    self.on_render()
                if not self.start_screen:
                    self.on_loop()

        self.on_cleanup()
