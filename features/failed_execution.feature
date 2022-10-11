Feature: Failed exceptions

  Scenario: When a Lambda function fails, both the INFO and DEBUG logs should be logged
    Given a Lambda handler exists
    And the the Lambda will fail
    And the logger "myapp" will INFO log the message "abc"
    And the logger "myapp" will DEBUG log the message "def"
    When the Lambda is executed
    Then the Lambda execution failed
    And the logs contain "abc"
    And the logs contain "def"
