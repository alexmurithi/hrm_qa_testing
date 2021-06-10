# Created by ALEX at 09/06/2021
Feature: OrangeHrm Login

  Scenario:  Login to OrangeHrm with valid parameters
    Given I launch chrome browser
    When  I open OrangeHrm homepage
    And   Enter username "admin" and password "admin123"
    And   click login button
    Then  User must successfully login to the Dashboard panel

  Scenario Outline: Login to OrangeHrm with Multiple parameters
    Given I launch chrome browser
    When  I open OrangeHrm homepage
    And   Enter username "<username>" and password "<password>"
    And   click login button
    Then  User must successfully login to the Dashboard panel

    Examples:
      | username | | password |
      | admin    | | admin123 |
      | admin123 | | admin    |

