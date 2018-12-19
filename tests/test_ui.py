import unittest
from unittest import mock
import io
import sys
from ui import Ui
from board import Board

class UiTest(unittest.TestCase):
    def setUp(self):
        self.user_interface = Ui()
        self.board = Board()

    def test_greeting_message(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.user_interface.greet()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual('Welcome to the Python TicTacToe\n', output)

    def test_printing_board_at_the_start_of_the_game(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.user_interface.print_board(self.board)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual('\n          1 | 2 | 3\n         -----------\n          4 | 5 | 6\n         -----------\n          7 | 8 | 9\n        \n', output)

    def test_printing_board_whrn_board_is_not_empty(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.board.insert_value(1, 'X')
        self.user_interface.print_board(self.board)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual('\n          1 | X | 3\n         -----------\n          4 | 5 | 6\n         -----------\n          7 | 8 | 9\n        \n', output)

    def test_get_user_input(self):
        self.user_interface.get_input = mock.MagicMock(side_effect = ['foo', 'x', '3'])
        user_input = self.user_interface.get_input("text")
        self.assertEqual(user_input, 'foo')
        user_input = self.user_interface.get_input("text")
        self.assertEqual(user_input, 'x')
        user_input = self.user_interface.get_input("text")
        self.assertNotEqual(user_input, '2')

    def test_choose_marker_will_ask_again_until_input_is_valid(self):
        self.user_interface.get_input = mock.MagicMock(side_effect = ['-', 'X'])
        symbol = self.user_interface.choose_marker()
        self.assertEqual(symbol, 'X')

    def test_choose_marker_will_upcase_input(self):
        self.user_interface.get_input = mock.MagicMock(side_effect = ['x'])
        symbol = self.user_interface.choose_marker()
        self.assertEqual(symbol, 'X')

    def test_choose_move_will_ask_again_until_input_is_valid(self):
        self.user_interface.get_input = mock.MagicMock(side_effect = ['0', '10000', '5'])
        move = self.user_interface.choose_move()
        self.assertEqual(move, '5')


if __name__ == '__main__':
    unittest.main()
