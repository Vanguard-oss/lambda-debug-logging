import logging
from logging.handlers import MemoryHandler


class LevelFilterHandler(logging.Handler):
    """Only allow records that match a range of log levels"""

    def __init__(self, target, min_level=logging.DEBUG, max_level=logging.ERROR):
        logging.Handler.__init__(self)
        self._min_level = min_level
        self._max_level = max_level
        self._target = target

    def emit(self, record):
        if record.levelno >= self._min_level and record.levelno <= self._max_level:
            self._target.emit(record)

    def close(self):
        self._target.close()

    def flush(self):
        self._target.flush()


class DebugBufferHandler(MemoryHandler):
    """A MemoryBufferHandler that has a clear() method to remove unwanted messages"""

    def __init__(self, target, capacity=1024, flushLevel=logging.ERROR):
        MemoryHandler.__init__(
            self, target=target, capacity=capacity, flushLevel=flushLevel
        )

    def clear(self):
        """Clear the buffer"""
        self.buffer.clear()
