from model.trademodel import TradeModel
import pygame as pg
from constants import FPS_CAP, MIN_TIK

class TradeController():

    def __init__(self, width, height):
        self._model = TradeModel(width, height)

    def setup(self):

        self.clock = pg.time.Clock()
        self.dt = 0
        self._model.setup()

    def game_loop_step(self):
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    return "exit"
                case pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self._model.space_down()
                case pg.KEYUP:
                    if event.key == pg.K_SPACE:    
                        self._model.space_up()

        self._model.game_step()

        self.dt += self.clock.tick()
        if self.dt > MIN_TIK:
            self.dt -= MIN_TIK
            self._model.render()