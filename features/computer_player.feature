Feature: showing welcoming message
  As a player
  I want to play against a computer player
  So that it is more fun

    Scenario: human moves first
        Given new Game
        And human player selects "X" as their symbol
        And new game board is printed
        When human player makes move at "5"
        Then computer marker O is placed on the board randomly for the next move

    Scenario: computer moves first
        Given new Game
        And human player selects "O" as their symbol
        When new game board is printed
        Then computer marker X is placed on the board randomly for the first move