import pygame as pg

class TradeView():
    def setup(self):
        pg.init()

        self.screen = pg.display.set_mode((self._screen_width, self._screen_height), vsync=1)

        pg.display.set_caption("The Many Waters of Boolea")
        pg.mouse.set_visible(False)

        self.bg = pg.Surface(self.screen.get_size())
        self.bg = self.bg.convert()
        self.bg.fill("black")

        font = pg.font.Font(None, 36)
        text = font.render("Hello There", 1, "green")
        textpos = text.get_rect()
        textpos.centerx = self.bg.get_rect().centerx
        self.bg.blit(text, textpos)

        self.screen.blit(self.bg, (0,0))
        pg.display.flip()

    def dispWhite(self):
        self.bg.fill("white")
    
    def dispBlack(self):
        self.bg.fill("black")

    def refresh(self):
        self.screen.blit(self.bg, (0,0))
        pg.display.flip()

    def __init__(self, width, height):
        self._screen_width = width
        self._screen_height = height
