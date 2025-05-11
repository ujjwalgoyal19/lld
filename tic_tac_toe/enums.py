from enum import Enum


class Symbol(Enum):
    X, O = range(2)


class PlayerType(Enum):
    HumanPlayer, AIPlayer = range(2)
