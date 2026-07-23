from apscheduler.schedulers.blocking import BlockingScheduler
from strategy import get_top10


def job():

    print("开始每日选股")

    result = get_top10()

    print(result)



scheduler = BlockingScheduler()


# 每天9:00运行
scheduler.add_job(
    job,
    "cron",
    hour=9,
    minute=0
)


print("自动选股机器人启动")

scheduler.start()
from telegram_bot import send_message


def job():

    stocks=get_top10()

    msg="📈 今日Top10\n\n"

    for s,score in stocks:
        msg+=f"{s}  {score}\n"


    send_message(msg)