from input_validator import InputValidator

class Ui:
    def __init__(self):
        self.input_validator = InputValidator()

    def greet(self):
        print("Welcome to the Python TicTacToe")

    def print_board(self, board):
        current_board = board.all_spots()
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*current_board))

    def get_input(self, text):
        return input(text)

    def choose_marker(self):
        text = 'Choose the symbol you want to play with: X or O. Enter x or o:\n'
        symbol = None
        while not symbol:
            symbol = self.get_input(text).upper()
            if self.input_validator.valid_marker(symbol):
                return symbol
            else:
                symbol = None

    def choose_move(self):
        text = "Enter a number to make your move:\n"
        move = None
        while not move:
            move = self.get_input(text)
            if self.input_validator.valid_move(move):
                return move
            else:
                move = None
