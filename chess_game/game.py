from typing import List

from board import Board
from color import Color
from move import Move
from player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(color=Color.WHITE), Player(color=Color.BLACK)]
        self.current_player = 0

    def start(self):
        while not self._is_game_over():
            player = self.players[self.current_player]
            try:
                move: Move = self._get_player_move(player)

                if move:
                    player.make_move(board=self.board, move=move)
                    self.current_player = (self.current_player + 1) % 2
            except Exception as e:
                print(f"Error: {e}")
            finally:
                pass

    def _get_player_move(self, player: Player):
        source_row = int(input("Enter source row:"))
        source_col = int(input("Enter source col:"))
        dest_row = int(input("Enter destination row:"))
        dest_col = int(input("Enter destination col:"))

        piece = self.board.get_piece(row=source_row, col=source_col)
        if piece is None or piece.color != player.color:
            raise ValueError("Invalid piece selection!")

        return Move(piece=piece, row=dest_row, col=dest_col)

    def _is_game_over(self):
        return (
            self.board.is_checkmate(color=Color.WHITE)
            or self.board.is_checkmate(color=Color.BLACK)
            or self.board.is_stalemate(color=Color.WHITE)
            or self.board.is_stalemate(color=Color.BLACK)
        )
