from player import Player
from ui import Ui

class Human(Player):
    def __init__(self, marker):
        Player.__init__(self, marker)

    def choose_move(self, board):
        user_interface = Ui()
        return user_interface.choose_move(board)
