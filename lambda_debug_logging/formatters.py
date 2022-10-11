import json
import logging
import os
import traceback
from datetime import datetime

import pytz


_tz = pytz.timezone(os.environ.get("LOG_TIMEZONE", "UTC"))


class JSONFormatter(logging.Formatter):
    """A basic Json Formatter"""

    def __init__(self):
        super().__init__()

    def format(self, record):
        record.msg = {
            "level": record.levelname,
            "name": record.name,
            "ts": datetime.fromtimestamp(record.created, _tz).isoformat(),
            "msg": record.msg,
            "module": record.module,
            "func": record.funcName,
            "line": f"{record.filename}:{record.lineno}",
        }
        if record.exc_info:
            record.msg["stacktrace"] = "\n".join(
                traceback.format_exception(
                    record.exc_info[0], record.exc_info[1], record.exc_info[2]
                )
            )
        if "_X_AMZN_TRACE_ID" in os.environ:
            record.msg["xray_trace_id"] = os.environ["_X_AMZN_TRACE_ID"]
        record.msg = json.dumps(record.msg, sort_keys=True)
        return super().format(record)
