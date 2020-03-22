Feature: Test contact page

  Scenario: Test contact page
    Given I have open main page
    When I fill all fields
    And I click send button
    Then My request successfully send