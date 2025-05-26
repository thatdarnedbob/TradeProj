import pygame
from constants import *
from tradeview import TradeView
from trademodel import TradeModel

def main():

    trademodel = TradeModel(SCREEN_WIDTH, SCREEN_HEIGHT)
    # tradecontroller = TradeController(tradeview)
    trademodel.setup()

    clock = pygame.time.Clock()
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                trademodel.space_down()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:    
                trademodel.space_up()
        trademodel.game_step()
        dt += clock.tick(FPS_CAP) / 1000

if __name__ == "__main__":
    main()