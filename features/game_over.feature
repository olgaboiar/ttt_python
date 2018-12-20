Feature: game over
    As a player,
    I want to see a winning message when the game is over,
    So that I know the game is over

    Scenario: tie game over
        Given new Game
        And first player selects "X" as their symbol
        And new game board is printed
        And players move until all cells are taken but no win reached
        Then game over tie message is printed

    Scenario: horizontal win game over
        Given new Game
        And first player selects "X" as their symbol
        And new game board is printed
        And players move until horizontal win is reached
        Then game over tie message is printed

    Scenario: vertical win game over
        Given new Game
        And first player selects "X" as their symbol
        And new game board is printed
        And players move until vertical win is reached
        Then game over tie message is printed

    Scenario: diagonal win game over
        Given new Game
        And first player selects "X" as their symbol
        And new game board is printed
        And players move until diagonal win is reached
        Then game over tie message is printed

