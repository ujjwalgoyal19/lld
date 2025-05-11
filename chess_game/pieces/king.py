from pieces.piece import Piece


class King(Piece):
    def can_move(self, board, dest_row, dest_col):
        row_diff, col_diff = self.__calculate_diff(dest_col=dest_col, dest_row=dest_row)
        return row_diff <= 1 and col_diff <= 1
