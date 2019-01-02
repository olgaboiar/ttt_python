Feature: computer as a player
  As a player
  I want to play against a computer player
  So that it is more fun

    Scenario: computer moves first
        Given new Game
        And human player selects "O" as their symbol
        When computer makes a move
        Then computer marker X is placed on 9 to prevent human from winning