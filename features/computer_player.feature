Feature: showing welcoming message
  As a player
  I want to play against a computer player
  So that it is more fun

    Scenario: computer moves first
        Given new Game
        And human player selects "O" as their symbol
        When computer makes a move
        Then computer marker X is placed on the board randomly for the first move