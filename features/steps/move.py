# import io
# import sys
# from game import Game
# from ui import Ui

@given('empty board')
def create_board(context):
    pass
    # context.user_interface = Ui()
    # context.game = Game(context.user_interface)

@when('first player makes move')
def player1_move(context):
    pass
    # user_input = io.StringIO('x')
    # sys.stdin = user_input
    # context.game.start()
    # sys.stdin = sys.__stdin__

@then('players marker X is placed on the board')
def get_x_marker_in_a_certain_spot(context):
    pass
    # captured_output = io.StringIO()
    # sys.stdout = captured_output
    # context.user_interface.greet()
    # sys.stdout = sys.__stdout__
    # output = captured_output.getvalue()
    # assert output == 'Welcome to the Python TicTacToe\n'


@given('non-empty board')
def get_board(context):
    pass
    # context.user_interface = Ui()
    # context.game = Game(context.user_interface)

@when('second player makes move')
def player2_move(context):
    pass
    # user_input = io.StringIO('x')
    # sys.stdin = user_input
    # context.game.start()
    # sys.stdin = sys.__stdin__

@then('players marker O is placed on the board')
def get_o_marker_in_a_certain_spot(context):
    pass
    # Scenario: second move
    #     Given non-empty board
    #     When second player makes move
    #     Then players marker O is placed on the board.

