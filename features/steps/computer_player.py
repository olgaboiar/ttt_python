import io
import sys
from board import Board
from player_factory import PlayerFactory

@given('human player selects "X" as their symbol')
def human_selects_x(context):
    context.player_factory = PlayerFactory()
    user_input = io.StringIO('x')
    sys.stdin = user_input
    marker1 = context.user_interface.choose_marker()
    sys.stdin = sys.__stdin__
    context.player1 = context.player_factory.create_player('human', marker1)
    marker2 = context.player1.define_marker(marker1)
    context.player2 = context.player_factory.create_player('computer', marker2)

@when('human player makes move at "5"')
def first_player_moves_to_five(context):
    context.board = Board()
    context.board.insert_value(5, 'X')

@then('computer marker O is placed on the board randomly for the next move')
def board_printed_with_o_marker_in_some_spot(context):
    marker = context.player2.marker
    spot = context.player2.choose_move(context.board)
    context.player2.move(context.board, spot, marker)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board(context.board)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert 'O' in output

@given('human player selects "O" as their symbol')
def human_selects_o(context):
    context.player_factory = PlayerFactory()
    user_input = io.StringIO('o')
    sys.stdin = user_input
    marker1 = context.user_interface.choose_marker()
    sys.stdin = sys.__stdin__
    context.player1 = context.player_factory.create_player('human', marker1)
    marker2 = context.player1.define_marker(marker1)
    context.player2 = context.player_factory.create_player('computer', marker2)

@when('new game board is printed')
def print_board(context):
    context.board = Board()

@then('computer marker X is placed on the board randomly for the first move')
def computer_makes_first_move(context):
    marker = context.player2.marker
    spot = context.player2.choose_move(context.board)
    context.player2.move(context.board, spot, marker)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board(context.board)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert 'X' in output
