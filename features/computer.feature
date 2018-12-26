Feature: showing welcoming message
  As a player
  I want to play against a computer player
  So that it is more fun

  Scenario: show welcoming message
     Given new Game
      When game starts
      Then the second player is computer