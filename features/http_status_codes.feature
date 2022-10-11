Feature: HTTP status codes

  Scenario: When an HTTP Lambda function returns a >=400 status code then both the INFO and DEBUG logs should be logged
    Given a Lambda handler exists that returns "HTTP" responses
    And the logger "myapp" will INFO log the message "abc"
    And the logger "myapp" will DEBUG log the message "def"
    And the Lambda handler will return:
      """
      {
          "statusCode": 401
      }
      """
    When the Lambda is executed
    Then the Lambda execution succeeded
    And the logs contain "abc"
    And the logs contain "def"

  Scenario: When an HTTP Lambda function returns an invalid response then both the INFO and DEBUG logs should be logged
    Given a Lambda handler exists that returns "HTTP" responses
    And the random seed is "1"
    And the logger "myapp" will INFO log the message "abc"
    And the logger "myapp" will DEBUG log the message "def"
    When the Lambda is executed
    Then the Lambda execution succeeded
    And the logs contain "abc"
    And the logs contain "def"

  Scenario: When an HTTP Lambda function returns a 200 status code then only INFO messages should be logged
    Given a Lambda handler exists that returns "HTTP" responses
    And the random seed is "1"
    And the logger "myapp" will INFO log the message "abc"
    And the logger "myapp" will DEBUG log the message "def"
    And the Lambda handler will return:
      """
      {
          "statusCode": 200
      }
      """
    When the Lambda is executed
    Then the Lambda execution succeeded
    And the logs contain "abc"
    And the logs do not contain "def"
