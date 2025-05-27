from view.tradeview import TradeView
from enum import Enum

class state(Enum):
    TOP_LEVEL = 1
    RED_LEVEL = 2
    GREEN_LEVEL = 3
    BLUE_LEVEL = 4

class TradeModel():

    def __init__(self, width, height):
        self._view = TradeView(width, height)

    def setup(self):
        self._view.setup()

    def game_step(self):
        pass

    def render(self):
        self._view.refresh()

    def space_down(self):
        self._view.dispWhite()
        
    def space_up(self):
        self._view.dispBlack()