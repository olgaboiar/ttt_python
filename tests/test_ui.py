import unittest
from unittest import mock
import io
import sys
from ui import Ui

class UiTest(unittest.TestCase):
    def setUp(self):
        self.user_interface = Ui()

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
        self.user_interface.print_board()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual('\n          1 | 2 | 3\n         -----------\n          4 | 5 | 6\n         -----------\n          7 | 8 | 9\n        \n', output)

    def test_get_user_input(self):
        self.user_interface.get_input = mock.MagicMock(side_effect = ['foo', 'x', '3'])
        user_input = self.user_interface.get_input("text")
        self.assertEqual(user_input, 'foo')
        user_input = self.user_interface.get_input("text")
        self.assertEqual(user_input, 'x')
        user_input = self.user_interface.get_input("text")
        self.assertNotEqual(user_input, '2')

    def test_choose_marker_for_the_first_human_player(self):
        self.user_interface.get_input = mock.MagicMock(side_effect = ['X', 'x', 'o', 'O', 'd', '-', '1', 'o'])
        symbol = self.user_interface.choose_marker()
        self.assertEqual(symbol, 'X')
        symbol = self.user_interface.choose_marker()
        self.assertEqual(symbol, 'X')
        symbol = self.user_interface.choose_marker()
        self.assertEqual(symbol, 'O')
        symbol = self.user_interface.choose_marker()
        self.assertEqual(symbol, 'O')
        symbol = self.user_interface.choose_marker()
        self.assertEqual(symbol, 'O')

if __name__ == '__main__':
    unittest.main()
