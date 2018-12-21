from game import Game
from ui import Ui
from board import Board

user_interface = Ui()
board = Board()
game = Game(user_interface)
game.start()
game.play(board)
