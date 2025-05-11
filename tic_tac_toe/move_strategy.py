from abc import ABC, abstractmethod

from board import Board


class MoveStrategy(ABC):
    @abstractmethod
    def is_valid_move(self, x: int, y: int, board: Board):
        pass


class DefaultMoveStrategy(MoveStrategy):
    def is_valid_move(self, x, y, board):
        return board.get_cell(x, y) == None
