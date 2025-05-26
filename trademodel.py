from tradeview import TradeView

class TradeModel():

    def __init__(self, width, height):
        self._view = TradeView(width, height)
        self._view.setup()

    def setup(self):
        pass

    def game_step(self):
        self._view.refresh()

    def space_down(self):
        self._view.dispWhite()
    def space_up(self):
        self._view.dispBlack()