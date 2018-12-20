from game import Game
from ui import Ui

user_interface = Ui()
game = Game(user_interface)
game.start()
game.play()
