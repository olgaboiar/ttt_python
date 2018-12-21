import io
import sys
from board import Board

@given('the board is one move away from a tie')
def game_almost_tie(context):
    context.board = Board()
    context.board.spots = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 9]

@when('player places the final move and tie is reached')
def game_final_move_tie(context):
    context.board.insert_value(9, 'X')

@then('game over message is printed')
def game_over(context):
    user_input = io.StringIO('x')
    sys.stdin = user_input
    captured_output = io.StringIO()
    sys.stdout = captured_output
    context.game.play(context.board)
    sys.stdout = sys.__stdout__
    sys.stdin = sys.__stdin__
    output = captured_output.getvalue()
    assert 'Game over!' in output

    # Scenario: diagonal win game over
    #     Given new Game
    #     And the board is one move away from a diagonal win
    #     When player places the final move and diagonal win is reached
    #     Then game over message is printed

@given('the board is one move away from horizontal win')
def game_horizontal_win(context):
    context.board = Board()
    context.board.spots = ['X', 2, 'X', 'O', 5, 'O', 'X', 8, 9]

@when('player places the final move and horizontal win is reached')
def game_final_move_horizontal_win(context):
    context.board.insert_value(5, 'O')

@given('the board is one move away from vertical win')
def game_vertical_win(context):
    context.board = Board()
    context.board.spots = [1, 2, 'X', 'O', 'O', 'X', 7, 8, 9]

@when('player places the final move and vertical win is reached')
def game_final_move_vertical_win(context):
    context.board.insert_value(9, 'X')

@given('the board is one move away from a diagonal win')
def game_diagonal_win(context):
    context.board = Board()
    context.board.spots = ['X', 'O', 3, 'O', 'X', 6, 7, 8, 9]

@when('player places the final move and diagonal win is reached')
def game_final_move_diagonal_win(context):
    context.board.insert_value(9, 'X')