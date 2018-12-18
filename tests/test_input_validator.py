import unittest
from input_validator import InputValidator

class GameTest(unittest.TestCase):
    def setUp(self):
        self.input_validator = InputValidator()

    def test_valid_marker(self):
        symbol = self.input_validator.valid_marker('O')
        self.assertEqual(symbol, True)
        symbol = self.input_validator.valid_marker('X')
        self.assertEqual(symbol, True)
        symbol = self.input_validator.valid_marker('D')
        self.assertEqual(symbol, None)
        symbol = self.input_validator.valid_marker('x')
        self.assertEqual(symbol, None)

if __name__ == '__main__':
    unittest.main()
