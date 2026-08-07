"""
Runtime Logger

Stage23 Production Reliability
"""

import json
from datetime import datetime
from pathlib import Path


LOG_DIR = Path("data/runtime")
LOG_FILE = LOG_DIR / "runtime.log"


class RuntimeLogger:

    def __init__(self):

        LOG_DIR.mkdir(
            parents=True,
            exist_ok=True
        )


    def log(
        self,
        component,
        status,
        duration=None,
        error=None
    ):

        record = {
            "time": datetime.now().isoformat(),
            "component": component,
            "status": status,
            "duration": duration,
            "error": str(error) if error else None
        }

        with open(
            LOG_FILE,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                json.dumps(
                    record,
                    ensure_ascii=False
                )
                + "\n"
            )


    def read_logs(self):

        if not LOG_FILE.exists():

            return []

        with open(
            LOG_FILE,
            encoding="utf-8"
        ) as f:

            return [
                json.loads(line)
                for line in f
            ]