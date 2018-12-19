import unittest
from game import Game
from ui import Ui

class GameTest(unittest.TestCase):
    def setUp(self):
        user_interface = Ui()
        self.game = Game(user_interface)

    def test_start(self):
        pass

if __name__ == '__main__':
    unittest.main()
