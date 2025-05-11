import random
from typing import List

from snake_ladder.cell import Cell
from snake_ladder.jump import Jump


class Board:

    def __init__(self, board_size, total_snakes, total_ladders):
        self.__board_size = board_size
        self.__total_snakes = total_snakes
        self.__total_ladders = total_ladders
        self.__used_cells = set()
        self.__board: List[Cell] = []
        for i in range(board_size):
            row = []
            for j in range(board_size):
                col = board_size - j if (i + 1) % 2 == 0 else j
                position = i * board_size + col
                row.append(Cell(position=position))
            self.__board.append(row)

    def add_snakes(self):
        t_snakes = self.__total_snakes
        while t_snakes:
            start = [
                random.randint(0, self.__board_size - 1),
                random.randint(0, self.__board_size - 1),
            ]

            end = [
                random.randint(0, start[0] - 1),
                random.randint(0, self.__board_size - 1),
            ]

            if start in self.__used_cells or end in self.__used_cells:
                continue
            self.__used_cells.add(start)
            self.__used_cells.add(end)

            current_cell = self.__board[start[0]][start[1]]
            jump = Jump(end=end)
            current_cell.set_jump(jump)
            t_snakes -= 1

    def add_ladders(self):
        t_ladders = self.__total_ladders
        while t_ladders:
            start = [
                random.randint(0, self.__board_size - 2),
                random.randint(0, self.__board_size - 1),
            ]

            end = [
                random.randint(start[0] + 1, self.__board_size - 1),
                random.randint(0, self.__board_size - 1),
            ]

            if start in self.__used_cells or end in self.__used_cells:
                continue
            self.__used_cells.add(start)
            self.__used_cells.add(end)

            current_cell = self.__board[start[0]][start[1]]
            jump = Jump(end=end)
            current_cell.set_jump(jump)
            t_ladders -= 1
