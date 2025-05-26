from tradeview import TradeView

class TradeModel():

    def __init__(self, width, height):
        self._view = TradeView(width, height)

    def setup(self):
        self._view.setup()

    def game_step(self):
        pass

    def render(self):
        self._view.refresh()

    def space_down(self):
        self._view.dispWhite()
        
    def space_up(self):
        self._view.dispBlack()