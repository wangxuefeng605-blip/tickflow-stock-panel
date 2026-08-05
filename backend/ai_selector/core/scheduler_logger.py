"""
AI Selector Scheduler Logger
"""

from pathlib import Path
from datetime import datetime


LOG_DIR = Path(
    "data/logs"
)


LOG_FILE = LOG_DIR / "scheduler.log"



def write_log(
    message
):

    LOG_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    line = (
        f"{datetime.now()} | {message}\n"
    )


    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(line)



    return LOG_FILE