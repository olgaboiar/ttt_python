import unittest
from input_validator import InputValidator

class GameTest(unittest.TestCase):
    def setUp(self):
        self.input_validator = InputValidator()

    def test_valid_marker_when_input_is_a_valid_character(self):
        symbol = self.input_validator.valid_marker('O')
        self.assertEqual(symbol, True)

        symbol = self.input_validator.valid_marker('X')
        self.assertEqual(symbol, True)

    def test_valid_marker_when_input_is_an_invalid_character(self):
        symbol = self.input_validator.valid_marker('D')
        self.assertEqual(symbol, None)

    def test_valid_marker_when_input_is_a_lowercase_character(self):
        symbol = self.input_validator.valid_marker('x')
        self.assertEqual(symbol, None)

    def test_valid_marker_when_input_is_a_number(self):
        symbol = self.input_validator.valid_marker('1')
        self.assertEqual(symbol, None)

    def test_valid_marker_when_input_is_a_special_character(self):
        symbol = self.input_validator.valid_marker('-')
        self.assertEqual(symbol, None)

    def test_valid_move_when_input_is_a_valid_possible_move(self):
        move = self.input_validator.valid_move('2')
        self.assertEqual(move, True)

    def test_valid_move_when_input_is_a_lowercase_character(self):
        with self.assertRaises(ValueError): self.input_validator.valid_move('x')

    def test_valid_move_when_input_is_an_invalid_number(self):
        move = self.input_validator.valid_move('100')
        self.assertEqual(move, None)

    def test_valid_move_when_input_is_a_special_character(self):
        with self.assertRaises(ValueError): self.input_validator.valid_move('-')


if __name__ == '__main__':
    unittest.main()
