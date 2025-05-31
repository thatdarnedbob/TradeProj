from model.trademodel import TradeModel
import pygame as pg
from constants import (FPS_CAP, MIN_TIK,
                       SCREEN_WIDTH, SCREEN_HEIGHT)
import sys

class TradeController():

    def __init__(self):
        self._model = TradeModel(SCREEN_WIDTH, SCREEN_HEIGHT, self.exit)

    def setup(self):

        self.clock = pg.time.Clock()
        self.dt = 0

        self._model.setup()

    def exit(self):
        pg.quit()
        sys.exit()


    def game_loop_step(self):
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self.exit()
                    return "exit"
                case pg.KEYDOWN:
                    if self.is_down_key(event.key):
                        self._model.menu_down()
                    if self.is_up_key(event.key):    
                        self._model.menu_up()
                    if self.is_select_key(event.key):
                        self._model.execute()

        self._model.game_step()

        self.dt += self.clock.tick()
        if self.dt > MIN_TIK:
            self.dt -= MIN_TIK
            self._model.render()
        
    def is_down_key(self, key_id):
        return key_id in [pg.K_DOWN, pg.K_s, pg.K_j]
    
    def is_up_key(self, key_id):
        return key_id in [pg.K_UP, pg.K_w, pg.K_k]
    
    def is_select_key(self, key_id):
        return key_id in [pg.K_SPACE, pg.K_KP_ENTER, pg.K_RETURN]