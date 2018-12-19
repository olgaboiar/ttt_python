Feature: choosing the symbol
As a player,
I want to choose X or O,
So that I can see my choice on the board

  Scenario: ask the first player to choose symbol
     Given new Game
      When game starts
      Then player1 is asked to choose X or O as a symbol
