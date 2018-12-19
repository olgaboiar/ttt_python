import unittest
from player import Player

class GameTest(unittest.TestCase):
    def setUp(self):
        self.player = Player('X')

    def test_define_second_marker_automatically_when_the_first_one_is_O(self):
        symbol = self.player.define_marker('O')
        self.assertEqual(symbol, 'X')
        
    def test_define_second_marker_automatically_when_the_first_one_is_X(self):
        symbol = self.player.define_marker('X')
        self.assertEqual(symbol, 'O')

if __name__ == '__main__':
    unittest.main()
