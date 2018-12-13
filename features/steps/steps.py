import io
import sys
from game import Game

@given('new Game')
def create_game(context):
    context.game = Game()

@when('game starts')
def start_game(context):
    context.game.start()

@then('welcoming message is shown')
def print_message(context):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.game.start()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output == 'hi\n'
