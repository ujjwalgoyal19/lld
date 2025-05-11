from color import Color
from pieces.piece import Piece


class Move:
    def __init__(self, piece: Piece, row: int, col: int):
        self.piece = piece
        self.dest_row = row
        self.dest_col = col
