import pygame
from pygame.locals import *
import sys

# Initialize pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
CHAR_SIZE = 40
MOVE_SPEED = 5

''' FUNCTIONS '''
# this function moves the duck character around
def move_character(keys, x, y):
    """
    Update character position based on keyboard input.

    :param keys: List of currently pressed keys.
    :param x: Current x-coordinate of the character.
    :param y: Current y-coordinate of the character.
    :return: Updated x, y coordinates.
    """
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

# Create the screen/window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("DuckieAIventure")

# Initial character position
char_x, char_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Update character position
    char_x, char_y = move_character(keys, char_x, char_y)

    # Fill the screen with a color (e.g., black)
    screen.fill((125, 199, 242))

    
    img = pygame.image.load("../images/duckie.png")

    screen.blit(img, (0,0))

    # Update the display
    pygame.display.update()
    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
