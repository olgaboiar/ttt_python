import unittest
from game import Game
from ui import Ui
from board import Board

class GameTest(unittest.TestCase):
    def setUp(self):
        user_interface = Ui()
        self.game = Game(user_interface)
        self.board = Board()

    def test_start(self):
        pass

if __name__ == '__main__':
    unittest.main()
