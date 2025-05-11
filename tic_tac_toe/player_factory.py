from enums import PlayerType


class PlayerFactory:
    def __init__(self):
        pass

    def create_player(self, player_type: PlayerType):
        if player_type == PlayerType.HumanPlayer:
            # TODO: Call Human Player Class
            pass
        elif player_type == PlayerType.AIPlayer:
            # TODO: Call AI Player Class
            pass
        else:
            raise ValueError("Unknown Player Type")
