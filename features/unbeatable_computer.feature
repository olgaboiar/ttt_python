Feature: ubeatable computer
  As a player,
  I want to play against an unbeatable computer player
  So that it is even more fun

  Scenario: computer wins
     Given new Game
       And the board is [X, O, X, 4, O, 6, 7, 8, 9]
       And human player selects "X" as their symbol
      When human player makes a move on 7
      Then computer wins by making move on 8

    Scenario: computer prevents human from winning
     Given new Game
       And the board is [X, O, 3, 4, 5, 6, 7, 8, 9]
       And human player selects "X" as their symbol
      When human player makes a move on 9
      Then computer makes move on 5