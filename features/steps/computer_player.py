import io
import sys
from board import Board
from players.player_factory import PlayerFactory

@given('human player selects "{marker}" as their symbol')
def human_selects_o(context, marker):
    context.player_factory = PlayerFactory()
    user_input = io.StringIO(marker)
    sys.stdin = user_input
    marker1 = context.user_interface.choose_marker()
    sys.stdin = sys.__stdin__
    context.player1 = context.player_factory.create_player('human', marker1)
    marker2 = context.player1.define_marker(marker1)
    context.player2 = context.player_factory.create_player('computer', marker2)

@when('computer makes a move')
def computer_makes_first_move(context):
    context.board = Board()
    marker = context.player2.marker
    spot = context.player2.choose_move(context.board)
    context.player2.move(context.board, spot, marker)

@then('computer marker X is placed on the board randomly for the first move')
def board_with_computer_marker_is_printed(context):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board(context.board)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert 'X' in output
