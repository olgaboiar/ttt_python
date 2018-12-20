Feature: player's move
    As a player,
    I want to be able to place a move on the board,
    So that I can play the game

    Scenario: first move
        Given new Game
        And first player selects "X" as their symbol
        And new game board is printed
        When first player makes move at "5"
        Then players marker X is placed on the board

    Scenario: second move
        Given new Game
        And first player selects "X" as their symbol
        And new game board is printed
        And first player makes move at "5"
        When second player makes move at "2"
        Then players marker O is placed on the board
