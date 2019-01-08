from players.human import Human
from players.computer import Computer

class PlayerFactory:
    def __init__(self):
        pass

    def create_player(self, player_type, marker, db):
        targetclass = player_type.capitalize()
        return globals()[targetclass](marker, db)
