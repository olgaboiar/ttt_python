import io
import sys
from unittest import mock
from game import Game
from ui import Ui

@given('new Game started')
def create_game(context):
    context.user_interface = Ui()
    # context.game = Game(context.user_interface)

@when('When after the welcome message')
def start_game(context):
    # context.game.start()
    pass

@then('player1 is asked to choose X or O as a symbol')
def choose_marker(context):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.choose_marker()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output == 'Choose the symbol you want to play with: X or O. Enter x or o:\n'
