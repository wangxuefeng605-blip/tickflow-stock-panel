from ranking import run_ranking

from telegram_bot import send_message

from datetime import datetime




def generate_report():


    df=run_ranking()



    msg="""

📈 AI量化选股日报

日期:
{}

================

""".format(
        datetime.now()
    )



    for i,row in df.iterrows():


        msg += f"""

{i+1}.

股票:
{row['code']}

评分:
{row['score']}

趋势:
{row['trend']}

动量:
{row['momentum']}

----------------

"""



    return msg






if __name__=="__main__":


    report=generate_report()


    print(report)



    send_message(
        report
    )