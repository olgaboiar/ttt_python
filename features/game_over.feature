Feature: game over
    As a player,
    I want to see a winning message when the game is over,
    So that I know the game is over

    Scenario: tie game over
        Given new Game
        When players move until all cells are taken but no win reached
        Then game over message is printed for tie

    Scenario: horizontal win game over
        Given new Game
        When players move until horizontal win is reached
        Then game over message is printed for horizontal win

    Scenario: vertical win game over
        Given new Game
        When players move until vertical win is reached
        Then game over message is printed for vertical win

    Scenario: diagonal win game over
        Given new Game
        When players move until diagonal win is reached
        Then game over message is printed for diagonal win

