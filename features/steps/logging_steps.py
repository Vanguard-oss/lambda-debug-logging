import logging


@given('the logger "{name}" will {level} log the message "{msg}"')
def step_impl(context, name, level, msg):
    level_int = getattr(logging, level)
    context.messages.append({"logger": name, "level": level_int, "message": msg})
