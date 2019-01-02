Feature: unbeatable computer
  As a player,
  I want to play against an unbeatable computer player
  So that it is even more fun

  Scenario: computer wins
     Given new Game
       And the board is XOX4O6789
       And human player selects "X" as their symbol
      When human player makes a move on 7
      Then computer makes move on 8

    Scenario: computer prevents human from winning
     Given new Game
       And the board is XO3456789
       And human player selects "X" as their symbol
      When human player makes a move on 9
      Then computer makes move on 5
