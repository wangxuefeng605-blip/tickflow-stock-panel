from daily_report import generate_report
from telegram_bot import send_message



def main():

    print(
        "开始每日AI选股"
    )


    report=generate_report()


    send_message(
        report
    )


    print(
        "完成"
    )



if __name__=="__main__":

    main()