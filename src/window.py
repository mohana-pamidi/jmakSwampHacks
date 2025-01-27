import pygame, sys
from pygame.locals import *
from toolbox import *
from gameState import *
import textwrap
import random


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
        self.font = pygame.font.Font("frontend/PressStart2P-Regular.ttf", 10)
        self.keys = []
        self.user_text = ""
        self.info_on_screen=True
        self.instruc_on_screen=True
        self.levelUp = False
        self.restrictedWord = False
 
    def on_init(self):
        self._display_surf = pygame.display.set_mode(self.size)
        pygame.display.set_caption("DuckieAIventure")
        self._running = True
 
    def on_event(self, event):
        # get current state
        state = self.gameState.__get_state__()

        # Event: user exits window
        if event.type == pygame.QUIT:
            self._running = False
        # Event: mouse is clicked
        # Currently checking: if info button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 275 <= x <= 600 and 350 <= y <= 449 and self.start_screen:
                self.start_screen = False
                self.game_running = True
                # render everything
            if 275<=x<=600 and 451<=y<= 550 and self.start_screen:
                self._running=False
            if 751<=x<=850 and 0<=y<=100 and self.game_running:
                if self.info_on_screen==False:
                    self.info_on_screen=True

                elif self.info_on_screen:
                    self.info_on_screen = False
            # Instruction button is pressed
            if 650<=x<=749 and 0<=y<=100 and self.game_running:

                if self.instruc_on_screen==False:
                    self.instruc_on_screen=True
                elif self.instruc_on_screen:
                    self.instruc_on_screen = False
            # Reset button is pressed
            if 470 <= x <= 670 and 0 <= y <= 90 and (self.game_running or state == State.WIN):
                if self.game_running:
                    self.game_running = False
                self.start_screen = True
                self.gameState.__set_state__(State.WELCOME)
                self.toolbox.input_active = False
                print("set state to welcome")

            if 670 <= x <= 870 and 0 <= y <= 100 and state == State.WIN: #center=(770, 45)
                self._running = False

            
            if(self.gameState.__get_state__() == State.GETTING_FEEDBACK):

                if(self.levelUp):
                    self.gameState.__set_state__(State.PLAYING)
                    # get rid of bug / pop first element from toolbox's bug array
                    self.toolbox.arrOfBugs[0].location = (-1, -1)
                    self.toolbox.arrOfBugs.pop(0)
                    print("BUG POPPED") # delete this later

                    if not self.toolbox.arrOfBugs: # if empty, then set game state to win
                        self.gameState. __set_state__(State.WIN)
                        print("WIN!!!!!!!!!!!!!!")

                    self.levelUp = False
                else:
                    self.gameState.__set_state__(State.PROMPTING)


        # Event: key is pressed
        # Currently checking: if game state is in prompting to collect user input
        if event.type == pygame.KEYDOWN:
            
            if self.toolbox.input_active:
                if event.key == pygame.K_RETURN:
                    # Send the prompt to Google Gemini/ make API call
                    response =  self.user_text
                    
                    if self.toolbox.arrOfBugs[0].word_duck_is_trying_to_guess in response.lower() :
                        self.toolbox.myAPI.makeAPICall(("The user just used a restricted word. Give them a rating of 0. Format response with 'yourRating/10 : yourexplanation'"))
                        self.restrictedWord = True
                    else:
                        self.toolbox.myAPI.makeAPICall(("What is your rating ( on a scale of 1-10 ) for this prompt if I was trying to get you to say: ", self.toolbox.arrOfBugs[0].word_duck_is_trying_to_guess, ". The prompt is: ", response, ". Format response with 'yourRating/10 : yourexplanation'"))
                        self.restrictedWord = False
                   
                    self.gameState.__set_state__(State.GETTING_FEEDBACK)

                    self.user_text = ""  # Reset input


                elif event.key == pygame.K_BACKSPACE:
                    self.user_text =  self.user_text [:-1]  # Remove last character
                else:
                    self.user_text += event.unicode  # Add typed character


    def on_loop(self):

        state = self.gameState.__get_state__()


        if state == State.WELCOME and self.start_screen:
            self.on_render()
            # print("EVERYTHING RENDERED!") # delete this later
           # self.gameState. __set_state__(State.PLAYING)

        # print("State: " , state) # CAN UNCOMMENT THIS LATER
        if state == State.PLAYING and self.game_running:
            # Welcome Screen Graphics
            game_screen_image = pygame.image.load("images/game_background.png")
            self._display_surf.blit(game_screen_image, game_screen_image.get_rect(topleft=(0, 0)))
            
            # Duck Playing Graphics
            self.toolbox.keys = pygame.key.get_pressed()

            if not self.toolbox.input_active:
                self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y = self.toolbox.myDuck.move_duck(
                    self.toolbox.keys, self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y)

            # Check to see if duck is near bug
            if self.toolbox.myDuck.is_near_bug(self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y,
                                               self.toolbox.arrOfBugs[0].location[0],
                                               self.toolbox.arrOfBugs[0].location[1]):

                self.gameState.__set_state__(State.PROMPTING)
                self.toolbox.input_active = True

            # display duckie
            self._display_surf.blit(self.toolbox.myDuck.duck_img,
                                    (self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y))
            # display bug
            self._display_surf.blit(self.toolbox.arrOfBugs[0].bug_img,
                                    self.toolbox.arrOfBugs[0].location)
            
            info_button = pygame.image.load("images/info_button.png")
            instruc_button = pygame.image.load("images/instruc_button.png")
            restart_button= pygame.image.load("images/restart.png")
            gemini_logo = pygame.image.load("images/gemini_logo.png")
            self._display_surf.blit(restart_button, restart_button.get_rect(center=(570,45)))
            self._display_surf.blit(info_button, info_button.get_rect(topright=(850, 0)))
            self._display_surf.blit(instruc_button, instruc_button.get_rect(topright=(750, 0)))
            self._display_surf.blit(gemini_logo, gemini_logo.get_rect(bottomleft=(5, 695)))
            if self.info_on_screen:
                info_tab = pygame.image.load("images/info_tab.png")
                self._display_surf.blit(info_tab, info_tab.get_rect(topright=(875, 100)))
            if self.instruc_on_screen:
                instruc_tab = pygame.image.load("images/instruc_tab.png")
                self._display_surf.blit(instruc_tab, instruc_tab.get_rect(topleft=(75, 100)))


        if state == State.PROMPTING and self.game_running:
            # display win screen make sure win screen has restart button
            # once restart button is clicked, send user back to welcome
            game_screen_image =  pygame.image.load("images/game_background.png")
            self._display_surf.blit(game_screen_image, game_screen_image.get_rect(topleft=(0,0)))
             # display duckie
            self._display_surf.blit(self.toolbox.myDuck.duck_img,
                                    (self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y))
            # display bug
            self._display_surf.blit(self.toolbox.arrOfBugs[0].bug_img,
                                    self.toolbox.arrOfBugs[0].location)

            self.draw_text_box()
            info_button = pygame.image.load("images/info_button.png")
            instruc_button = pygame.image.load("images/instruc_button.png")
            restart_button= pygame.image.load("images/restart.png")
            gemini_logo = pygame.image.load("images/gemini_logo.png")
            self._display_surf.blit(restart_button, restart_button.get_rect(center=(570,45)))
            self._display_surf.blit(info_button, info_button.get_rect(topright=(850, 0)))
            self._display_surf.blit(instruc_button, instruc_button.get_rect(topright=(750, 0)))
            self._display_surf.blit(gemini_logo, gemini_logo.get_rect(bottomleft=(5, 695)))
            # display text box of bug word (the word that the user needs Gemini to guess)
            word = self.toolbox.arrOfBugs[0].returnText()
            self._display_surf.blit(word, (self.toolbox.arrOfBugs[0].location[0], self.toolbox.arrOfBugs[0].location[1] - BUG_RADIUS/2))

            self.renderText(self.user_text)
            if self.info_on_screen:
                info_tab = pygame.image.load("images/info_tab.png")
                self._display_surf.blit(info_tab, info_tab.get_rect(topright=(875, 100)))
            if self.instruc_on_screen:
                instruc_tab = pygame.image.load("images/instruc_tab.png")
                self._display_surf.blit(instruc_tab, instruc_tab.get_rect(topleft=(75, 100)))

        if state == State.WIN and self.game_running:
            end_screen_image = pygame.image.load("images/win_screen.png")
            self._display_surf.blit(end_screen_image, end_screen_image.get_rect(topleft=(0, 0)))
            restart_button = pygame.image.load("images/restart.png")
            self._display_surf.blit(restart_button, restart_button.get_rect(center=(570, 45)))
            exit_button = pygame.image.load("images/exit.png")
            self._display_surf.blit(exit_button, exit_button.get_rect(center=(770, 45)))

        if state == State.GETTING_FEEDBACK and self.game_running:
            #print(self.toolbox.myAPI.getFeedback())
            self.draw_text_box()

            if(("incorrect" in self.toolbox.myAPI.getFeedback().lower()) or ("try again" in self.toolbox.myAPI.getFeedback().lower()) or self.restrictedWord):
           
                self.renderText((self.toolbox.myAPI.getFeedback()))

                #print((self.toolbox.myAPI.getFeedback() + ". Don't use the word!"))
                #must have some way of keeping feedback on screen before prmopting again
            else:
                rating = (int) (self.toolbox.myAPI.getRating((self.toolbox.myAPI.getFeedback())))
            
                # print("rating: ", rating) # delete - later
                if rating > THRESHOLD:
                    self.renderText((self.toolbox.myAPI.getFeedback()))
                    self.toolbox.input_active = False
                    self.levelUp = True
                    # print("bug word: ", self.toolbox.arrOfBugs[0].word_duck_is_trying_to_guess) # delete this later
                    # check if the bug array is empty
                    
                else:
                    self.renderText((self.toolbox.myAPI.getFeedback() + ". Try again!"))


        self.toolbox.clock.tick(60)

        pygame.display.flip()



    def on_render(self):
        # Make a copy of the constant words
        self.toolbox.words_array = WORDS[:]
        #print(self.toolbox.words_array) - delete this later
        self.toolbox.arrOfBugs = []
        self.toolbox.randomizeInitBugs()
        self.user_text = ""
        self.restrictedWord = False
        # Reset location of duck
        self.toolbox.myDuck.char_x, self.toolbox.myDuck.char_y = DUCK_STARTING_POSITION
        # print("Bug location: ", self.toolbox.arrOfBugs[0].location[0], ", ", self.toolbox.arrOfBugs[0].location[1])
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
        # Draw the text box (background)
        text_box = pygame.image.load("images/text_box.png")
        
        self._display_surf.blit(text_box, text_box.get_rect(center=(450, 600)))

        # pygame.display.flip()  # Update the display
        # pygame.draw.rect(self._display_surf, (255, 255, 255), (200, 500, 500, 50))
        # pygame.draw.rect(self._display_surf, (0, 0, 0), (200, 500, 500, 50), 2)
        # text_surface = self.font.render( text, True, (0, 0, 0))
        # self._display_surf.blit(text_surface, (210, 510))

    def renderText(self, input):

        lines = textwrap.wrap(input, width = 500 // self.font.size(" ")[0])
        y_offset = 0

        for line in lines:
            self.text_surface = self.font.render(line, True, (0,0,0))
            self._display_surf.blit(self.text_surface, (200, 565 + y_offset))
            y_offset += self.font.size(" ")[1] + 4

            if y_offset > 50:
                break

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()

        self.on_cleanup()

    def exit_render(self):
        end_screen_image = pygame.image.load("images/win_screen.png")
        self._display_surf.blit(end_screen_image, end_screen_image.get_rect(topleft=(0, 0)))
        restart_button = pygame.image.load("images/restart.png")
        self._display_surf.blit(restart_button, restart_button.get_rect(topleft=(100,200)))

        exit_button = pygame.image.load("images/exit_button.png")
        self._display_surf.blit(exit_button, exit_button.get_rect(topleft=(400,200)))
