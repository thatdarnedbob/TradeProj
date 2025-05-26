import pygame as pg

class TradeView():
    def setup(self):
        pg.init()

        self.screen = pg.display.set_mode((self._screen_width, self._screen_height), vsync=1)
        self.screen.fill("black")

        pg.display.set_caption("The Many Waters of Boolea")
        pg.mouse.set_visible(False)

        pg.display.flip()

    def dispWhite(self):
        self.screen.fill("white")
    
    def dispBlack(self):
        self.screen.fill("black")

    def refresh(self):
        pg.display.flip()

    def __init__(self, width, height):
        self._screen_width = width
        self._screen_height = height
