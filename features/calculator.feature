# calculator.feature

Feature: Calculator

  Scenario: Addition
    Given I have entered 2 into the calculator
    And I have entered 3 into the calculator
    When I press the add button
    Then the result should be 5 on the screen
