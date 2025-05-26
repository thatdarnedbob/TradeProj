import pygame

class TradeView():
    def setup(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self._screen_width, self._screen_height), vsync=1)
        self.screen.fill("black")
        pygame.display.flip()

    def dispWhite(self):
        self.screen.fill("white")
    
    def dispBlack(self):
        self.screen.fill("black")

    def refresh(self):
        pygame.display.flip()

    def __init__(self, width, height):
        self._screen_width = width
        self._screen_height = height
