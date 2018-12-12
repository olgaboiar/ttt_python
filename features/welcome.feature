Feature: showing welcoming message

  Scenario: show welcoming message
     Given new Game
      When game starts
      Then welcoming message is shown