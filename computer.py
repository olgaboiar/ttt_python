import random

class Computer:
    def __init__(self):
        pass

    def choose_move(self, board):
        return (random.choice(board.available_spots()))

   