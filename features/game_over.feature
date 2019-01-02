Feature: game over
    As a player,
    I want to see a winning message when the game is over,
    So that I know the game is over

    Scenario: tie game over
        Given new Game
        And the board is one move away from a tie
        When player places the final move and tie is reached
        Then game over message is printed

    Scenario: horizontal win game over
        Given new Game
        And the board is one move away from horizontal win
        When player places the final move and horizontal win is reached
        Then game over message is printed

    Scenario: vertical win game over
        Given new Game
        And the board is one move away from vertical win
        When player places the final move and vertical win is reached
        Then game over message is printed

    @wip
    Scenario: diagonal win game over
        Given new Game
        And the board is one move away from a diagonal win
        When player places the final move and diagonal win is reached
        Then game over message is printed

