import pygame
import random
def draw_board(screen):
    for i in range(1,16):
        pygame.draw.line(screen, (255,255,255), (0,i*32), (640,i*32))
    for i in range(1,20):
        pygame.draw.line(screen,(255,255,255), (i*32,0), (i*32,512))



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y=event.pos
                    row=y//32
                    col=x//32
                    if row*32==mole_y and col*32==mole_x:
                        mole_x = random.randrange(0, 20)*32
                        mole_y = random.randrange(0, 16)*32
                        screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x,mole_y)))

            screen.fill("light green")
            draw_board(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()



if __name__ == "__main__":
    main()
