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
        print(marker1)
        print(marker2)
        self.user_interface.print_board(self.board)
        move = self.user_interface.choose_move()
        print(move)
        player1.move(self.board, move, marker1)
        self.user_interface.print_board(self.board)


#  def choose_move(self):
#         text = "Enter a number to make your move:\n"
#         move = None
#         while not move:
#             move = self.get_input(text)
#             if self.input_validator.valid_move(move):
#                 return move
#             else:
#                 move = None