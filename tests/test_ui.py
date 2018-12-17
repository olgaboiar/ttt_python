import unittest
import io
import sys
from ui import Ui

class GameTest(unittest.TestCase):
    def setUp(self):
        self.user_interface = Ui()

    def test_start(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        self.user_interface.greet()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertEqual('Welcome to the Python TicTacToe\n', output)

    def test_print_board(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        self.user_interface.print_board()

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertEqual('\n          1 | 2 | 3\n         -----------\n          4 | 5 | 6\n         -----------\n          7 | 8 | 9\n        \n', output)

if __name__ == '__main__':
    unittest.main()
