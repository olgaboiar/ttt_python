Feature: showing welcoming message
  As a player,
  I want to see a welcome message when I start the game,
  So that I know I started the game

  Scenario: show welcoming message
     Given new Game
      When game starts
      Then welcoming message is shown