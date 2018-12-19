from player import Player
from board import Board

class Game:
    def __init__(self, user_interface):
        self.user_interface = user_interface
        self.board = Board()

    def start(self):
        self.user_interface.greet()
        marker1 = self.user_interface.choose_marker()
        player1 = Player(marker1)
        marker2 = player1.define_marker(marker1)
        player2 = Player(marker2)
        self.user_interface.print_board(self.board)
        move1 = self.user_interface.choose_move(self.board)
        player1.move(self.board, move1, marker1)
        self.user_interface.print_board(self.board)
        move2 = self.user_interface.choose_move(self.board)
        player2.move(self.board, move2, marker2)
        self.user_interface.print_board(self.board)
