# Created by ALEX at 10/06/2021
Feature: OrangeHrm LoginSearch

  Background: Common Steps
    Given I launch  browser
    When  I open application
    And   Enter valid username and password
    And   click on login


  Scenario: Login To Hrm App
    Then  user must login to the Dashboard page

  Scenario: Search User
    When  I navigate to search page
    Then  Search page should display results

  Scenario: Advanced Search
    When  I navigate to advanced search page
    Then  Advanced search page should display results
