Feature: Basic execution

  Scenario: INFO messages are logged
    Given a Lambda handler exists
    And the logger "myapp" will INFO log the message "abc"
    When the Lambda is executed
    Then the logs contain "abc"
    And the Lambda execution succeeded

  Scenario: DEBUG messages are not logged
    Given a Lambda handler exists
    And the logger "myapp" will DEBUG log the message "abc"
    And the random seed is "1"
    When the Lambda is executed
    Then the logs do not contain "abc"
    And the Lambda execution succeeded

  Scenario: DEBUG messages are sometimes printed
    Given a Lambda handler exists with sample rate of "100"
    And the logger "myapp" will DEBUG log the message "abc"
    And the random seed is "1"
    When the Lambda is executed
    Then the logs contain "abc"
    And the Lambda execution succeeded
