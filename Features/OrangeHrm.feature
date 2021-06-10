Feature: OrangeHrm Logo

  Scenario: Logo Presence on OrangeHrm HomePage
    Given launch chrome browser
    When  open orangehrm homepage
    Then  verify that logo present on the page
    And   close browser