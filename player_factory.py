from human import Human
from computer import Computer

class PlayerFactory:
    def __init__(self):
        pass

    def create_player(self, player_type, marker):
        targetclass = player_type.capitalize()
        return globals()[targetclass](marker)
