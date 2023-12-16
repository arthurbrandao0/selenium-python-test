Feature: Exemplo de testes de interface

  Narrative:

  This is just an example to show a minimal structure using Python, Selenium and Behave
  The number of possible scenarios, positive and negative, were not considered

  Scenario Outline: Validate sum of 2 numbers
    Given that I access the website "https://www.lambdatest.com/selenium-playground/simple-form-demo"
    When I enter <first_number> in the first field
    And I enter <second_number> in the second field
    And click the "Get Sum" button
    Then the result will be <sum_total>
    Examples:
      | first_number | second_number | sum_total |
      | 1            | 2             | 3         |
      | 5            | 12            | 17        |
      | 10           | 15            | 25        |
      | 50           | 1             | 51        |
      | 38           | 12            | 50        |