import pygame
from constants import *
from controller.tradecontroller import TradeController

def main():

    tradecontroller = TradeController(SCREEN_WIDTH, SCREEN_HEIGHT)
    tradecontroller.setup()

    while(True):
        program_action = tradecontroller.game_loop_step()
        if program_action == "exit":
            return

if __name__ == "__main__":
    main()