import unittest
# from . import player
from players.player import Player
from board import Board

class GameTest(unittest.TestCase):
    def setUp(self):
        self.player = Player('X')
        self.board = Board()

    def test_define_second_marker_automatically_when_the_first_one_is_o(self):
        symbol = self.player.define_marker('O')
        self.assertEqual(symbol, 'X')

    def test_define_second_marker_automatically_when_the_first_one_is_x(self):
        symbol = self.player.define_marker('X')
        self.assertEqual(symbol, 'O')

    def test_move_when_user_entered_valid_move_option(self):
        self.player.move(self.board, 4, 'O')
        board_spot_value = self.board.get_value(3)
        self.assertEqual(board_spot_value, 'O')


if __name__ == '__main__':
    unittest.main()
