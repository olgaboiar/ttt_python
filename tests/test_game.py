import unittest
import io
import sys
from game import Game

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_start(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.game = Game()
        self.game.start()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual('hi\n', output)
