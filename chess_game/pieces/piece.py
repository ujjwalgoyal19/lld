from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def __calculate_diff(self, dest_row, dest_col):
        return abs(dest_row - self.row), abs(dest_col - self.col)

    @abstractmethod
    def can_move(self, board, dest_row, dest_col):
        pass
