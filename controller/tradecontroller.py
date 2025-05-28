from model.trademodel import TradeModel
import pygame as pg
from constants import (FPS_CAP, MIN_TIK,
                       SCREEN_WIDTH, SCREEN_HEIGHT)

class TradeController():

    def __init__(self):
        self._model = TradeModel(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):

        self.clock = pg.time.Clock()
        self.dt = 0

        self._model.setup()

    def game_loop_step(self):
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    pg.quit()
                    return "exit"
                case pg.KEYDOWN:
                    if event.key == pg.K_DOWN:
                        self._model.menu_down()
                    if event.key == pg.K_UP:    
                        self._model.menu_up()

        self._model.game_step()

        self.dt += self.clock.tick()
        if self.dt > MIN_TIK:
            self.dt -= MIN_TIK
            self._model.render()