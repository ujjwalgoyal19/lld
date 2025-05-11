from color import Color
from pieces.piece import Piece


class Pawn(Piece):
    def can_move(self, board, dest_row, dest_col):
        row_diff, col_diff = self.__calculate_diff(dest_row=dest_row, dest_col=dest_col)

        piece_is_at_starting_location = (
            self.color == Color.WHITE and self.row == 1
        ) or (self.color == Color.BLACK and self.row == 6)
        dest_piece: Piece = board.get_piece(dest_row, dest_col)

        return (
            (piece_is_at_starting_location and col_diff == 0 and row_diff <= 2)
            or (
                row_diff == 1
                and col_diff == 1
                and dest_piece is not None
                and dest_piece.color != self.color
            )
            or (row_diff == 1 and col_diff == 0 and dest_piece is None)
        )
