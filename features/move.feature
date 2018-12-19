Feature: player's move
    As a player,
    I want to be able to place a move on the board,
    So that I can play the game

    Background: game starts
        Given new Game
        When game starts

    Scenario: first move
        Given empty board
        When first player makes move
        Then players marker X is placed on the board.

    Scenario: second move
        Given non-empty board
        When second player makes move
        Then players marker O is placed on the board.

