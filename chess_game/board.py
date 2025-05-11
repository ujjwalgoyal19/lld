from typing import List

from color import Color
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.piece import Piece
from pieces.queen import Queen
from pieces.rook import Rook


class Board:
    def __init__(self):
        self.board: List[List[Piece]] = [[None] * 8 for _ in range(8)]
        self._initialize_board()

    def _initialize_board(self):
        self.board[7][0] = Rook(color=Color.BLACK, row=0, col=0)
        self.board[7][1] = Bishop(color=Color.BLACK, row=0, col=1)
        self.board[7][2] = Knight(color=Color.BLACK, row=0, col=2)
        self.board[7][3] = Queen(color=Color.BLACK, row=0, col=3)
        self.board[7][4] = King(color=Color.BLACK, row=0, col=4)
        self.board[7][5] = Knight(color=Color.BLACK, row=0, col=5)
        self.board[7][6] = Bishop(color=Color.BLACK, row=0, col=6)
        self.board[7][7] = Rook(color=Color.BLACK, row=0, col=7)
        for i in range(8):
            self.board[6][i] = Pawn(color=Color.BLACK, row=1, col=i)

        self.board[0][0] = Rook(color=Color.WHITE, row=7, col=0)
        self.board[0][1] = Bishop(color=Color.WHITE, row=7, col=1)
        self.board[0][2] = Knight(color=Color.WHITE, row=7, col=2)
        self.board[0][3] = Queen(color=Color.WHITE, row=7, col=3)
        self.board[0][4] = King(color=Color.WHITE, row=7, col=4)
        self.board[0][5] = Knight(color=Color.WHITE, row=7, col=5)
        self.board[0][6] = Bishop(color=Color.WHITE, row=7, col=6)
        self.board[0][7] = Rook(color=Color.WHITE, row=7, col=7)
        for i in range(8):
            self.board[1][i] = Pawn(color=Color.WHITE, row=6, col=i)

    def get_piece(self, row, col):
        if row >= 8 or col >= 8:
            raise ValueError("Piece can only present inside the Chess Board")
        return self.board[row][col]

    def set_piece(self, piece: Piece, row: int, col: int):
        if row >= 8 or col >= 8:
            raise ValueError("Piece can only present inside the Chess Board")
        self.board[row][col] = piece

    def is_valid_move(self, piece: Piece, dest_row: int, dest_col: int):
        if (
            piece is None
            or dest_row < 0
            or dest_col < 0
            or dest_row > 7
            or dest_col > 7
        ):
            return False

        dest_piece: Piece = self.board[dest_row][dest_col]
        return (
            dest_piece is None or dest_piece.color != piece.color
        ) and piece.can_move(self, dest_row=dest_row, dest_col=dest_col)

    def is_checkmate(self, color):
        # TODO: Implement checkmate logic
        return False

    def is_stalemate(self, color):
        # TODO: Implement stalemate logic
        return False
