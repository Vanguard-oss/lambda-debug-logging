import json
import logging
import random
import traceback

from behave import when

from lambda_debug_logging import failure_detection, lambda_debug_logging


@given("the the Lambda will fail")
def step_impl(context):
    context.throw = Exception("FAIL")


@given("a Lambda handler exists")
def step_impl(context):
    @lambda_debug_logging()
    def mock_handler(event, ctx):
        print("In Handler")
        print("Messages: " + str(context.messages))
        for msg in context.messages:
            log = logging.getLogger(msg["logger"])
            print(json.dumps(msg))
            log.log(msg["level"], msg["message"])

        if context.throw:
            raise context.throw
        return context.return_value

    context.handler = mock_handler


@given('a Lambda handler exists with sample rate of "{rate}"')
def step_impl(context, rate):
    @lambda_debug_logging(sample_rate=float(rate))
    def mock_handler(event, ctx):
        print("In Handler")
        print("Messages: " + str(context.messages))
        print(str(logging.getLogger()))
        for msg in context.messages:
            log = logging.getLogger(msg["logger"])
            log.log(msg["level"], msg["message"])

        if context.throw:
            raise context.throw
        return context.return_value

    context.handler = mock_handler


@given('a Lambda handler exists that returns "{response_type}" responses')
def step_impl(context, response_type):
    @lambda_debug_logging(
        response_failure_check=getattr(failure_detection, response_type)
    )
    def mock_handler(event, ctx):
        print("In Handler")
        print("Messages: " + str(context.messages))
        print(str(logging.getLogger()))
        for msg in context.messages:
            log = logging.getLogger(msg["logger"])
            log.log(msg["level"], msg["message"])

        if context.throw:
            raise context.throw
        return context.return_value

    context.handler = mock_handler


@given("the Lambda handler will return")
def step_impl(context):
    context.return_value = json.loads(context.text)


@given('the random seed is "{value}"')
def step_impl(context, value):
    random.seed(int(value))


@when("the Lambda is executed")
def step_impl(context):
    # Behave is resetting the log level
    logging.getLogger().setLevel(logging.DEBUG)

    context.resp = None
    context.thrown = None
    try:
        context.resp = context.handler({}, None)
    except Exception as e:
        traceback.print_exc()
        context.thrown = e
    print("logged: ")
    print(context.buffer.getvalue())


@then("the Lambda execution failed")
def step_impl(context):
    assert context.thrown is not None


@then("the Lambda execution succeeded")
def step_impl(context):
    assert context.thrown is None
