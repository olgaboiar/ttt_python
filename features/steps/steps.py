import io
import sys
# from behave import context
from behave import given, when, then
from tictactoe import Game

@given('new Game')
def step_impl(context):
    context.game = Game()

@when('game starts')
def step_impl(context):
    context.game.start()

@then('welcoming message is shown')
def step_impl(context):
    pass
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.game.start()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output == 'hi\n'
