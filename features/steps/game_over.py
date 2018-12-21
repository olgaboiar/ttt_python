import io
import sys
from board import Board


@when('players move until all cells are taken but no win reached')
def game_tie(context):
    context.board = Board()
    context.board.insert_value(1, 'X')
    context.board.insert_value(2, 'O')
    context.board.insert_value(3, 'X')
    context.board.insert_value(5, 'O')
    context.board.insert_value(4, 'X')
    context.board.insert_value(6, 'O')
    context.board.insert_value(8, 'X')
    context.board.insert_value(7, 'O')
    context.board.insert_value(9, 'X')
    

@then('game over message is printed for tie')
def game_over_for_tie(context):
    user_input = io.StringIO('x')
    sys.stdin = user_input
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.game.play(context.board)
    sys.stdout = sys.__stdout__
    sys.stdin = sys.__stdin__
    output = captured_output.getvalue()
    assert output == 'Choose the symbol you want to play with: X or O. Enter x or o:\n\n          X | O | X\n         -----------\n          X | O | O\n         -----------\n          O | X | X\n        \nGame over!\n'

@when('players move until horizontal win is reached')
def game_horizontal_win(context):
    context.board = Board()
    context.board.insert_value(1, 'X')
    context.board.insert_value(5, 'O')
    context.board.insert_value(3, 'X')
    context.board.insert_value(4, 'O')
    context.board.insert_value(2, 'X')
    

@then('game over message is printed for horizontal win')
def game_over_for_horizontal_win(context):
    user_input = io.StringIO('x')
    sys.stdin = user_input
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.game.play(context.board)
    sys.stdout = sys.__stdout__
    sys.stdin = sys.__stdin__
    output = captured_output.getvalue()
    assert output == 'Choose the symbol you want to play with: X or O. Enter x or o:\n\n          X | X | X\n         -----------\n          O | O | 6\n         -----------\n          7 | 8 | 9\n        \nGame over!\n'

@when('players move until vertical win is reached')
def game_vertical_win(context):
    context.board = Board()
    context.board.insert_value(1, 'X')
    context.board.insert_value(2, 'O')
    context.board.insert_value(4, 'X')
    context.board.insert_value(5, 'O')
    context.board.insert_value(7, 'X')

@then('game over message is printed for vertical win')
def game_over_for_vertical_win(context):
    user_input = io.StringIO('x')
    sys.stdin = user_input
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.game.play(context.board)
    sys.stdout = sys.__stdout__
    sys.stdin = sys.__stdin__
    output = captured_output.getvalue()
    assert output == 'Choose the symbol you want to play with: X or O. Enter x or o:\n\n          X | O | 3\n         -----------\n          X | O | 6\n         -----------\n          X | 8 | 9\n        \nGame over!\n'

@when('players move until diagonal win is reached')
def game_diagonal_win(context):
    context.board = Board()
    context.board.insert_value(1, 'X')
    context.board.insert_value(2, 'O')
    context.board.insert_value(5, 'X')
    context.board.insert_value(7, 'O')
    context.board.insert_value(9, 'X')

@then('game over message is printed for diagonal win')
def game_over_for_diagonal_win(context):
    user_input = io.StringIO('x')
    sys.stdin = user_input
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.game.play(context.board)
    sys.stdout = sys.__stdout__
    sys.stdin = sys.__stdin__
    output = captured_output.getvalue()
    assert output == 'Choose the symbol you want to play with: X or O. Enter x or o:\n\n          X | O | 3\n         -----------\n          4 | X | 6\n         -----------\n          O | 8 | X\n        \nGame over!\n'

