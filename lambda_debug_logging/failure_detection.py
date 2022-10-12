def http_status_code_check(resp) -> bool:
    """Check a response for an HTTP response

    This function checks the response for an API Gateway or ALB response.  If the status code
    is >= 400 then the response is considered a failure.

    Args:
        resp (any): The response from the Lambda function

    Returns:
        bool: True if the Lambda response is considered successful
    """
    if not isinstance(resp, dict):
        return False

    status_code = resp.get("statusCode", 200)
    if status_code >= 400:
        return False
    return True


def apigw_authpolicy_check(resp) -> bool:
    """Check a response for an API Gateway Authorizer Response

    This function checks the response for an API Gateway Authorizer response.  If the response is a Deny,
    then the response is considered a failure.

    Args:
        resp (any): The response from the Lambda function

    Returns:
        bool: True if the Lambda response is considered successful
    """
    if not isinstance(resp, dict):
        return False

    effect = (
        resp.get("policyDocument", {}).get("Statement", [{}])[0].get("Effect", "Deny")
    )
    if effect == "Deny":
        return False
    return True
