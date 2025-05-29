import pygame as pg
from constants import (MENU_X_OFFSET, MENU_Y_OFFSET,
                       MENU_X_STAGGER, MENU_Y_STAGGER,
                       BG_COLOR, SEL_HIGHLIGHT_COLOR, MENU_TEXT_COLOR, MENUS_MASK_COLOR)


class TradeView():
    def setup(self):
        pg.init()

        self.screen = pg.display.set_mode((self._screen_width, self._screen_height), vsync=1)

        pg.display.set_caption("The Many Waters of Boolea")
        pg.mouse.set_visible(False)

        self.menus = pg.Surface(self.screen.get_size()).convert()
        self.menus.fill(MENUS_MASK_COLOR)
        self.menus.set_colorkey(MENUS_MASK_COLOR)

        self._bg = pg.Surface(self.screen.get_size()).convert()
        self._bg.fill(pg.Color(BG_COLOR))

        self.screen.blit(self.menus, (0,0))
        pg.display.flip()

    def acceptNewMenu(self, menu_array, selected):
        self.menus.fill(MENUS_MASK_COLOR)
        font = pg.font.SysFont('couriernew', 36)
        for i in range(len(menu_array)):
            if i == selected:
                num_size = font.size(f"{i + 1}")
                self.menus.fill(SEL_HIGHLIGHT_COLOR, pg.Rect((MENU_X_OFFSET, MENU_Y_OFFSET + i * MENU_Y_STAGGER),
                                               num_size))
            text = font.render(f"{i + 1} - {menu_array[i]}", 1, MENU_TEXT_COLOR)
                
            self.menus.blit(text, (MENU_X_OFFSET + MENU_X_STAGGER * i,
                                   MENU_Y_OFFSET + MENU_Y_STAGGER * i))
            

    def refresh(self):
        self.screen.blit(self._bg, (0, 0))
        self.screen.blit(self.menus, (0,0))
        pg.display.flip()

    def __init__(self, width, height):
        self._screen_width = width
        self._screen_height = height
