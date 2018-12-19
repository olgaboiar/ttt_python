from board import Board
from player import Player

@given('empty board')
def create_board(context):
    context.board = Board()

@when('first player makes move')
def player1_move(context):
    context.player = Player('X')
    context.player.move(context.board, 3, 'X')


@then('players marker X is placed on the board')
def get_x_marker_in_a_certain_spot(context):
    value = context.board.get_value(2)
    assert value == 'X'


@given('non-empty board')
def get_board(context):
    context.board = Board()
    context.board.insert_value(1, 'X')


@when('second player makes move')
def player2_move(context):
    context.player = Player('O')
    context.player.move(context.board, 5, 'O')

@then('players marker O is placed on the board')
def get_o_marker_in_a_certain_spot(context):
    value = context.board.get_value(4)
    assert value == 'O'
