import io
import sys
from game import Game
from ui import Ui

@given('new Game')
def create_game(context):
    context.user_interface = Ui()
    context.game = Game(context.user_interface)

@when('game starts')
def start_game(context):
    context.game.start()

@then('welcoming message is shown')
def print_message(context):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.greet()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output == 'Welcome to the Python TicTacToe\n'
