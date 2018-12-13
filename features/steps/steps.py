"""These are the steps to test welcome feature"""
import io
import sys
# from behave import context
# from behave import given, when, then
from tictactoe import Game
# given = given
@given('new Game')
def create_game(context):
    """Creates new game."""
    context.game = Game()

@when('game starts')
def start_game(context):
    """Starts the game."""
    context.game.start()

@then('welcoming message is shown')
def print_message(context):
    """Checks if starting the game prints welcome message."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.game.start()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output == 'hi\n'
