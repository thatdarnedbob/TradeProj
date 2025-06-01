from view.tradeview import TradeView
from enum import Enum
from model.WorldManager import WorldManager
import gc

class TradeModel():
    def __init__(self, width, height, exit_command):
        self._view = TradeView(width, height)
        self.current_menu = None
        self.menu_actions = None
        self.menu_selection = [0]

        self._exit_command = exit_command

    def setup(self):
        self._view.setup()
        self._world = WorldManager()
        self.createMainMenu()

    def createMainMenu(self):
        self.current_menu = ["Towns", "Ships", "Goods", "Exit"]
        self.menu_actions = [self.createTownsMenu, self.createShipsMenu, self.createGoodsMenu, self._exit_command]
        self._view.updateMenu(self.current_menu, self.menu_selection[-1])

    def backToMainMenu(self):
        del self.current_menu
        del self.menu_actions
        gc.collect()

        self.menu_selection.pop()
        self.current_menu = ["Towns", "Ships", "Goods", "Exit"]
        self.menu_actions = [self.createTownsMenu, self.createShipsMenu, self.createGoodsMenu, self._exit_command]
        self._view.updateMenu(self.current_menu, self.menu_selection[-1])
    
    def createTownsMenu(self):
        '''del self.current_menu
        del self.menu_actions
        gc.collect()'''

        self.current_menu = self._world.disp_town_list()
        self.menu_actions = [None] * self._world.num_of_towns()

        self.current_menu.append("Back to Main Menu")
        self.menu_actions.append(self.backToMainMenu)

        self.menu_selection.append(0)
        self._view.updateMenu(self.current_menu, self.menu_selection[-1])

    def createShipsMenu(self):
        '''del self.current_menu
        del self.menu_actions
        gc.collect()'''

        self.current_menu = self._world.disp_ship_list()
        self.menu_actions = [None] * len(self.current_menu)

        self.current_menu.append("Back to Main Menu")
        self.menu_actions.append(self.backToMainMenu)

        self.menu_selection.append(0)
        self._view.updateMenu(self.current_menu, self.menu_selection[-1])

    def createGoodsMenu(self):
        '''del self.current_menu
        del self.menu_actions
        gc.collect()'''

        self.current_menu = self._world.disp_goods_list()
        self.menu_actions = [None] * len(self.current_menu)

        self.current_menu.append("Back to Main Menu")
        self.menu_actions.append(self.backToMainMenu)

        self.menu_selection.append(0)
        self._view.updateMenu(self.current_menu, self.menu_selection[-1])

    def game_step(self):
        pass

    def render(self):
        self._view.refresh()

    def menu_down(self):
        if self.menu_selection[-1] < len(self.current_menu) - 1:
            self.menu_selection[-1] += 1
            self._view.updateMenu(self.current_menu, self.menu_selection[-1])
    
    def menu_up(self):
        if self.menu_selection[-1] > 0:
            self.menu_selection[-1] -= 1
            self._view.updateMenu(self.current_menu, self.menu_selection[-1])
    
    def menu_execute(self):
        if self.menu_actions[self.menu_selection[-1]]:
            self.menu_actions[self.menu_selection[-1]]()