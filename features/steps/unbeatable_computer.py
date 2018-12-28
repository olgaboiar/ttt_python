import io
import sys
from board import Board

@given('the board is [X, O, X, 4, O, 6, 7, 8, 9]')
def special_board_state(context):
    context.board = Board()
    context.board.spots = ['X', 'O', 'X', 4, 'O', 6, 7, 8, 9]

@when('human player makes a move on 7')
def human_moves_on_seven(context):
    context.board.insert_value(7, 'X')

@then('computer wins by making move on 8')
def board_with_computer_marker_on_eight_is_printed(context):
    marker = context.player2.marker
    spot = context.player2.choose_move(context.board)
    context.player2.move(context.board, spot, marker)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board(context.board)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert "8" not in output

@given('the board is [X, O, 3, 4, 5, 6, 7, 8, 9]')
def certain_board_state(context):
    context.board = Board()
    context.board.spots = ['X', 'O', 3, 4, 5, 6, 7, 8, 9]

@when('human player makes a move on 9')
def human_moves_on_nine(context):
    context.board.insert_value(9, 'X')

@then('computer makes move on 5')
def board_with_computer_marker_on_five_is_printed(context):
    marker = context.player2.marker
    spot = context.player2.choose_move(context.board)
    context.player2.move(context.board, spot, marker)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board(context.board)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert "5" not in output
