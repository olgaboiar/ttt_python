import io
import sys
from board import Board

@given('the board is {board}')
def special_board_state(context, board):
    context.board = Board()
    context.board.spots = [int(n) if n.isdigit() else n for n in board]

@when('human player makes a move on {spot}')
def human_moves_on_seven(context, spot):
    context.board.insert_value(spot, 'X')

@then('computer makes move on {cell}')
def board_with_computer_marker_on_eight_is_printed(context, cell):
    marker = context.player2.marker
    spot = context.player2.choose_move(context.board)
    context.player2.move(context.board, spot, marker)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.user_interface.print_board(context.board)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()
    assert cell not in output