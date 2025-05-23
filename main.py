import pygame
from constants import *

def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")
    pygame.display.flip()

    clock = pygame.time.Clock()
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                screen.fill("white")
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:    
                screen.fill("black")
        pygame.display.flip()
        dt += clock.tick(FPS_CAP) / 1000

if __name__ == "__main__":
    main()