import random
from players.player import Player

class Computer(Player):
    def __init__(self, marker):
        Player.__init__(self, marker)

    def choose_move(self, board):
        return random.choice(board.available_spots())
