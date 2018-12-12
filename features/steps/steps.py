from behave import *
from tictactoe import *
import io
import sys

@given('new Game')
def step_impl(context):
    context.game = Game()

@when('game starts')
def step_impl(context):
    context.game.start()

@then('welcoming message is shown')
def step_impl(context):
  pass
  capturedOutput = io.StringIO()
  sys.stdout = capturedOutput
  context.game.start()                                 
  sys.stdout = sys.__stdout__
  output = capturedOutput.getvalue()
  assert ('hi\n' == output)