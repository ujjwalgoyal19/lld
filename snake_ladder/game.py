from collections import deque
from platform import win32_edition
from typing import Deque

from snake_ladder.board import Board
from snake_ladder.cell import Cell
from snake_ladder.dice import Dice
from snake_ladder.player import Player


class Game:
    def __init__(
        self, board_size, total_dices, total_snakes, total_ladders, total_players
    ):
        self.__total_cells = board_size * board_size
        self.__board_size = board_size
        self.__board: Board = Board(
            board_size=board_size,
            total_snakes=total_snakes,
            total_ladders=total_ladders,
        )
        self.__dice: Dice = Dice(number_of_dices=total_dices)
        self.__playerList: Deque[Player] = deque()
        self.__winner: Player = None
        self.__add_players(total_players)

    def __add_players(self, total_players):
        for i in range(total_players):
            new_player = Player(player_id=f"Player_{i}")
            self.__playerList.append(new_player)

    def start_game(self):
        while self.__winner == None:
            curr_player: Player = self.__playerList.popleft()
            print(
                f"Player: {curr_player.player_id} | Current Position: {curr_player.current_position}"
            )

            player_move = self.__dice.roll_dice()

            player_new_position = curr_player.current_position + player_move
            player_new_position = self.__jump_check(player_new_position)
            curr_player.move(player_new_position)

            if player_new_position > self.__total_cells:
                self.__winner = curr_player

    def __jump_check(self, current_position):
        row = current_position // self.__board_size
        col = current_position % self.__board_size
        col = -col if row % 2 == 0 else col - 1
        current_cell: Cell = self.__board[row][col]

        return current_cell.stay_or_jump()
