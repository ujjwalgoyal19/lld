from typing import List


class Board:
    def __init__(self, size):
        self._board: List[List[chr]] = [
            [None for _ in range(size)] for _ in range(size)
        ]
        self._observers: List[any] = list()

    def add_observer(self, observer: any):
        if not observer:
            raise ValueError("Observer cannot be None")
        self._observers.append(observer)

    def __notify_observers(self):
        for obs in self._observers:
            obs.update(self)

    def update_board(self, x: int, y: int, symbol: chr):
        self._board[x][y] = symbol
        self.__notify_observers()

    def get_cell(self, x: int, y: int) -> chr:
        return self._board[x][y]

    def get_size(self):
        return len(self._board)
