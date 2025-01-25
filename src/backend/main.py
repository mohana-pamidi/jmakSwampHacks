import pygame, sys


if __name__ == "__main__":
    screen = pygame.display.set_mode((900, 700))
    pygame.init()
    start_screen=True
    game_running=False
    game_finish=False
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if start_screen:
                screen.fill((125, 199, 242))  # Background color
                start_screen_image = pygame.image.load("../images/Start screen.png")
                screen.blit(start_screen_image, start_screen_image.get_rect(topleft=(0, 0)))
                start_button=pygame.image.load("../images/Start.png")
                screen.blit(start_button,start_button.get_rect(center=(450,525)))
                pygame.display.flip()
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                if 275<=x<=600 and 425<=y<=625:
                    start_screen=False
                    game_running=True
            if game_running:
                screen.fill((125, 199, 242))
                pygame.display.flip()






