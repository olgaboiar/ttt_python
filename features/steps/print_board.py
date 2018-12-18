import io
import sys
from ui import Ui

@given('new Game starts')
def game_start(context):
    context.user_interface = Ui()
    # context.game = Game(context.user_interface)

@when('after the welcome message')
def start_game(context):
    context.user_interface.greet()

@then('new game board is printed')
def print_board(context):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output == '\n          1 | 2 | 3\n         -----------\n          4 | 5 | 6\n         -----------\n          7 | 8 | 9\n        \n'
