from abc import ABC, abstractmethod

from enums import Symbol


class Player(ABC):
    def __init__(self, symbol: Symbol):
        self.symbol = symbol

    @abstractmethod
    def make_move(self, board):
        pass


class HumanPlayer(Player):

    def make_move(self, board):
        pass


# TODO: For later
class AIPlayer(Player):
    pass
