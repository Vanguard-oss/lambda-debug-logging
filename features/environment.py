import io
import logging

from lambda_debug_logging import clear_buffer, register_handler


def before_scenario(context, scenario):
    context.buffer = io.StringIO()
    register_handler(stream=context.buffer)
    context.messages = []
    context.throw = None
    context.return_value = None


def after_scenario(context, scenario):
    context.buffer.truncate(0)
    clear_buffer()
