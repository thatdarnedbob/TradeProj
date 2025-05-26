from trademodel import TradeModel
import pygame
from constants import FPS_CAP, MIN_TIK

class TradeController():

    def __init__(self, width, height):
        self._model = TradeModel(width, height)

    def setup(self):

        self.clock = pygame.time.Clock()
        self.dt = 0
        self._model.setup()

    def game_loop_step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self._model.space_down()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:    
                self._model.space_up()

        self._model.game_step()

        self.dt += self.clock.tick()
        if self.dt > MIN_TIK:
            self.dt -= MIN_TIK
            self._model.render()