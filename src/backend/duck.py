import pygame
import sys

# Initialize pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

# Create the screen/window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("DuckieAIventure")

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (e.g., black)
    screen.fill((125, 199, 242))

    
    img = pygame.image.load("C:/Users/SRIDH/Projects/jmakSwampHacks/src/images/duckie.png")

    screen.blit(img, (0,0))

    # Update the display
    pygame.display.update()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
