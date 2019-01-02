import io
import sys
from board import Board

@given('the board is {raw_spots}')
def special_board_state(context, raw_spots):
    context.board = Board()
    context.board.spots = [int(spot) if spot.isdigit() else spot for spot in raw_spots]

@when('human player makes a move on {spot}')
def human_moves_on_spot(context, spot):
    context.board.insert_value(spot, 'X')

@then('computer makes move on {spot}')
def board_with_computer_marker_on_certain_spot_is_printed(context, spot):
    marker = context.player2.marker
    best_move = context.player2.choose_move(context.board)
    context.player2.move(context.board, best_move, marker)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board(context.board)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert spot not in output