"""
AI Selector Runtime Lock
"""

from pathlib import Path


LOCK_DIR = Path(
    "data/runtime"
)


LOCK_FILE = (
    LOCK_DIR /
    "daily_selector.lock"
)



def acquire_lock():

    LOCK_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    if LOCK_FILE.exists():

        return False


    LOCK_FILE.write_text(
        "running",
        encoding="utf-8"
    )


    return True



def release_lock():

    if LOCK_FILE.exists():

        LOCK_FILE.unlink()