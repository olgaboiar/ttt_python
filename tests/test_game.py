import unittest
import io
import sys
from game import Game
from ui import Ui

class GameTest(unittest.TestCase):
    def setUp(self):
        user_interface = Ui()
        self.game = Game(user_interface)

    def test_start(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        user_interface = Ui()
        self.game = Game(user_interface)
        self.game.start()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual('Welcome to the Python TicTacToe\n\n           1  |  2  |  3\n         -----------------\n           4  |  5  |  6\n         -----------------\n           7  |  8  |  9\n        \n', output)

if __name__ == '__main__':
    unittest.main()
