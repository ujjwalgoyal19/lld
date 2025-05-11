class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.current_position = 0

    def move(self, new_position):
        self.current_position = new_position
