from view.tradeview import TradeView
from enum import Enum

class TradeModel():

    def __init__(self, width, height):
        self._view = TradeView(width, height)
        self.current_menu = ["Default string, none"]
        self.menu_selection = 0

    def setup(self):
        self._view.setup()
        self.createMainMenu()
        self._view.acceptNewMenu(self.current_menu, self.menu_selection)

    def createMainMenu(self):
        self.current_menu = ["Do nothing", "Do less", "Exit"]
        self.menu_selection = 0

    def game_step(self):
        pass

    def render(self):
        self._view.acceptNewMenu(self.current_menu, self.menu_selection)
        # self._view.updateMenuSelection(self.menu_selection)
        self._view.refresh()

    def menu_down(self):
        if self.menu_selection < len(self.current_menu) - 1:
            self.menu_selection += 1
    def menu_up(self):
        if self.menu_selection > 0:
            self.menu_selection -= 1