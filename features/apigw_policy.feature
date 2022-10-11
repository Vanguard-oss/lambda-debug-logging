

Feature: API Gateway policies

  Scenario: When an API Gateway authorizer denies access then both the INFO and DEBUG logs should be logged
    Given a Lambda handler exists that returns "APIGW_AUTHPOLICY" responses
    And the logger "myapp" will INFO log the message "abc"
    And the logger "myapp" will DEBUG log the message "def"
    And the Lambda handler will return:
      """
      {
          "policyDocument": {
            "Statement": [
              {
                "Effect": "Deny"
              }
            ]
          }
      }
      """
    When the Lambda is executed
    Then the Lambda execution succeeded
    And the logs contain "abc"
    And the logs contain "def"

  Scenario: When an API Gateway authorizer allows access then only the INFO logs should be logged
    Given a Lambda handler exists that returns "APIGW_AUTHPOLICY" responses
    And the logger "myapp" will INFO log the message "abc"
    And the logger "myapp" will DEBUG log the message "def"
    And the Lambda handler will return:
      """
      {
          "policyDocument": {
            "Statement": [
              {
                "Effect": "Allow"
              }
            ]
          }
      }
      """
    When the Lambda is executed
    Then the Lambda execution succeeded
    And the logs contain "abc"
    And the logs do not contain "def"
