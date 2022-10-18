# lambda-debug-logging

lambda-debug-logging is a Python library that helps reduce logging costs without sacrificing debugging capabilities.  The library will automatically detect when your Lambda execution as failed.  If the execution failed, then all of your debug logs will get written out to CloudWatch.  If your execution succeeded, then only a small percentage of your debug logs will get written out to CloudWatch.

## Installation

```
$ pip install lambda-debug-logging
```

## Usage

```
from lambda_debug_logging import lambda_debug_logging, register_handler

register_handler()

@lambda_debug_logging()
def handler(event, context):
    return "success!"
```

## Failure Detection

In many scenarios, the Lambda will succeed, but what happened during the execution should be considered a failure.
A great example of that is the scenario where your Lambda is processing an HTTP request.  A lambda that successfully
sends back a 500 should still be considered a failure.  The debug logs should get sent to CloudWatch in that scenario.

### HTTP requests

When using a Lambda with an ALB or API Gateway, you can use the `http_status_code_check` function to check for status codes >= 400.

```
from lambda_debug_logging import lambda_debug_logging, failure_detection, register_handler

register_handler()

@lambda_debug_logging(response_failure_check=failure_detection.http_status_code_check)
def handler(event, context):
    return {
        "statusCode": 500
    }
```

### API Gateway Auth Policy

When using a Lambda as an API Gateway custom authorizer, you can use the `apigw_authpolicy_check` function to check for Access Denied polices.

```
from lambda_debug_logging import lambda_debug_logging, failure_detection, register_handler

register_handler()

@lambda_debug_logging(response_failure_check=failure_detection.apigw_authpolicy_check)
def handler(event, context):
    return {
        "policyDocument": {
            "Statement": [
                {
                    "Effect": "Deny"
                }
            ]
        }
    }
```

## Caveats

### Out of order logs

Log messages that use INFO or above will log in realtime.  Log messages that use DEBUG will be buffered in memory until later.
When the library determines that DEBUG logs do need to be written out, they will be flushed from memory in bulk.  This means
the DEBUG logs will show up after the INFO logs.  The default JSON Formatter includes a timestamp that allows you to re-sort
the messages to be in order, but that is an extra step you have to do.

### Filling the buffer

If your Lambda writes enough log messages, then the in-memory buffer will fill up.  Rather than lose those logs, the library
will flush those logs out.

### Lambda timeouts

The DEBUG logs will not get written when the Lambda times out.

## Why DEBUG logs are written

There are multiple reasons that DEBUG logs will get written

- The Lambda throw an exception
- The Lambda response was detected as having a failure response
- log.error() was called
- clear_buffer() was called (based on the sample rate)
- The Lambda succeeded (based on the sample rate)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

- [Basic Contributor Guide](CONTRIBUTING.md)
- [Development Guides](docs/devguide.md)

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0/)

## Dependencies

[Dependency Notices](NOTICE.md)