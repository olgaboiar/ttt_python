import io
import sys

@then('new game board is printed')
def print_board(context):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output == '\n          1 | 2 | 3\n         -----------\n          4 | 5 | 6\n         -----------\n          7 | 8 | 9\n        \n'
