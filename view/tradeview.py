import pygame as pg
from constants import (MENU_X_OFFSET, MENU_Y_OFFSET,
                       MENU_X_STAGGER, MENU_Y_STAGGER)

class TradeView():
    def setup(self):
        pg.init()

        self.screen = pg.display.set_mode((self._screen_width, self._screen_height), vsync=1)

        pg.display.set_caption("The Many Waters of Boolea")
        pg.mouse.set_visible(False)

        self.menus = pg.Surface(self.screen.get_size())
        self.menus = self.menus.convert()
        self.menus.fill("black")
        self.menu_strings = []

        self.screen.blit(self.menus, (0,0))
        pg.display.flip()

    def dispWhite(self):
        self.bg.fill("white")
    
    def dispBlack(self):
        self.bg.fill("black")

    def acceptNewMenu(self, menu_array):
        self.menu_strings = menu_array
        font = pg.font.Font(None, 36)
        for i in range(len(self.menu_strings)):
            text = font.render(self.menu_strings[i], 1, "green")
            
            self.menus.blit(text, (MENU_X_OFFSET + MENU_X_STAGGER * i,
                                   MENU_Y_OFFSET + MENU_Y_STAGGER * i))
            

    def refresh(self):
        self.screen.blit(self.menus, (0,0))
        pg.display.flip()

    def __init__(self, width, height):
        self._screen_width = width
        self._screen_height = height
