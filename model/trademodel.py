from view.tradeview import TradeView
from enum import Enum

class TradeModel():
    # for scope limitation, let's have the TradeModel class handle its own menu logic.
    def __init__(self, width, height, exit_command):
        self._view = TradeView(width, height)
        self.current_menu = ["Default string, none"]
        self.menu_selection = 0
        self._exit_command = exit_command

    def setup(self):
        self._view.setup()
        self.createMainMenu()
        self._view.updateMenu(self.current_menu, self.menu_selection)

    def createMainMenu(self):
        self.current_menu = ["Do nothing", "Do less", "Goods", "Exit"]
        self.menu_actions = [None, None, None, self._exit_command]
        self.menu_selection = 0

    def game_step(self):
        pass

    def render(self):
        self._view.refresh()

    def menu_down(self):
        if self.menu_selection < len(self.current_menu) - 1:
            self.menu_selection += 1
            self._view.updateMenu(self.current_menu, self.menu_selection)
    
    def menu_up(self):
        if self.menu_selection > 0:
            self.menu_selection -= 1
            self._view.updateMenu(self.current_menu, self.menu_selection)
    
    def execute(self):
        self.menu_actions[self.menu_selection]()