Feature: ubeatable computer
  As a player,
  I want to play against an unbeatable computer player
  So that it is even more fun

  Scenario: show welcoming message
     Given new Game
      When one of the players is computer
      Then it is impossible to beat the computer