import pygame
from constants import *
from tradeview import TradeView

def main():

    tradeview = TradeView(SCREEN_WIDTH, SCREEN_HEIGHT)

    tradeview.setup()

    clock = pygame.time.Clock()
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                tradeview.dispWhite()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:    
                tradeview.dispBlack()
        tradeview.refresh()
        dt += clock.tick(FPS_CAP) / 1000

if __name__ == "__main__":
    main()