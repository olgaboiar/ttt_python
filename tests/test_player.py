import unittest
from player import Player

class GameTest(unittest.TestCase):
    def setUp(self):
        self.player = Player('X')

    def test_define_second_marker_automatically(self):
        symbol = self.player.define_marker('O')
        self.assertEqual(symbol, 'X')
        symbol = self.player.define_marker('X')
        self.assertEqual(symbol, 'O')

if __name__ == '__main__':
    unittest.main()
