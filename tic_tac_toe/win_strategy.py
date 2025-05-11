from abc import ABC, abstractmethod

from board import Board


class WinStrategy(ABC):
    @abstractmethod
    def check_win(self, board: Board, symbol: chr): ...


class DefaultWinStrategy(WinStrategy):

    def __check_row(self, board: Board, symbol, i):
        size = board.get_size()

        for col in range(size):
            if board.get_cell(i, col) != symbol:
                return False

        return True

    def __check_col(self, board: Board, symbol, i):
        size = board.get_size()

        for row in range(size):
            if board.get_cell(row, i) != symbol:
                return False

        return True

    def __check_diagonal(self, board: Board, symbol):
        size = board.get_size()

        for rc in range(size):
            if board.get_cell(rc, rc) != symbol:
                return False

        return True

    def __check_anti_diagonal(self, board: Board, symbol):
        size = board.get_size()

        for rc in range(size):
            if board.get_cell(rc, size - rc - 1) != symbol:
                return False

        return True

    def check_win(self, board, symbol):
        size = board.get_size()

        for i in range(size):
            if self.__check_row(board, symbol, i) or self.__check_col(board, symbol, i):
                return True

        return self.__check_diagonal(board, symbol) or self.__check_anti_diagonal(
            board, symbol
        )
