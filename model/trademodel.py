from view.tradeview import TradeView
from enum import Enum

class State(Enum):
    TOP_LEVEL = 1
    RED_LEVEL = 2
    GREEN_LEVEL = 3
    BLUE_LEVEL = 4

class TradeModel():

    def __init__(self, width, height):
        self._view = TradeView(width, height)
        self._state = State.TOP_LEVEL

    def setup(self):
        self._view.setup()
        self._view.acceptNewMenu(self.createMainMenu())

    def createMainMenu(self):
        main_menu = ["Do nothing", "Do less", "Exit"]
        return main_menu

    def game_step(self):
        pass

    def render(self):

        self._view.refresh()

    def space_down(self):
        self._view.dispWhite()
        
    def space_up(self):
        self._view.dispBlack()