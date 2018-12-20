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

    def test_horizontal_win_when_first_row_is_all_x(self):
        self.board.insert_value(1, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(3, 'X')
        self.board.insert_value(4, 'O')
        self.board.insert_value(2, 'X')
        self.assertEqual(True, self.game.horizontal_win(self.board))

    def test_horizontal_win_when_second_row_is_all_o(self):
        self.board.insert_value(1, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(3, 'X')
        self.board.insert_value(4, 'O')
        self.board.insert_value(7, 'X')
        self.board.insert_value(6, 'O')
        self.assertEqual(True, self.game.horizontal_win(self.board))

    def test_horizontal_win_when_third_row_is_all_x(self):
        self.board.insert_value(7, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(9, 'X')
        self.board.insert_value(4, 'O')
        self.board.insert_value(8, 'X')
        self.board.insert_value(2, 'O')
        self.assertEqual(True, self.game.horizontal_win(self.board))

    def test_vertical_win_when_first_column_is_all_x(self):
        self.board.insert_value(1, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(4, 'X')
        self.board.insert_value(3, 'O')
        self.board.insert_value(7, 'X')
        self.assertEqual(True, self.game.vertical_win(self.board))

    def test_vertical_win_when_second_column_is_all_o(self):
        self.board.insert_value(1, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(3, 'X')
        self.board.insert_value(2, 'O')
        self.board.insert_value(7, 'X')
        self.board.insert_value(8, 'O')
        self.assertEqual(True, self.game.vertical_win(self.board))

    def test_vertical_win_when_third_column_is_all_x(self):
        self.board.insert_value(3, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(9, 'X')
        self.board.insert_value(4, 'O')
        self.board.insert_value(6, 'X')
        self.assertEqual(True, self.game.vertical_win(self.board))

    def test_diagonal_win_when_first_diagonal_is_all_x(self):
        self.board.insert_value(1, 'X')
        self.board.insert_value(2, 'O')
        self.board.insert_value(9, 'X')
        self.board.insert_value(4, 'O')
        self.board.insert_value(5, 'X')
        self.assertEqual(True, self.game.diagonal_win(self.board))

    def test_diagonal_win_when_second_diagonal_is_all_o(self):
        self.board.insert_value(1, 'X')
        self.board.insert_value(3, 'O')
        self.board.insert_value(9, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(2, 'X')
        self.board.insert_value(7, 'O')
        self.assertEqual(True, self.game.diagonal_win(self.board))

    def test_win_when_horizontal_row_is_all_x(self):
        self.board.insert_value(7, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(9, 'X')
        self.board.insert_value(4, 'O')
        self.board.insert_value(8, 'X')
        self.board.insert_value(2, 'O')
        self.assertEqual(True, self.game.win(self.board))

    def test_win_when_vertical_column_is_all_x(self):
        self.board.insert_value(1, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(4, 'X')
        self.board.insert_value(3, 'O')
        self.board.insert_value(7, 'X')
        self.assertEqual(True, self.game.win(self.board))

    def test_win_when_second_diagonal_is_all_o(self):
        self.board.insert_value(1, 'X')
        self.board.insert_value(3, 'O')
        self.board.insert_value(9, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(2, 'X')
        self.board.insert_value(7, 'O')
        self.assertEqual(True, self.game.win(self.board))

    def test_win_when_board_is_empty(self):
        self.assertEqual(None, self.game.win(self.board))

    def test_win_when_board_is_not_empty_but_no_winning_scenario_reached(self):
        self.board.insert_value(1, 'X')
        self.board.insert_value(3, 'O')
        self.board.insert_value(9, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(2, 'X')
        self.board.insert_value(6, 'O')
        self.assertEqual(None, self.game.win(self.board))

    def test_win_when_board_is_tie(self):
        self.board.insert_value(1, 'X')
        self.board.insert_value(2, 'O')
        self.board.insert_value(3, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(4, 'X')
        self.board.insert_value(6, 'O')
        self.board.insert_value(8, 'X')
        self.board.insert_value(7, 'O')
        self.board.insert_value(9, 'X')
        self.assertEqual(None, self.game.win(self.board))

if __name__ == '__main__':
    unittest.main()
