import pygame
from pygame.locals import *
from constants import *
import sys
import toolbox


class Duck:
    def __init__(self):
        self.imagePath = "images/Duckie.png"
        # Constants for screen dimensions
        self.char_x, self.char_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        self.duck_img = pygame.image.load(self.imagePath)

        self.duck_img = pygame.transform.scale(self.duck_img, (CHAR_SIZE, CHAR_SIZE))

    def move_duck(self, keys, x, y):

        if keys[K_UP] or keys[K_w]:
            y -= MOVE_SPEED
        if keys[K_DOWN] or keys[K_s]:
            y += MOVE_SPEED
        if keys[K_LEFT] or keys[K_a]:
            x -= MOVE_SPEED
        if keys[K_RIGHT] or keys[K_d]:
            x += MOVE_SPEED

            # keep character within screen bounds
        x = max(0, min(SCREEN_WIDTH - CHAR_SIZE, x))
        y = max(0, min(SCREEN_HEIGHT - CHAR_SIZE, y))

        return x, y


    def is_near_bug(self, duck_x, duck_y, bug_x, bug_y):
        distance = ((duck_x - bug_x) ** 2 + (duck_y - bug_y) ** 2) ** 0.5
        return distance <= BUG_RADIUS + CHAR_SIZE // 2


    #
    #
    # # Initial character position
    #
    #
    # # Set up the clock for controlling the frame rate
    # clock = pygame.time.Clock()
    #
    # # Font
    #
    # # Load Images
    # duck_img = pygame.image.load("../images/duckie.png")
    # duck_img = pygame.transform.scale(duck_img, (CHAR_SIZE, CHAR_SIZE))
    # bug_img = pygame.image.load("../images/buggie.png")
    # bug_img = pygame.transform.scale(bug_img, (60, 60))
    #
    # # Get bugs
    # for x in range(10):
    #     print(toolbox.arrOfBugs[x].get_location())
    #
    # # Text Input
    # input_active = False
    # user_text = ""
    #
    # # Main game loop
    # running = True
    #
    # while running:
    #     # Fill the screen with a color
    #     screen.fill((125, 199, 242))
    #
    #     # Handle the events
    #     for event in pygame.event.get():
    #
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #         if event.type == pygame.KEYDOWN:
    #
    #             if input_active:
    #
    #                 print("can type input_active is not false")
    #                 if event.key == pygame.K_RETURN:
    #                     # Send the prompt to Google Gemini/ make API call
    #                     response = user_text  # send_to_gemini_model(user_text)
    #                     print(response)  # Show response in the console (or handle it)
    #                     if response == "goodbye":
    #                         # get rid of bug
    #                         input_active = False
    #                         BUG_POSITION = (-31, -31)
    #                     user_text = ""  # Reset input
    #                     # input_active = False  # Deactivate text box
    #                 elif event.key == pygame.K_BACKSPACE:
    #                     user_text = user_text[:-1]  # Remove last character
    #                 else:
    #                     user_text += event.unicode  # Add typed character
    #
    #     # Get keys that are pressed
    #     keys = pygame.key.get_pressed()
    #
    #     # Update duck character position
    #     if not input_active:
    #         char_x, char_y = move_character(keys, char_x, char_y)
    #
    #     # Check to see if duck is near bug
    #     if is_near_bug(char_x, char_y):
    #         print("reset")
    #         input_active = True
    #
    #     # duck_img = pygame.transform.scale(duck_img, (CHAR_SIZE, CHAR_SIZE))
    #
    #     # Draw duck and bug images
    #     screen.blit(duck_img, (char_x, char_y))
    #     screen.blit(bug_img, (BUG_POSITION[0] - 30, BUG_POSITION[1] - 30))
    #
    #     # Draw text box for input if near bug
    #     if input_active:
    #
    #         pygame.draw.rect(screen, (255, 255, 255), (200, 500, 500, 50))
    #         pygame.draw.rect(screen, (0, 0, 0), (200, 500, 500, 50), 2)
    #         text_surface = font.render(user_text, True, (0, 0, 0))
    #         screen.blit(text_surface, (210, 510))
    #
    #     # Update the display
    #     # pygame.display.update()
    #     pygame.display.flip()
    #
    #     # Cap the frame rate to 60 fps
    #     clock.tick(60)
    #
    # # Quit pygame
    # pygame.quit()
    # sys.exit()


