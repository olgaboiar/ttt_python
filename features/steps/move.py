import io
import sys
from board import Board
from player import Player


@given('first player selects "X" as their symbol')
def game_starts(context):
    user_input = io.StringIO('x')
    sys.stdin = user_input
    marker1 = context.user_interface.choose_marker()
    sys.stdin = sys.__stdin__
    context.player1 = Player(marker1)
    marker2 = context.player1.define_marker(marker1)
    context.player2 = Player(marker2)

@given('new game board is printed')
def print_board(context):
    context.board = Board()
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board(context.board)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output == '\n          1 | 2 | 3\n         -----------\n          4 | 5 | 6\n         -----------\n          7 | 8 | 9\n        \n'

@when('first player makes move at "5"')
def player1_move(context):
    user_input = io.StringIO('5')
    sys.stdin = user_input
    move1 = context.user_interface.choose_move(context.board)
    sys.stdin = sys.__stdin__
    context.player1.move(context.board, move1, 'X')


@then('players marker X is placed on the board')
def board_printed_with_x_marker_in_a_certain_spot(context):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board(context.board)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output == '\n          1 | 2 | 3\n         -----------\n          4 | X | 6\n         -----------\n          7 | 8 | 9\n        \n'

@given('first player makes move at "5"')
def first_player_moves_to_five(context):
    user_input = io.StringIO('5')
    sys.stdin = user_input
    move1 = context.user_interface.choose_move(context.board)
    sys.stdin = sys.__stdin__
    context.player1.move(context.board, move1, 'X')


@when('second player makes move at "2"')
def second_player_moves_to_two(context):
    user_input = io.StringIO('2')
    sys.stdin = user_input
    move1 = context.user_interface.choose_move(context.board)
    sys.stdin = sys.__stdin__
    context.player2.move(context.board, move1, 'O')

@then('players marker O is placed on the board')
def board_printed_with_x_and_o_markers_in_a_certain_spots(context):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board(context.board)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert output == '\n          1 | O | 3\n         -----------\n          4 | X | 6\n         -----------\n          7 | 8 | 9\n        \n'
