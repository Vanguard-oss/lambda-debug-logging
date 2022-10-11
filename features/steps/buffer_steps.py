@then('the logs contain "{value}"')
def step_impl(context, value):
    print(context.buffer.getvalue())
    assert value in context.buffer.getvalue()


@then('the logs do not contain "{value}"')
def step_impl(context, value):
    assert value not in context.buffer.getvalue()
