Feature: printing game board
As a player,
I want to see an empty board in the beginning of the game,
So that I know the game is ready to be played.

  Scenario: print game board when starting the game
     Given new Game starts
      When after the welcome message
      Then new game board is printed
