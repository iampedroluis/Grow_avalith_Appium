@feature
Feature: try demo apk
  "As a user I want to test the mobile app"
  @testcase1
  Scenario: enter some value button
    Given the user is in the application
    When the user clicks the enter some value button
    And write the first value
    And click submit Button
    Then the first value is displayed

  @testcase2
    Scenario: contact us form button
      Given being the user in the application
      When the user clicks on the button contact us from
      And  complete the requested data
      And click submit
      Then the loaded data is displayed

  @testcase3
    Scenario: Scrollview button
    Given the user is in the app
    When click on the Scrollview button
    And  Scrolls down
    And   click on option number 09
    And  click yes
    Then the home window is displayed

  @testcase4
    Scenario:  TAB ACTIVITY button
    Given the user entered the app
    When click on the Tab Activity button
    And scrolls horizontally
    And click on the different boxes
    Then you can browse the different sections

  @testcase5
    Scenario: Zoom button
    Given login in app
    When click on the zoom button
    Then The logo is displayed by zooming

  @testcase6
    Scenario: Login button
    Given being in the application
    When click on the login button
    And complete the email and passw information
    And click on login
    And write admin in the required field
    And click on the submit button
    Then you see the word Admin on the screen

  @testcase7
    Scenario: Crash button
    Given mobile demo application
    When the user scrolls to the bottom
    And click on the crash button
    Then exit the application

  @testcasefail
    Scenario: fail the test
      Given user a mobile app
    When user clicks login button
    And do not put the credentials
    And clicks login without credentials
    Then lets you log in
