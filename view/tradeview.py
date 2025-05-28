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

        self.screen.blit(self.menus, (0,0))
        pg.display.flip()

    def dispWhite(self):
        self.bg.fill("white")
    
    def dispBlack(self):
        self.bg.fill("black")

    def acceptNewMenu(self, menu_array, selected):
        self.menus.fill("black")
        font = pg.font.Font(None, 36)
        for i in range(len(menu_array)):
            if i == selected:
                self.menus.fill("red", pg.Rect(MENU_X_OFFSET, MENU_Y_OFFSET + i * MENU_Y_STAGGER,
                                               20, 25))
            text = font.render(f"{i + 1} - {menu_array[i]}", 1, "green")
                
            self.menus.blit(text, (MENU_X_OFFSET + MENU_X_STAGGER * i,
                                   MENU_Y_OFFSET + MENU_Y_STAGGER * i))
            

    def refresh(self):
        self.screen.fill("black")
        self.screen.blit(self.menus, (0,0))
        pg.display.flip()

    def __init__(self, width, height):
        self._screen_width = width
        self._screen_height = height
