import io
import sys

@then('player1 is asked to choose X or O as a symbol')
def choose_marker(context):
    captured_output = io.StringIO()
    user_input = io.StringIO('x')
    sys.stdout = captured_output
    sys.stdin = user_input
    context.game.create_players()
    sys.stdout = sys.__stdout__
    sys.stdin = sys.__stdin__
    output = captured_output.getvalue()
    assert output == 'Choose the symbol you want to play with: X or O. Enter x or o:\n'
