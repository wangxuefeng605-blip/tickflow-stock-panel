"""
AI Selector Daily Scheduler

Production scheduler for daily AI TOP10 generation.

"""

import time
from datetime import datetime


from core.daily_ai_selector import (
    run_daily_selector
)
from core.scheduler_logger import write_log
from core.runtime_lock import (
    acquire_lock,
    release_lock
)


RUN_TIME = "09:35"



def run_job():

    if not acquire_lock():

        write_log(
            "SKIP: already running"
        )

        return



    write_log(
        "START daily selector"
    )


    try:

        run_daily_selector()


        write_log(
            "SUCCESS daily selector"
        )


    except Exception as e:


        write_log(
            f"FAILED: {e}"
        )


    finally:

        release_lock()



def start_scheduler():


    print("=" * 60)

    print(
        "AI Selector Scheduler Started"
    )

    print(
        "Daily Run Time:",
        RUN_TIME
    )

    print("=" * 60)



    while True:


        now = datetime.now()


        current_time = (
            now.strftime("%H:%M")
        )


        if current_time == RUN_TIME:

            run_job()


            # 防止一分钟内重复执行

            time.sleep(70)


        time.sleep(20)



if __name__ == "__main__":

    start_scheduler()