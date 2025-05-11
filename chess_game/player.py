from turtle import colormode

from board import Board
from color import Color
from move import Move


class Player:
    def __init__(self, color: Color):
        self.color = color

    def make_move(self, board: Board, move: Move):
        piece = move.piece
        dest_row = move.dest_row
        dest_col = move.dest_col

        if board.is_valid_move(piece=piece, dest_row=dest_row, dest_col=dest_col):
            source_row = piece.row
            source_col = piece.col
            board.set_piece(piece=None, row=source_row, col=source_col)
            board.set_piece(piece=piece, row=dest_row, col=dest_col)
            piece.row = dest_row
            piece.col = dest_col
        else:
            raise ValueError("Invalid Move!")
